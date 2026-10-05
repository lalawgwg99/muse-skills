# 技能網（Skill Net）

> 2026-10-05 榮德提出「技能樹」，後修正為網：節點是 skill，邊是互補／fallback／工作流關係。
> 維護規則：每新增一個 skill，標註它連向哪些節點、補什麼缺口、進哪條迴路。

## 節點（按層）

### 研究層 — 找資料、找靈感
- exa-search：全網語義搜尋（選題、話題挖掘、背景資料）
- x-post-reader：X 單篇貼文讀取
- social.search：社群話題、爆款搜尋
- browser.search：即時搜尋（news/sports/finance/datetime）
- wide-research：深度研究報告
- image-search：找圖（封面、參考、靈感）
- media-library：他自己的照片庫
- places-search：地點搜尋（店家、座標）

### 生產層 — 內容製造
- muse-video：影片前期策劃（分鏡、虛擬劇組）
- tts：配音（台灣腔國語）
- podcast/generate_podcast：完整音頻節目
- magic-moment：短影音魔法時刻
- media（圖像生成）：柴犬圖卡、海報、縮圖
- canva：設計備用

### 發布層 — 各平台出去
- threads/meta-threads：Threads 經營
- instagram：IG、Reels
- facebook-cli：FB
- meta-ads：廣告投放
- social-content-performance：成效分析（數據回流）
- vocus（API，未包裝）：慢錢研究所發文

### 資料層 — 存、算、管
- google-sheets：試算表（外送紀錄、數據）
- google-drive：檔案（照片、影片檔）
- google-docs：文件
- github：程式碼推送（TaiCalc、字研所、shift-fill）
- artifacts：網頁成品管理
- plaid：銀行帳務

### 日常層
- gmail/outlook-mail、google-calendar、flightaware、duffel（機票）、travel-planning、shopping（比價購物）、spotify（配樂找歌）

### 系統層
- skill-creator：建新 skill（織網的梭子）
- goals：目標追蹤
- subscription-status：額度查詢
- muse-feedback：問題回報

---

## 邊 — 互補與 fallback（網的密度在這裡）

**研究互補**
- exa-search ↔ browser.search：Exa 語義深、browser 即時快。突發新聞先 browser（news vertical），背景深挖再用 Exa
- exa-search ↔ x-post-reader：X 是 Exa 的盲區，X 內容一律走 x-post-reader
- social.search → x-post-reader：先找到爆文（social），再讀全文細節（x-post-reader）
- image-search ↔ media-library：先翻自己的照片庫，沒有才去外網找
- wide-research ↔ exa-search：要快用 Exa，要深用 wide-research；可先 Exa 掃、再 wide-research 深挖
- places-search ↔ browser.search：店家資訊先 places，營業時間／評價異常時 browser 交叉

**生產互補**
- muse-video → tts：策劃完直接配音，說書產線固定這條
- media → image-search：生成前先找參考圖，避免風格跑偏
- media-library → media：有參考照時當輸入（男友 POV 續集、柴犬角色一致性）
- tts → podcast：單段配音 vs 完整節目，看長度選

**發布互補**
- threads ↔ instagram ↔ facebook-cli：同一內容改寫多發，看平台調性
- social-content-performance → social.search：看數據 → 回頭找下一波爆款（迴路）
- meta-ads：自然流量起不來時才考慮，不主動推

**資料互補**
- google-sheets ↔ artifacts：外送資料雙棲，試算表存檔、網頁給師傅
- github → （Cloudflare Pages）：推送即部署，TaiCalc／字研所／shift-fill 固定這條
- google-drive ↔ media-library：大檔案走 drive，常用照片走 media-library

**跨層 fallback**
- 任何「要查 X」→ x-post-reader（不要用 exa-search 硬碰）
- 任何「要即時」→ browser.search 對應 vertical（不要等 Exa 索引）
- 任何「要他照片」→ media-library 優先
- 付費／下單／授權節點 → 一律停在他面前（錢、帳號、授權不自動過）

---

## 迴路 — 高頻工作流（端到端，含回流）

1. **慢錢研究所每日**：exa-search 選題 → 寫作 → image-search 封面 → vocus 發布 → social-content-performance 看數據 → 回流選題
2. **爆紅影片工廠**：social.search 找爆款 → muse-video 策劃 → tts 配音 → 發布 → 數據回流
3. **X 經營**：social.search/x-post-reader 找話題 → exa-search 補背景 → 寫文 → 發布
4. **柴犬圖卡**：文案 → image-search 找參考 → media 生成 → threads 發布 → 數據回流
5. **外送單**：照片轉錄 → 排序 → artifacts 網頁版 ＋ LINE 文字版（文字版 = 他的查詢庫）
6. **網站 SEO**：exa-search 長尾關鍵字 → 寫文 → github 推送 → Search Console 數據回流（每週跟他要）
7. **說書影片**：選書 → exa-search 找資料 → muse-video 策劃 → tts 配音 → 發布

## 織網原則
1. 新 skill 上線先回答：它補哪個缺口？跟誰互補？進哪條迴路？
2. Fallback 寫死，不靠臨場想：A 不行自動換 B
3. 錢、帳號、授權、公開發布四個節點永遠是人工閘門
4. 每季檢查一次斷掉的邊（API 改版、服務下線就換線）
