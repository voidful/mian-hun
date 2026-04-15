# Changelog

## [5.2-verified] — 2026-04-15

### 262店驗證報告全面更新（30項變更）

#### 營業狀態更新
- **金龍 Taipei**: 標記為「查無此店」（驗證確認台灣無此店）
- **一樂拉麵 火影忍者**: 更新為城中店（開封街一段8號2樓）+西門店，信義旗艦店已歇業
- **梨橙溫泉拉麵**: 更名為「梨橙溫泉CAPYSPA」，確認營業中
- **龍鱗拉麵**: 確認2家分店（中山+士林二店 2025/6/17開幕）
- **麵屋鶴立**: 確認營業中（2024/9/7試營運）
- **定置漁場三代目 台北店**: 更新地址為中山北路二段39巷22號（2025/8/16開幕）
- **拉麵魚堺**: 更新為3家分店（中和/大安/中山新店），板橋店狀態存疑
- **麵屋輝 TERU**: 確認營業中，地址更新為伊通街8-1號1樓

#### 地址精確度驗證（8/9通過）
- **勝王**: 確認林森北路306號，加入殿堂制度資訊
- **塩琉**: 更新地址重慶南路一段116號，另有林森分店
- **伊禾白湯**: 確認光復南路519巷9號
- **柑橘Shinn**: 更新地址仁愛路四段228-6號，確認3家分店
- **五之神製作所**: 確認忠孝東路四段553巷6弄6號
- **牛庵**: 更新地址文心路三段107-16號
- **旨燕**: 確認開封街一段90號

#### 價格更新
- **一蘭拉麵**: 全部分店價格更新為310元（2024/4/1起調漲）

#### 連鎖品牌更新
- **一風堂**: 更新全台約20-21家分店
- **屯京拉麵**: 更新全台6家分店
- **麵屋武藏**: 更新全台6家分店（2023年營收1.2億元）

#### 新增店家
- **拉麵公子**（八德路二段279號）— 大王具足蟲拉麵創始店
- **知初拉麵 ROOT RAMEN**（忠孝東路四段216巷32弄3號）— 全植物系純素拉麵
- **雞湯桑 Torisan**（4家分店）— 雞白湯結合直火燒鳥

#### 新增資料結構
- `rankings`: 2023年度愛好會TOP10完整排名 + 殿堂制度
- `chain_brands`: 連鎖品牌分店清單（一蘭/一風堂/屯京/武藏）
- `market_pricing`: 台北拉麵市場價格行情

---

## [2.0.0] — 2026-04-13

### Added
- **Cross-platform support**: agentskills.io compatible (Hermes, Claude, ChatGPT, Gemini, Cursor, Codex)
- **Platform-specific prompts**: `prompts/` directory with optimized prompts for each LLM
- **SOURCES.md**: Complete data provenance with URLs and verification dates
- **CHANGELOG.md**: Version tracking
- **2026 shop updates**: Added 柳町家, 炊煙拉麵, Hiro's, 湮鯱, 懸日拉, 狸匠, 好呷拉麵
- **Knowledge expansion**: 20-type ramen classification (per 青木健《拉麵之魂》)
- **Health data**: Calorie ranges per broth type with source citations
- **Ramen culture history**: Taiwan-specific timeline 2000-2025

### Changed
- **SKILL.md**: Rewritten to agentskills.io standard with YAML frontmatter
- **Data sources**: All claims now traced to specific URLs
- **README.md**: Full repo documentation with quick-start for every platform
- **Recommendation engine**: Weather × broth matrix refined

## [1.0.0] — 2026-04-11

### Added
- Initial release
- 1069 shops (39 detailed + 1030 placeholder)
- Knowledge base, recommendation rules
- GitHub Pages website
- Basic LLM skill files (Claude/ChatGPT/Meta)
