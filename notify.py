import os
import json
import re
import requests
from datetime import datetime
from pathlib import Path

TG_TOKEN  = os.environ.get('TG_TOKEN',  '')
TG_CHAT_ID = os.environ.get('TG_CHAT_ID', '')

SS_URL   = 'https://www.ss.com/lv/transport/cars/tesla/today/'
DBA_URL  = 'https://www.dba.dk/mobility/search/car?variant=0.8078'
SS_BASE  = 'https://www.ss.com'
DKK_RATE = 7.46

SEEN_FILE = Path('seen_listings.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/124.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}


# ── Persistence ───────────────────────────────────────────────────────────────

def load_seen():
    if SEEN_FILE.exists():
        try:
            return json.loads(SEEN_FILE.read_text())
        except Exception:
            pass
    return {}

def save_seen(seen):
    SEEN_FILE.write_text(json.dumps(seen, indent=2))


# ── Fetch ─────────────────────────────────────────────────────────────────────

def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.text


# ── ss.com parser ─────────────────────────────────────────────────────────────

def parse_ss(html):
    listings = []
    row_re = re.compile(r'<tr[^>]*id="tr_[^"]*"[^>]*>([\s\S]*?)</tr>', re.IGNORECASE)

    for match in row_re.finditer(html):
        row = match.group(1)

        link_m = re.search(r'href="(/msg/lv/transport/cars/tesla/[^"]+\.html)"', row)
        if not link_m:
            continue
        url = SS_BASE + link_m.group(1)

        title = ''
        for tm in re.finditer(r'href="[^"]+\.html"[^>]*>([^<]{5,})<', row):
            t = tm.group(1).strip()
            if not re.match(r'^[\d,.\s€]+$', t) and re.match(r'^[A-Za-z]', t):
                title = t
                break

        price_m   = re.search(r'([\d\s]{3,}\s*€)', row)
        mileage_m = re.search(r'([\d]+\s*tūkst\.?)', row)
        year_m    = re.search(r'\b(19|20)\d{2}\b', row)
        img_m     = re.search(r'src="(https?://i\.ss\.com/gallery/[^"]+\.th2\.jpg)"', row)

        listings.append({
            'url':     url,
            'title':   title,
            'price':   price_m.group(1).strip() if price_m else '',
            'mileage': mileage_m.group(1) if mileage_m else '',
            'year':    year_m.group(0) if year_m else '',
            'images':  [img_m.group(1)] if img_m else [],
            'source':  'ss',
        })

    return listings


# ── dba.dk parser ─────────────────────────────────────────────────────────────

def _deep_find(obj, depth=0):
    """Recursively find the first array that looks like a listing collection."""
    if depth > 15 or not isinstance(obj, (dict, list)):
        return None
    if isinstance(obj, list) and len(obj) >= 2:
        f = obj[0]
        if isinstance(f, dict):
            has_title = any(f.get(k) for k in ('heading', 'name', 'title'))
            has_data  = any(f.get(k) for k in ('price', 'year', 'mileage', 'canonicalUrl', 'url', 'images'))
            if has_title and has_data:
                return obj
        for item in obj:
            r = _deep_find(item, depth + 2)
            if r:
                return r
        return None
    if isinstance(obj, dict):
        for v in obj.values():
            r = _deep_find(v, depth + 1)
            if r:
                return r
    return None


def _normalize_dba(item):
    if not isinstance(item, dict):
        return None
    title = item.get('heading') or item.get('name') or item.get('title') or ''
    if not title:
        return None
    url = item.get('canonicalUrl') or item.get('url') or item.get('href') or ''
    if not url or not url.startswith('http'):
        return None

    raw_price = item.get('price') or (item.get('offers') or {}).get('price')
    price = ''
    if raw_price is not None:
        digits = re.sub(r'\D', '', str(raw_price))
        if digits:
            price_num = int(digits)
            if price_num > 0:
                price = f"{round(price_num / DKK_RATE):,} €"

    year = str(item.get('year') or item.get('modelYear') or '')

    raw_mile = (item.get('mileage') or item.get('kilometertal')
                or item.get('odometer') or item.get('km') or '')
    mileage = ''
    if raw_mile:
        if isinstance(raw_mile, dict):
            raw_mile = raw_mile.get('amount') or raw_mile.get('value') or 0
        digits = re.sub(r'\D', '', str(raw_mile))
        if digits:
            mileage = f"{int(digits):,} km"

    images = []
    for src_key in ('images', 'image', 'photos', 'media'):
        img_src = item.get(src_key)
        if img_src:
            if isinstance(img_src, list):
                for img in img_src:
                    u = (img.get('url') or img.get('src') or '') if isinstance(img, dict) else str(img)
                    if u.startswith('http'):
                        images.append(u)
            break

    return {
        'url': url, 'title': title, 'price': price,
        'mileage': mileage, 'year': year, 'images': images, 'source': 'dba',
    }


def parse_dba(html):
    # Strategy 1: __NEXT_DATA__
    next_m = re.search(r'<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)</script>', html)
    if next_m:
        try:
            data  = json.loads(next_m.group(1))
            items = _deep_find(data)
            if items:
                out = [_normalize_dba(i) for i in items]
                out = [x for x in out if x]
                if out:
                    return out
        except Exception as e:
            print(f'[dba] __NEXT_DATA__ error: {e}')

    # Strategy 2: regex scan for dba listing URLs
    listings, seen_urls = [], set()
    for m in re.finditer(r'"(https?://(?:www\.)?dba\.dk/[^"]*?/\d{6,}[^"]*)"', html):
        url = m.group(1).split('?')[0]
        if url in seen_urls or not re.search(r'\d{6,}', url):
            continue
        seen_urls.add(url)
        ctx = html[max(0, m.start() - 800): m.start() + 2000]

        title_m = re.search(r'"(?:heading|name|title|label)"\s*:\s*"([^"]{5,120})"', ctx)
        price_m = re.search(r'"(?:price|amount|priceCash)"\s*:\s*"?([\d.,]+)"?', ctx)
        year_m  = re.search(r'"(?:year|modelYear)"\s*:\s*(\d{4})', ctx)
        mile_m  = re.search(r'"(?:mileage|kilometertal|odometer|km)"\s*:\s*"?([\d.,]+)"?', ctx)
        img_m   = re.search(
            r'"(?:url|src|imageUrl)"\s*:\s*"(https?://[^"]*dbastatic[^"]*\.(?:jpg|jpeg|png|webp))"',
            ctx, re.IGNORECASE)

        price_num = int(re.sub(r'\D', '', price_m.group(1))) if price_m else None
        mile_num  = int(re.sub(r'\D', '', mile_m.group(1)))  if mile_m  else None

        listings.append({
            'url':     url,
            'title':   title_m.group(1) if title_m else '',
            'price':   f"{round(price_num / DKK_RATE):,} €" if price_num else '',
            'mileage': f"{mile_num:,} km" if mile_num is not None else '',
            'year':    year_m.group(1) if year_m else '',
            'images':  [img_m.group(1)] if img_m else [],
            'source':  'dba',
        })

    return listings


# ── Telegram ──────────────────────────────────────────────────────────────────

def wsrv_url(src):
    """Route image through images.weserv.nl to bypass ss.com hotlink protection."""
    from urllib.parse import quote
    return f'https://images.weserv.nl/?url={quote(src, safe="")}'


def send_telegram(listing):
    full_url = listing['url'] if listing['source'] == 'dba' else SS_BASE + listing['url']

    lines = [f"🚗 <b>{listing.get('title') or 'New Tesla listing'}</b>"]
    if listing.get('price'):   lines.append(f"💰 {listing['price']}")
    if listing.get('mileage'): lines.append(f"🛣 {listing['mileage']}")
    if listing.get('year'):    lines.append(f"📅 {listing['year']}")
    lines.append(f'<a href="{full_url}">View listing ↗</a>')
    caption = '\n'.join(lines)

    base = f'https://api.telegram.org/bot{TG_TOKEN}'

    if listing.get('images'):
        # Use weserv to proxy the image so Telegram can download it
        photo_url = wsrv_url(listing['images'][0]) if 'ss.com' in listing['images'][0] else listing['images'][0]
        try:
            r = requests.post(f'{base}/sendPhoto', json={
                'chat_id':    TG_CHAT_ID,
                'photo':      photo_url,
                'caption':    caption,
                'parse_mode': 'HTML',
            }, timeout=15)
            if r.json().get('ok'):
                return
        except Exception:
            pass

    # Fallback: text only
    requests.post(f'{base}/sendMessage', json={
        'chat_id':    TG_CHAT_ID,
        'text':       caption,
        'parse_mode': 'HTML',
        'disable_web_page_preview': False,
    }, timeout=15)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not TG_TOKEN or not TG_CHAT_ID:
        print('TG_TOKEN / TG_CHAT_ID not set — skipping')
        return

    seen = load_seen()
    is_first_run = len(seen) == 0
    now = datetime.utcnow().isoformat()

    # Fetch both sources
    ss_listings, dba_listings = [], []

    try:
        ss_listings = parse_ss(fetch(SS_URL))
        print(f'[ss.com] {len(ss_listings)} listing(s)')
    except Exception as e:
        print(f'[ss.com] error: {e}')

    try:
        dba_listings = parse_dba(fetch(DBA_URL))
        print(f'[dba.dk] {len(dba_listings)} listing(s)')
    except Exception as e:
        print(f'[dba.dk] error: {e}')

    # Find new listings
    new_listings = []
    for l in ss_listings + dba_listings:
        if l['url'] not in seen:
            seen[l['url']] = now
            if not is_first_run:
                new_listings.append(l)

    save_seen(seen)

    if is_first_run:
        print(f'First run — {len(seen)} listing(s) marked as seen. No notifications sent.')
        return

    print(f'{len(new_listings)} new listing(s)')
    for l in new_listings:
        print(f'  → [{l["source"]}] {l["title"]} | {l["price"]} | {l["url"]}')
        try:
            send_telegram(l)
        except Exception as e:
            print(f'  Telegram error: {e}')


if __name__ == '__main__':
    main()
