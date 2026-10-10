# 技能網（Skill Net）

> 2026-10-05 提出「技能樹」，後修正為網：節點是 skill，邊是互補／fallback／工作流關係。
> 維護規則：每新增一個 skill，標註它連向哪些節點、補什麼缺口、進哪條迴路。

## 節點（按層）

### 研究層 — 找資料、找靈感
- exa-search：全網語義搜尋（選題、話題挖掘、背景資料）【2026-10-05 註：API key 曾異常，後已恢復正常；x.com／twitter.com 限定搜尋實測回 0 筆，不做 X 搜尋】
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
- github：程式碼推送（TaiCalc、字研所、shift-fill、外送頁）
- cloudflare：Cloudflare API（DNS、網域 Registrar、Pages 自訂網域、SSL）【2026-10-07 新增：使用者接 `custom.cloudflare` 連接器＋親建 workspace skill；憑證存 Secure Vault，不存原始 Token／金鑰】【2026-10-09：使用者已訂閱 Workers Paid（US$5／月）並授權高價值功能儘量用；ai-proxy 已搬 KV 限流（RATE_LIMIT_KV）、新增 D1 ai-logs 問答觀測】
- artifacts：網頁成品管理
- plaid：銀行帳務

### 日常層
- gmail/outlook-mail、google-calendar、flightaware、duffel（機票）、travel-planning、shopping（比價購物）、spotify（配樂找歌）

### 系統層
- skill-creator：建新 skill（織網的梭子）
- openrouter：免費 AI 模型池（:free only，絕不動帳戶餘額；每日 1000 次免費額度）。機械性批量工作（初篩、翻譯、摘要、分類）的便宜算力；主力模型每天約 06:24 由 `openrouter-free-model-scan` 排程掃描更新 `state/free-model.json`（動態路由，不寫死模型 ID）；憑證走 Secure Vault（custom.openrouter），不存原始 key【2026-10-09 新建 skill；使用者立鐵律：只能用免費模型】【2026-10-10 實戰：nemotron 請求掛住逾時、gemma 上游 429 → 每日獵捕初篩改由主模型做，免費池不可用不硬等】
- goals：目標追蹤
- subscription-status：額度查詢
- muse-feedback：問題回報

### 觀察中（未安裝，不列邊）
- agent-reach：給 AI Agent 接網路能力的開源專案；評估中（目錄內尚無 SKILL.md，未 pip install、未完成可用性驗證，不可記成已安裝）。2026-10-07 使用者同意將 AI 工具獵人計畫封存（03:00 每日獵捕排程保留作火種，命中絕不自動安裝）；agent-reach 是否正式納入仍待確認
- claw-browser-anchor（候選，未安裝）：DOM 錨點瀏覽器自動化方法論；可參考作為 browser.spawn_task 租用 VM 失敗時的備援思路（該缺口 2026-10-03 實測至今無備援，2026-10-09 複查仍無備援）。2026-10-08 深入研究完成，結論＝不建議安裝整包，只吸收方法論：super-research 輕量版驗證紀律已寫入慢錢研究所流程（見迴路#1），DOM 錨點優先／動作後驗證／漂移恢復可作瀏覽器任務規範；安裝本身無額外價值。絕不自動安裝

---

## 邊 — 互補與 fallback（網的密度在這裡）

**研究互補**
- exa-search ↔ browser.search：Exa 語義深、browser 即時快。突發新聞先 browser（news vertical），背景深挖再用 Exa；browser.search 若回 401/session_invalid 就降級走題庫觀念文、不硬等新聞【2026-10-03 實測】
- exa-search ↔ x-post-reader：X 是 Exa 的盲區（2026-10-05 實測 x.com 限定搜尋回 0 筆），X 內容一律走 x-post-reader；x-post-reader 內部 fallback＝browser.open → 唯讀 live browser（不登入、不繞牆）【2026-10-01 實測鏈，多篇 X 貼文已實戰成功讀取】
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
- threads ↔ instagram ↔ facebook-cli：同一內容改寫多發，看平台調性【2026-10-06 註、10-10 複查仍未連結（待 Meta 授權），改發環節由 instagram／facebook-cli 覆蓋】
- social-content-performance → social.search：看數據 → 回頭找下一波爆款（迴路）
- meta-ads：自然流量起不來時才考慮，不主動推

**資料互補**
- google-sheets ↔ artifacts：外送資料已遷至 GitHub（private repo 存檔）＋ Cloudflare Pages 網頁給師傅；試算表／GAS 查詢方案 10-04 已棄。google-sheets 連接器自 10-02 由使用者手動斷開、10-10 複查仍斷，不主動重連
- github → （Cloudflare Pages）：推送即部署，TaiCalc／字研所／shift-fill／外送頁 固定這條【2026-10-08 實戰：外送頁 private repo 推送後 Pages 自動部署成功】
- github ↔ cloudflare：github 推送管「程式碼→部署」，cloudflare 管「網域→DNS→SSL→上線」；新站流程＝cloudflare 先買網域／掛 Pages 自訂網域＋DNS，再 github 推碼生效【2026-10-07 實戰：carepilot1966.com 經 Registrar 購買＋加到 care-calculator Pages 專案；含個資的頁面走 private repo，不公開原始碼】【2026-10-09 實戰：易問 Worker `iching-api` 正式服務一律配自訂網域路由（proxied DNS `yiwen-api.taicalc.com` → Worker route），不依賴 workers.dev——workers.dev 在本環境回 1042、使用者實機亦 Load failed，改正式網域路由後 POST /divine 端到端成功】
- cloudflare 錢閘：網域購買、付費操作一律人工決定（2026-10-07 是使用者親自買 carepilot1966.com），skill 只做技術執行
- google-drive ↔ media-library：大檔案走 drive，常用照片走 media-library

