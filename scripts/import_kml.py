"""
台灣拉麵地圖匯入工具
將 Google My Maps KML 轉換為資料庫格式

使用步驟：
1. 開啟 http://tinyurl.com/p6e9u8l
2. 點擊右上角三點 → 下載 KML
3. 執行: python import_kml.py your_map.kml
"""

import xml.etree.ElementTree as ET
import json
import sys

def parse_kml(kml_path):
    """解析 Google My Maps KML"""
    tree = ET.parse(kml_path)
    root = tree.getroot()
    
    # KML namespace
    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    
    shops = []
    for placemark in root.findall('.//kml:Placemark', ns):
        name = placemark.find('kml:name', ns)
        desc = placemark.find('kml:description', ns)
        coords = placemark.find('.//kml:coordinates', ns)
        
        if name is not None:
            shop = {
                "id": f"kml_{len(shops):04d}",
                "name": name.text,
                "description": desc.text if desc is not None else "",
                "coordinates": coords.text.strip() if coords is not None else "",
                "source": "台灣拉麵地圖 989",
                "data_quality": "from_kml"
            }
            
            # 解析座標
            if coords is not None:
                lon, lat, _ = coords.text.strip().split(',')
                shop['longitude'] = float(lon)
                shop['latitude'] = float(lat)
            
            shops.append(shop)
    
    return shops

def merge_with_database(kml_shops, existing_db_path):
    """合併到現有資料庫"""
    with open(existing_db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    
    # 建立名稱索引
    existing_names = {s['name'] for s in db['shops'] if s.get('data_quality') == 'detailed'}
    
    merged = 0
    for kml_shop in kml_shops:
        if kml_shop['name'] not in existing_names:
            # 轉換為標準格式
            new_shop = {
                "id": kml_shop['id'],
                "name": kml_shop['name'],
                "city": "待分類",  # 需根據座標判斷
                "broth_types": [],
                "price_range": {"avg": 0},
                "rating": 0,
                "coordinates": [kml_shop.get('latitude', 0), kml_shop.get('longitude', 0)],
                "data_quality": "from_kml",
                "source": "台灣拉麵地圖",
                "needs_verification": True
            }
            db['shops'].append(new_shop)
            merged += 1
    
    # 更新統計
    db['meta']['total_shops'] = len(db['shops'])
    db['meta']['last_kml_import'] = "2026-04-11"
    
    return db, merged

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python import_kml.py 地圖.kml")
        sys.exit(1)
    
    kml_path = sys.argv[1]
    shops = parse_kml(kml_path)
    print(f"解析到 {len(shops)} 家店")
    
    db, merged = merge_with_database(shops, 'ramen-database-1000.json')
    
    with open('ramen-database-1000-updated.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    
    print(f"合併 {merged} 家新店，總計 {len(db['shops'])} 家")
