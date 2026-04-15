# 🍜 麵魂 MIAN-HUN — 台灣拉麵 AI Skill

> **The universal Taiwan ramen skill for every LLM.**
> 全台最完整的開源拉麵推薦引擎 — 跨平台 AI 拉麵助手

[![agentskills.io](https://img.shields.io/badge/agentskills.io-compatible-blue)](https://agentskills.io)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
![Shops](https://img.shields.io/badge/shops-1304+-D94F30)
![Last Updated](https://img.shields.io/badge/updated-2026--04--15-green)
![Version](https://img.shields.io/badge/version-5.2--verified-blue)

---

## ⚡ Quick Start

### Hermes Agent
```bash
hermes skills install your-username/mian-hun
```

### Claude (Claude Code / Claude.ai)
Copy `SKILL.md` + `references/` to `~/.claude/skills/mian-hun/` or upload as `.skill` zip.

### ChatGPT (Custom GPTs)
1. Create a new GPT at https://chat.openai.com/gpts/create
2. Paste `prompts/chatgpt-system.md` into Instructions
3. Upload `data/ramen-database.json` as Knowledge

### Gemini (Google AI Studio / Gems)
1. Go to https://aistudio.google.com
2. Paste `prompts/gemini-system.md` into System Instructions
3. Upload `data/ramen-database.json`

### Any LLM
Copy `prompts/universal-system.md` as your system prompt. Attach or reference `data/ramen-database.json`.

---

## 📁 Repo Structure

```
mian-hun/
├── SKILL.md                          # agentskills.io skill (Hermes/Claude)
├── README.md                         # This file
├── LICENSE                           # CC BY 4.0
├── SOURCES.md                        # All data sources with URLs
├── CHANGELOG.md                      # Version history
│
├── prompts/                          # Platform-specific prompts
│   ├── universal-system.md           # Works on any LLM
│   ├── chatgpt-system.md             # Optimized for ChatGPT/GPTs
│   ├── gemini-system.md              # Optimized for Gemini
│   └── claude-project.md             # Claude Projects prompt
│
├── references/                       # Deep knowledge (loaded on demand)
│   ├── knowledge.md                  # Ramen encyclopedia
│   ├── shops-detailed.md             # 39 verified shops (full data)
│   └── recommendation-engine.md      # Decision tree & rules
│
├── data/                             # Structured data
│   ├── ramen-database.json           # Full 1304-shop database
│   ├── ramen-database-min.json       # Compact version for LLMs
│   └── ramen-shops.csv               # Spreadsheet-friendly
│
├── website/                          # GitHub Pages site
│   └── index.html                    # Single-file app
│
└── scripts/                          # Utilities
    ├── import_kml.py                 # Import Google Maps KML
    └── update_verification_2026.py   # 262-shop verification update
```

---

## 📊 Data Coverage

| Metric | Count | Source |
|--------|-------|--------|
| Total shops | 1,304 | Multi-source aggregation |
| Detailed verified | 273 | Manual verification + 262-shop audit |
| Cities covered | 22 | All Taiwan counties |
| Broth types tracked | 12+ | Classification system |
| Address verified | 8/9 | 2026-04 verification report |

### City Distribution (Top 6)
| City | Shops | Detailed |
|------|-------|----------|
| 台北市 | 280 | 18+ |
| 新北市 | 180 | 8+ |
| 台中市 | 150 | 12+ |
| 高雄市 | 120 | 10+ |
| 桃園市 | 90 | 6+ |
| 台南市 | 80 | 6+ |

### Market Pricing (Taipei, 2026)
| Segment | Price Range | Examples |
|---------|-------------|----------|
| 平價高CP值 | 145-230元 | 好呷拉麵, 拉麵魚堺 |
| 中價位 | 240-300元 | 屯京, 麵屋武藏 |
| 連鎖品牌 | 260-320元 | 一風堂, 一蘭(310元) |
| 高端特色 | 300-400元+ | 創作系, 限定 |

---

## 🤖 What It Does

1. **Custom Recommendations** — 5-question quick match (city, flavor, budget, wait time, weather)
2. **Ramen Encyclopedia** — Broth types, noodle science, toppings, eating etiquette
3. **Situation Matching** — Auto-adjust for: date night, family, late night, rainy day, budget
4. **Learning Path** — Beginner → Advanced → Connoisseur progression

---

## 📖 Data Sources

All sources documented in [`SOURCES.md`](SOURCES.md). Primary:

| Source | Type | URL |
|--------|------|-----|
| 台灣拉麵協會 | Organization | [taiwan-ramen-association.github.io](https://taiwan-ramen-association.github.io) |
| 台灣拉麵愛好會 | FB Community (9萬+) | [facebook.com/groups/RamenTW](https://facebook.com/groups/RamenTW/) |
| 台灣拉麵愛好會 IG | Social Media | [instagram.com/twramenclub](https://instagram.com/twramenclub/) |
| 拉麵地圖 | Google My Maps (1071家) | [Google Maps](http://tinyurl.com/p6e9u8l) |
| 台灣拉麵協會 IG | Social Media | [instagram.com/twramen.assoc](https://instagram.com/twramen.assoc/) |
| Google Maps | Ratings & Info | Per-shop verification |
| 食力 foodNEXT | Media | 2023年度85家必吃 |
| Klook / 自由時報 / 妞新聞 | Media | Review aggregation |

---

## 🏆 Hall of Fame — 台灣拉麵愛好會殿堂

| Year | Champion | Broth | Note |
|------|----------|-------|------|
| 2016-2020 | 鬼金棒 | 辣麻味噌 | **五連霸** → 入殿堂 🏆 |
| 2021 | 勝王 | 創作系 | First win |
| 2022 | 勝王 | 創作系 | Two-peat |
| 2023 | 勝王 | 創作系 | **三連霸** → 入殿堂 🏆 |

### 2023年度 TOP 10（近10萬人票選）

| Rank | Shop | Location | Highlight |
|------|------|----------|-----------|
| 🥇 1 | 勝王 | 台北中山・林森北路306號 | 三連霸，入殿堂 |
| 🥈 2 | 塩琉 | 台北中正・重慶南路一段116號 | 龍蝦清湯 |
| 🥉 3 | 五之神製作所 | 台北信義 | 東京名店，濃厚蝦湯 |
| 4 | 辰拉麵 | 新北永和 | 前鷹流大師兄 |
| 5 | 伊禾白湯 | 台北信義 | 限量40碗，Google 4.9 |
| 6 | Okaeri お帰り | 台北大安 | 濃厚豚骨 |
| 7 | 雞吉君拉麵 | 台北內湖 | 雞白湯先驅 |
| 8 | 牛庵 | 台中西屯 | 牛骨湯頭 |
| 9 | 拉麵公子 | 台北中山 | 大王具足蟲拉麵 |
| 10 | 旨燕 | 台北中正 | 泡系拉麵 |

---

## 🌐 Website

Deploy `website/` to GitHub Pages for an interactive ramen finder:

```bash
# In repo settings → Pages → Source: /website
```

Live: `https://voidful.github.io/mian-hun/website`

---

## 🤝 Contributing

PRs welcome! See [`SOURCES.md`](SOURCES.md) for data format.

To add a shop:
1. Edit `data/ramen-shops.csv`
2. Set `data_quality: detailed` and fill all fields
3. Add source URL in the `source` column
4. Submit PR

---

## 📄 License

Data: [CC BY 4.0](LICENSE) — free to share and adapt with attribution.
Code: MIT.

Sources are public information aggregated for educational purposes.