**免費算力互補（openrouter）**
- openrouter ↔ 主模型分工：機械性批量工作（初篩、翻譯、摘要、分類）自動走 :free 免費模型，不再逐次詢問；需要判斷、要品質的工作主模型自己做【2026-10-09 使用者確認成本原則】
- openrouter → 每日獵捕初篩：skill-scan 第一層「相關」批量初判讀當天 free-model.json 走免費模型【2026-10-09 接上；2026-10-10 03:00 實戰：nemotron 請求掛住逾時（>9 分鐘）、gemma 上游 429 → 改由主模型自行初篩，「免費池不可用不硬等」fallback 真實觸發，未打擾使用者；2026-10-11 連兩天重演（nemotron 長請求 240s 逾時）→ 主模型自行初篩已成穩定 fallback；當日 21 新候選全屬已知排除類別，無新 skill 需織入】
- openrouter 鐵律：只用 :free（pricing 全 0）模型，絕不呼叫付費模型、不動帳戶餘額；key 只經 Secure Vault／env，不進檔案與 log
- 免費模型不穩定是常態：名單會洗牌（2026-10-09 實測 gemma 回 429、llama-3.3-70b 回 404，只剩 nemotron 可用）；超時必須包住 headers＋body 全程（r.json() 也在 abort 內），重試不做乘法【2026-10-09 聖所實戰教訓】
- 反向邊（不連網站）：三站 AI 助手（小算／小研／小伴）維持 Cloudflare Workers AI（Llama 3.1 8B），不接 OpenRouter——免費共享池限流會傷訪客體驗、便宜模型指令遵循較差可能破「只回本站相關問題」鐵律、key 塞進 Worker 多一個外洩面【2026-10-09 決定】
- 聖所 AI 鏈路：OpenRouter :free 第一順位 → pollinations 免 key 備援 → 瀏覽器直連第三層【2026-10-09 實戰上線】

**跨層 fallback**
- 任何「要查 X」→ x-post-reader（不要用 exa-search 硬碰）
- 任何「要即時」→ browser.search 對應 vertical（不要等 Exa 索引）
- 任何「要他照片」→ media-library 優先
- 付費／下單／授權節點 → 一律停在使用者面前（錢、帳號、授權不自動過）
- browser.spawn_task 若回 browser_vm_lease_unavailable → 無備援，任務延期；迴路設計須容忍單日缺發【2026-10-03 實測，缺口待補】

---

## 迴路 — 高頻工作流（端到端，含回流）

1. **慢錢研究所每日**：exa-search／browser.search 選題（每日 07:00 選題補給排程）→ 寫作 → image-search 封面 → vocus 發布 → social-content-performance 看數據 → 回流選題【2026-10-08 吸收 genspark-claw super-research 輕量版驗證紀律：選題與品質紅線現含「關鍵主張開來源頁確認、關鍵數字兩獨立來源交叉驗證、衝突並陳、不確定標「目前已知」、驗證不過刪掉不寫」；整包未安裝、只取方法論】【2026-10-09：方格子恢復全自動（A 帳號登入狀態正常）；ProseMirror 長文輸入損壞防呆已上（一次性貼全文＋貼後讀回驗證＋連兩次失敗停手請人工貼上），首次新流程尚待實跑驗證】
2. **爆紅影片工廠**：social.search 找爆款 → muse-video 策劃 → tts 配音 → 發布 → 數據回流
3. **X 經營**：social.search/x-post-reader 找話題 → exa-search 補背景 → 寫文 → 發布
4. **柴犬圖卡**：文案 → image-search 找參考 → media 生成 → threads 發布 → 數據回流
5. **外送單**：外送單照片 → 系統字體為準轉錄（手寫版不採用）→ 以店家起點由近到遠排序 → GitHub（private repo，客戶個資頁面不公開）推 index.html → Cloudflare Pages 自動部署給師傅 ＋ LINE 文字版（條列可搜尋、路線導航連結置頂、導航一律座標版、短連結走 da.gd）【版面鎖定：10/5 index.html 為唯一模板，只換資料；2026-10-08 已走新管線實戰成功 8 筆；舊 Muse Space 版本留作備用】
6. **網站 SEO**：exa-search 長尾關鍵字 → 寫文 → github 推送 → cloudflare（自訂網域／DNS／SSL 上線） → Search Console 數據回流（每週跟他要）
7. **說書／短劇影片**：選書 → exa-search 找資料 → muse-video 策劃 → tts 配音 → media.generate_image 分鏡 → ffmpeg 成片 → 發布【2026-10-01 短劇實測驗證此鏈】

## 織網原則
1. 新 skill 上線先回答：它補哪個缺口？跟誰互補？進哪條迴路？
2. Fallback 寫死，不靠臨場想：A 不行自動換 B
3. 錢、帳號、授權、公開發布四個節點永遠是人工閘門
4. 每日自動檢查斷掉的邊（連接器斷開、帳號未授權就標註暫失效），每季人工複檢（API 改版、服務下線就換線）
5. 每日 04:00 自動優化（cron `skill-net-daily-optimize`）：掃新 skill、修斷邊、按實際使用調整工作流、有變動就同步推 GitHub；無事不打擾
