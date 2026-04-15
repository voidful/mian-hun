#!/usr/bin/env python3
"""
Sync all derived data files from the master ramen-database.json.
Regenerates:
  - data/ramen-database-min.json  (minified JSON)
  - data/ramen-shops.csv          (CSV export)
  - data/shop-data.js             (JS array for website)
"""
import json
import csv
import io

DB_PATH = 'data/ramen-database.json'

with open(DB_PATH, 'r', encoding='utf-8') as f:
    db = json.load(f)

shops = db.get("shops", [])
print(f"Source: {len(shops)} shops from ramen-database.json")

# ── 1. ramen-database-min.json ──────────────────────────────
with open('data/ramen-database-min.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, separators=(',', ':'))
print("✅ ramen-database-min.json regenerated")

# ── 2. ramen-shops.csv ──────────────────────────────────────
csv_fields = [
    'id', 'name', 'city', 'district', 'address', 'mrt',
    'broth_types', 'specialties',
    'price_min', 'price_max', 'price_avg',
    'wait_time', 'rating', 'tags', 'notes', 'source', 'badge'
]

buf = io.StringIO()
writer = csv.DictWriter(buf, fieldnames=csv_fields, extrasaction='ignore',
                        lineterminator='\r\n')
writer.writeheader()
for shop in shops:
    row = dict(shop)
    # Convert list fields to pipe-separated strings
    if isinstance(row.get('broth_types'), list):
        row['broth_types'] = '|'.join(row['broth_types'])
    if isinstance(row.get('tags'), list):
        row['tags'] = '|'.join(row['tags'])
    writer.writerow(row)

with open('data/ramen-shops.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(buf.getvalue())
print("✅ ramen-shops.csv regenerated")

# ── 3. shop-data.js ─────────────────────────────────────────
def js_escape(s):
    """Escape single quotes and backslashes for JS string literals."""
    if not s:
        return ''
    return s.replace('\\', '\\\\').replace("'", "\\'")

lines = ["const S = ["]
for shop in shops:
    broth = shop.get('broth_types', [])
    if isinstance(broth, str):
        broth = [broth]
    broth_js = '[' + ', '.join(f'"{b}"' for b in broth) + ']'

    tags = shop.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    tags_js = '[' + ', '.join(f'"{js_escape(t)}"' for t in tags) + ']'

    n = js_escape(shop.get('name', ''))
    c = js_escape(shop.get('city', ''))
    d = js_escape(shop.get('district', ''))
    s = js_escape(shop.get('specialties', ''))
    m = js_escape(shop.get('mrt', ''))
    bg = js_escape(shop.get('badge', ''))
    p = shop.get('price_avg', 0)
    r = shop.get('rating', 0)
    w = js_escape(shop.get('wait_time', ''))

    lines.append(
        f"{{n:'{n}',c:'{c}',d:'{d}',b:{broth_js},"
        f"p:{p},r:{r},w:'{w}',t:{tags_js},"
        f"s:'{s}',m:'{m}',bg:'{bg}'}},"
    )
lines.append("];")

with open('data/shop-data.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print("✅ shop-data.js regenerated")

print(f"\n🎉 All 3 derived files synced with {len(shops)} shops.")
