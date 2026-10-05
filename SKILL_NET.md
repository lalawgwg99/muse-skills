# 技能網（Skill Net）

> 2026-10-05 提出「技能樹」，後修正為網：節點是 skill，邊是互補／fallback／工作流關係。
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
- threads/meta-threads：Threads 經營【2026-10-06 註：帳號尚未連結（待 Meta 授權），節點暫時失效】
- whatsapp：通知推送（日報／快訊送達；僅與使用者一對一傳訊，不能代聯繫他人）
- instagram：IG、Reels
- facebook-cli：FB
- meta-ads：廣告投放
- social-content-performance：成效分析（數據回流）
- vocus（API，未包裝）：慢錢研究所發文

### 資料層 — 存、算、管
- google-sheets：試算表（外送紀錄、數據）【2026-10-06 註：連接器已由使用者手動斷開，節點暫時失效】
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

### 觀察中（未安裝，不列邊）
- agent-reach：給 AI Agent 接網路能力的開源專案；評估中，使用者尚未點頭（目錄內尚無 SKILL.md）

---

## 邊 — 互補與 fallback（網的密度在這裡）

**研究互補**
- exa-search ↔ browser.search：Exa 語義深、browser 即時快。突發新聞先 browser（news vertical），背景深挖再用 Exa；browser.search 若回 401/session_invalid 就降級走題庫觀念文、不硬等新聞【2026-10-03 實測】
- exa-search ↔ x-post-reader：X 是 Exa 的盲區，X 內容一律走 x-post-reader
- social.search → x-post-reader：先找到爆文（social），再讀全文細節（x-post-reader）
- image-search ↔ media-library：先翻自己的照片庫，沒有才去外網找
- wide-research ↔ exa-search：要快用 Exa，要深用 wide-research；可先 Exa 掃、再 wide-research 深挖
- places-search ↔ browser.search：店家資訊先 places，營業時間／評價異常時 browser 交叉

**生產互補**
- muse-video → tts：策劃完直接配音，說書產線固定這條
- media → image-search：生成前先找參考圖，避免風格跑偏；media.generate_image 憑證失敗時改 PIL 自繪封面【2026-10-03 實測】
- media-library → media：有參考照時當輸入（男友 POV 續集、柴犬角色一致性）
- tts → podcast：單段配音 vs 完整節目，看長度選

**發布互補**
- threads ↔ instagram ↔ facebook-cli：同一內容改寫多發，看平台調性【2026-10-06 註：threads 節點暫時失效，改發環節先由 instagram／facebook-cli 覆蓋】
- social-content-performance → social.search：看數據 → 回頭找下一波爆款（迴路）
- meta-ads：自然流量起不來時才考慮，不主動推

**資料互補**
- google-sheets ↔ artifacts：外送資料雙棲，試算表存檔、網頁給師傅【2026-10-06 註：sheets 側暫斷，artifacts 單邊運作】
- github → （Cloudflare Pages）：推送即部署，TaiCalc／字研所／shift-fill 固定這條
- google-drive ↔ media-library：大檔案走 drive，常用照片走 media-library

**跨層 fallback**
- 任何「要查 X」→ x-post-reader（不要用 exa-search 硬碰）
- 任何「要即時」→ browser.search 對應 vertical（不要等 Exa 索引）
- 任何「要他照片」→ media-library 優先
- 付費／下單／授權節點 → 一律停在使用者面前（錢、帳號、授權不自動過）
- browser.spawn_task 若回 browser_vm_lease_unavailable → 無備援，任務延期；迴路設計須容忍單日缺發【2026-10-03 實測，缺口待補】

---

## 迴路 — 高頻工作流（端到端，含回流）

1. **慢錢研究所每日**：exa-search／browser.search 選題（每日 07:00 選題補給排程）→ 寫作 → image-search 封面 → vocus 發布 → social-content-performance 看數據 → 回流選題
2. **爆紅影片工廠**：social.search 找爆款 → muse-video 策劃 → tts 配音 → 發布 → 數據回流
3. **X 經營**：social.search/x-post-reader 找話題 → exa-search 補背景 → 寫文 → 發布
4. **柴犬圖卡**：文案 → image-search 找參考 → media 生成 → threads 發布 → 數據回流
5. **外送單**：照片轉錄 → 排序 → artifacts 網頁版 ＋ LINE 文字版（文字版 = 他的查詢庫）
6. **網站 SEO**：exa-search 長尾關鍵字 → 寫文 → github 推送 → Search Console 數據回流（每週跟他要）
7. **說書／短劇影片**：選書 → exa-search 找資料 → muse-video 策劃 → tts 配音 → media.generate_image 分鏡 → ffmpeg 成片 → 發布【2026-10-01 短劇實測驗證此鏈】

## 織網原則
1. 新 skill 上線先回答：它補哪個缺口？跟誰互補？進哪條迴路？
2. Fallback 寫死，不靠臨場想：A 不行自動換 B
3. 錢、帳號、授權、公開發布四個節點永遠是人工閘門
4. 每日自動檢查斷掉的邊（連接器斷開、帳號未授權就標註暫失效），每季人工複檢（API 改版、服務下線就換線）
5. 每日 04:00 自動優化（cron `skill-net-daily-optimize`）：掃新 skill、修斷邊、按實際使用調整工作流、有變動就同步推 GitHub；無事不打擾
