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
- reverse-engineer-anything：逆向工程（產物分析）——只有產物、沒有源碼時用：編譯後 bundle、Worker、APK、韌體、ASAR 的功能解釋／版本比對／反編譯【2026-10-21 使用者親自選定方案 A 裝入（`~/workspace/custom-skills/`）：只取 skill 指令 7 檔（SKILL.md＋references 6 份），未跑 setup、未註冊 MCP；VM 目前無 Ghidra/JDK，原生與 Android 深度分析需另備工具鏈。暫不綁固定迴路，QA／維護時按需呼叫（產物行為與源碼對不上、外部二進制檢驗）】

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
- user_journey_dogfood：上線前以使用者身份走查產品（`~/workspace/custom-skills/`，2026-10-22 實戰長出）：定一人一具體目標、從首頁走公開路徑到目標不跳步、逐頁對齊每個數字與標籤、按嚴重度（信任破壞／流程阻斷／外觀）修、複走同一旅程乾淨才放行。實證：CarePilot 上線前走查抓出 13 項（同 CMS 等級三頁補助數字打架、五年報表未接購物車、測試字串外洩、零元誤讀為應付額等），當晚全修；複走又抓 1 項（購物車頁頂大數字誤讀為應付總額）再修。同期 tsc／build／jest 全綠，一項都沒抓到——綠燈測試只驗程式路徑，不驗跨頁事實一致
- openrouter：免費 AI 模型池（:free only，絕不動帳戶餘額；每日 1000 次免費額度）。機械性批量工作（初篩、翻譯、摘要、分類）的便宜算力；主力模型每天約 06:24 由 `openrouter-free-model-scan` 排程掃描更新 `state/free-model.json`（動態路由，不寫死模型 ID）；憑證走 Secure Vault（custom.openrouter），不存原始 key【2026-10-09 新建 skill；使用者立鐵律：只能用免費模型】【2026-10-10 實戰：nemotron 請求掛住逾時、gemma 上游 429 → 每日獵捕初篩改由主模型做，免費池不可用不硬等】【2026-10-11 品質分流：free-model.json 新增 `quality_model`＝nvidia/nemotron-3-ultra-550b-a55b:free——批量機械活走 Lightning 日常主力，要品質時走 quality_model；每日掃描重寫名單時保留既有 quality_model／quality_note 不洗掉（10-12 實測原樣保留）】【2026-10-15：gemma 兩款連續第 7 天上游 429；or_api.py 寫死憑證路徑（templates/skill/bin）已修為現行 bin，不靠 PYTHONPATH 繞道也可跑】【2026-10-16：gemma 兩款連續第 8 天上游 429】【2026-10-19：gemma 兩款多日上游 429，不再重 ping（沿用「不可用」結論）；同日掃描主力仍為 nemotron lightning，ping 回 Pong! 約 2.5 分鐘（較 10-18 的 48 秒變慢）】【2026-10-20：10-20 03:00 每日獵捕初篩——免費模型連續第 3 天逾時，改由主模型自行初篩；「免費池不可用不硬等」fallback 再次實證】【2026-10-21：nemotron lightning 連續三天逾時後恢復——42 秒完成 5 候選初判，每日獵捕第一層初篩重回免費模型（第二、三層仍親自判定）；「不可用不硬等、可用就用上」雙向實證】【2026-10-22：lightning 持續可用——ping 2.5 秒、45 秒完成 29 候選初判，免費池第一層初篩穩定接回】【2026-10-23 06:24 掃描：20 個全免費模型，主力 `nvidia/nemotron-3.5-lightning:free` 續任（ping 一次通關、約 2 秒回 pong!）；gemma-4 兩款上游 429（10-19 起連續第 5 天）；minimax-m3.1-flash:free 轉付費掉出名單；免費池健康】【2026-10-24 06:24 掃描：仍 20 個免費模型、lightning 主力續任（2.3 秒回 pong!）；gemma-4 兩款 429 連續第 6 天；新增 xingchen-4.0、nemotron-3-nano-omni-reasoning 等免費模型；quality_model 原樣保留】【2026-10-25 06:24 掃描：仍 20 個免費模型、與前日完全相同無新增；lightning 主力續任（3.3 秒回 pong!）；gemma-4 仍上游 429（連第 7 天）；quality_model 原樣保留】
- goals：目標追蹤
- subscription-status：額度查詢
- muse-feedback：問題回報

### 觀察中（未安裝，不列邊）
- agent-reach：給 AI Agent 接網路能力的開源專案；評估中（目錄內尚無 SKILL.md，未 pip install、未完成可用性驗證，不可記成已安裝）。2026-10-07 使用者同意將 AI 工具獵人計畫封存（03:00 每日獵捕排程保留作火種，命中絕不自動安裝）；agent-reach 是否正式納入仍待確認
- claw-browser-anchor（候選，未安裝）：DOM 錨點瀏覽器自動化方法論；可參考作為 browser.spawn_task 租用 VM 失敗時的備援思路（該缺口 2026-10-03 實測至今無備援，2026-10-09 複查仍無備援）。2026-10-08 深入研究完成，結論＝不建議安裝整包，只吸收方法論：super-research 輕量版驗證紀律已寫入慢錢研究所流程（見迴路#1），DOM 錨點優先／動作後驗證／漂移恢復可作瀏覽器任務規範；安裝本身無額外價值。絕不自動安裝
- hedit（候選，未安裝）：pycodebr/heditor——創意豎屏影片剪輯 skill（ffmpeg＋HyperFrames、命名風格、逐字字幕）；2026-10-20 每日獵捕命中、安全初檢通過。補缺口：爆紅影片工廠迴路#2／說書影片迴路#7「策劃→配音→成片」中的剪輯環節（現靠外部工具）；待使用者點頭才裝，絕不自動安裝
- douyin-download-skill（候選，未安裝）：Arekejoker/douyin-download-skill——agent 用抖音無水印下載 skill（含 BGM＋元數據）；2026-10-20 每日獵捕命中、安全初檢通過。注意：裝前需在 VM 掛已登入抖音的 Chrome（掃碼一次）；現 tiktokio.bio 仍可用（影片下載三神器），不急裝。待使用者點頭才裝，絕不自動安裝
- 2026-10-21 03:00 每日獵捕（排程 10-19 曾自 cron 清單消失、已按 _archive 完整定義重建，10-20／10-21 連兩次正常執行）：本輪無命中，23 個新候選皆不符三層規則；10-20 兩款命中候選（heditor／douyin-download-skill）仍待使用者點頭，未安裝。掃描來源 10-20 新增 awesome-short-drama-skills 目錄（微短劇 skill 精選；本輪新增 3 項皆為微短劇全流程平台，與現有專案線不相關，不織入）
- qz-browser-agent（候選，未安裝）：alibaba 開源 local-first 瀏覽器 agent（Chrome 擴充套件、一句話任務描述在真實 Chrome 跑流程擷取資料、BYOK 模型，CLI／MCP 可被 agent 呼叫、任務可存成 skill）；2026-10-22 每日獵捕命中、安全初檢通過（91★、Apache-2.0、Chrome Web Store 上架、有 CI；19 權限完整揭露、service-worker 無外傳 URL、無混淆）。補缺口：瀏覽器自動化（方格子發文、review-helper 偵測的瀏覽器操作可存成 skill 重用；現 browser.spawn_task 租用 VM 失敗時無備援）。注意：權限廣（<all_urls>、debugger）、需自備模型 key；待使用者點頭才裝，絕不自動安裝
- founder-skill（候選，未安裝）：Jakeschincariol/founder-skill——商業點子驗證 11 skills（董事會／CFO 單位經濟學／100 人消費者面板／競品偵察／van Westendorp 定價法；1401★、MIT、程式碼初檢通過）；2026-10-23 每日獵捕命中。補缺口：新創意評估流程（小眾創意評估＋變現定價參考）。待使用者點頭才裝，絕不自動安裝
- motion-video-kit（候選，未安裝）：echris6/motion-video-kit——AI 商業短片 skill kit（AI 素材＋GSAP/Three.js 動畫＋獨立評審 Gauntlet 循環；1171★、MIT、安全初檢通過）；2026-10-24 每日獵捕命中。補缺口：迴路#2 爆紅影片工廠／迴路#7 說書影片的成片環節升級。待使用者點頭才裝，絕不自動安裝
- marketingskills（候選，未安裝）：coreyhaines31/marketingskills——給 AI agent 的行銷 skills 合集（SEO 稽核／programmatic SEO／schema／定價／offers 等 49 個 skills）；2026-10-26 每日獵捕命中、安全初檢通過。補缺口：迴路#6 SEO 內容＋變現（TaiCalc／字研所流量經營與定價參考）。注意：原為 Claude Code 設計（方法論可直接用；CLI 工具需自備各家 API key）。待使用者點頭才裝，絕不自動安裝
- last30days-skill（候選，未安裝）：mvanhorn/last30days-skill——跨 Reddit／X／YouTube／HN／Polymarket 等近 30 天話題搜尋引擎（按讚數／真金白銀評分綜合成有根據摘要）；2026-10-26 每日獵捕命中、安全初檢通過。補缺口：迴路#1 慢錢選題＋迴路#3 X 話題挖掘（Exa 的 X 盲區由多平台訊號補；找到話題後全文仍走 x-post-reader）。注意：部分 lane 需自備 key 或自有瀏覽器 session。待使用者點頭才裝，絕不自動安裝
- narwhal（候選，未安裝）：aindong/narwhal——local-first SEO＋AI 搜尋可見度（GEO／LLMO）掃描 skill（零依賴）；2026-10-26 每日獵捕命中、安全初檢通過。補缺口：迴路#6 定期體檢（TaiCalc／字研所 SEO＋FAQ schema／長尾成效驗證；GSC 斷線期間的公開數據體檢替代）。注意：GSC 串接需使用者本人在手機上過驗證（GSC 登入自 10/14 起失效，現況不變）。待使用者點頭才裝，絕不自動安裝
- deep-research-plus-skills（候選，未安裝）：Asaceoo/deep-research-plus-skills——帶證據閘門的深度調研編排層（大綱→深調→反方評審→報告；無證據結論進不了 TL;DR、單源標示、補搜逾 2 輪判失敗）；2026-10-26 每日獵捕命中、安全初檢通過。補缺口：迴路#1 慢錢驗證流程（把「關鍵主張開來源頁確認、兩獨立來源交叉驗證」人工紀律變成可執行閘門）。注意：新而小（1★），方法論價值大於名氣。待使用者點頭才裝，絕不自動安裝
- OpenMontage（候選，未安裝）：calesthio/OpenMontage——開源 agentic 影片工作室（12 條產線、100+ 工具、140 個 skill 檔）；2026-10-26 每日獵捕命中、安全初檢通過。補缺口：迴路#2／#7 影片產線升級（說書影片、AI 廣告片全流程工作室化）。注意：重裝備（162MB、AGPL-3.0、需多家付費 provider key，免費額度有限）、與 10-24 motion-video-kit 高度重疊（後者輕量、前者完整工作室），二選一或都不裝。待使用者點頭才裝，絕不自動安裝
- 2026-10-26 觀察中待決定累計：qz-browser-agent、founder-skill、motion-video-kit、heditor、douyin-download-skill（前 5 件）＋ marketingskills、last30days-skill、narwhal、deep-research-plus-skills、OpenMontage（10-26 新 5 件），共 10 件待使用者點頭；5 件新命中已在主聊天室交付、皆未安裝；安裝決策由獵捕排程向使用者報告，本織網只列候選、絕不自動安裝【2026-10-25 03:00 獵捕 0 命中，5 件仍待點頭不變；2026-10-26 03:00 獵捕掃 142 候選、深查 7 個、命中 5 個，另 2 個深查排除（clearframe 黑客松單日專案需特定硬體、x-agent-skill 薄 wrapper 品質不過，皆非惡意）】
- 退役空殼（不列邊、不算已安裝）：`~/workspace/custom-skills/` 下的 local-agent-reach 與 recovered-skill-notes，2026-10-21 經審查退役——兩份 SKILL.md 皆只有「保存舊學習、未經驗證」的樣板文字，無實質方法可併入任何現有 skill，僅留檔不進主動檢索；日後掃描見到它們不再重複列為新 skill。與本節 agent-reach（`~/workspace/skills/` 下無 SKILL.md 的評估中專案）是兩回事，勿混淆

---

## 邊 — 互補與 fallback（網的密度在這裡）

**研究互補**
- exa-search ↔ browser.search：Exa 語義深、browser 即時快。突發新聞先 browser（news vertical），背景深挖再用 Exa；browser.search 若回 401/session_invalid 就降級走題庫觀念文、不硬等新聞【2026-10-03 實測】
- exa-search ↔ x-post-reader：X 是 Exa 的盲區（2026-10-05 實測 x.com 限定搜尋回 0 筆），X 內容一律走 x-post-reader；x-post-reader 內部 fallback＝browser.open → 唯讀 live browser（不登入、不繞牆）【2026-10-01 實測鏈，多篇 X 貼文已實戰成功讀取】
- social.search → x-post-reader：先找到爆文（social），再讀全文細節（x-post-reader）
- image-search ↔ media-library：先翻自己的照片庫，沒有才去外網找
- wide-research ↔ exa-search：要快用 Exa，要深用 wide-research；可先 Exa 掃、再 wide-research 深挖
- places-search ↔ browser.search：店家資訊先 places，營業時間／評價異常時 browser 交叉
- reverse-engineer-anything ↔ github：repo 有完整源碼走 github／一般 repo 工具分析，不跑 REA；只有產物（編譯 bundle、Worker、APK、韌體、ASAR）才走 REA。REA 工具不在當前 session（未跑 setup）時先手動分析、不硬裝

**生產互補**
- muse-video → tts：策劃完直接配音，說書產線固定這條
- media → image-search：生成前先找參考圖，避免風格跑偏；media.generate_image 憑證失敗時改 PIL 自繪封面【2026-10-03 實測】
- media-library → media：有參考照時當輸入（男友 POV 續集、柴犬角色一致性）
- tts → podcast：單段配音 vs 完整節目，看長度選

**發布互補**
- threads ↔ instagram ↔ facebook-cli：同一內容改寫多發，看平台調性【2026-10-06 註、10-13 複查仍未連結（慢錢研究所 Threads／X 帳號待手機驗證建立，短貼文僅備稿未發；待 Meta 授權），改發環節由 instagram／facebook-cli 覆蓋】【10-15：三路偵察仍未取得 Threads／X 即時原生貼文數據，結論為二手概括】
- social-content-performance → social.search：看數據 → 回頭找下一波爆款（迴路）
- meta-ads：自然流量起不來時才考慮，不主動推

**資料互補**
- google-sheets ↔ artifacts：外送資料已遷至 GitHub（private repo 存檔）＋ Cloudflare Pages 網頁給師傅；試算表／GAS 查詢方案 10-04 已棄。google-sheets 連接器自 10-02 由使用者手動斷開、10-10 複查仍斷，不主動重連
- github → （Cloudflare Pages）：推送即部署，TaiCalc／字研所／shift-fill／外送頁 固定這條【2026-10-08 實戰：外送頁 private repo 推送後 Pages 自動部署成功】【2026-10-20：care-calculator 推送 f4bfb82 成功（tsc 0 error、build 靜態匯出、jest 114 全綠），Pages 自動部署，邊健康】【2026-10-21：care-calculator 推送 e6b6e24（tsc／build／jest 114 全綠）→ 遠端 4670e76，Pages 自動部署；P1 住宿式機構補助少算兩類對象同日修好上線，邊健康】【2026-10-22：care-calculator 推送 dd7eb87（tsc 0 error、build 成功、jest 114/114、4 頁靜態匯出皆帶 FAQPage JSON-LD）→ Pages 自動部署，邊健康】【2026-10-24：care-calculator 推送 c9843ff（40 頁差異化里程碑達成：tsc 0 error、build 成功、3 頁 FAQPage JSON-LD 靜態驗證）→ Pages 自動部署，邊健康】【2026-10-25：care-calculator 推送 f86464c（失智頁死鏈修復＋第 15 篇 blog，tsc／build 通過）→ Pages 自動部署，邊健康】【2026-10-26：care-calculator 推送 dad82a4（第 16 篇 blog 外籍看護 30% 規則、tsc 0 error、build 成功、sitemap 97→98、新頁含 FAQ JSON-LD）→ Pages 自動部署，邊健康】
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

**品管互補（user_journey_dogfood）**
- user_journey_dogfood ↔ github：上線前走查是推送前的閘門——走查乾淨才推，推完再驗正式站；綠燈測試（tsc／build／jest）通過不代表可放行，跨頁數字一致只能靠走查驗
- user_journey_dogfood → browser.browse：走查用 live browser 走使用者真實路徑（不用管理後台、不預填狀態）；工具不支援手機 viewport 時，手機版最終驗證只能靠真機截圖，不以桌面寬度冒充
- user_journey_dogfood ↔ reverse-engineer-anything：一個驗「自家產品給使用者看的事實是否一致」，一個驗「別人產物的行為與宣稱是否一致」；上線前後兩種 QA 按需呼叫，不互相取代

**跨層 fallback**
- 任何「要查 X」→ x-post-reader（不要用 exa-search 硬碰）
- 任何「要即時」→ browser.search 對應 vertical（不要等 Exa 索引）
- 任何「要他照片」→ media-library 優先
- 付費／下單／授權節點 → 一律停在使用者面前（錢、帳號、授權不自動過）
- browser.spawn_task 若回 browser_vm_lease_unavailable → 無備援，任務延期；迴路設計須容忍單日缺發【2026-10-03 實測，缺口待補】

---

## 迴路 — 高頻工作流（端到端，含回流）

1. **慢錢研究所每日**：exa-search／browser.search 選題（每日 07:00 選題補給排程）→ 寫作 → image-search 封面 → vocus 發布 → social-content-performance 看數據 → 回流選題【2026-10-08 吸收 genspark-claw super-research 輕量版驗證紀律：選題與品質紅線現含「關鍵主張開來源頁確認、關鍵數字兩獨立來源交叉驗證、衝突並陳、不確定標「目前已知」、驗證不過刪掉不寫」；整包未安裝、只取方法論】【2026-10-09：方格子恢復全自動（A 帳號登入狀態正常）】【2026-10-14 更正：編輯器實為 Lexical 非 ProseMirror；fill 回傳 unknown 但實際延遲 1–2 分鐘才生效，驗證為空後補 type＝全文重複兩次（當日連毀 2 稿）。防呆＝只做 1 次 fill 後等待至少 2–3 分鐘再驗證，絕不在驗證為空後補輸入；驗證通過（開頭第一句＋結尾延伸閱讀＋無重複段落）才繼續封面＋發佈；連續 2 次草稿損壞即停手】【2026-10-15 新失敗模式：同樣單次 fill＋等 2–3 分鐘＋重載，內文仍 0 字完全未寫入（兩份全新草稿皆如此）——與 10/14「延遲後重複」不同，兩天兩種模式；重試前要換輸入打法，不要照舊再填】【2026-10-16 備援實證：fill 失效時換「第一份全新草稿＋單次 type 全文」一次成功（7,043 字、無重複、無截斷），仍嚴禁分段輸入；fill 失效≠編輯器完全失效，先換 type 再放棄】【2026-10-17：單次 type 再次成功（5,019 字），type 備援二度驗證；同日再增 2 份空草稿待手動刪除（累計 6 份）】【2026-10-19：10-18／10-19 文章發佈成功（老福法三讀時事文 8,083 字），但封面圖上傳兩次失敗（vocus 上傳對話框未暴露檔案輸入欄位 target_blocked）→「不使用縮圖」公開，迴路封面環節當日斷；壞草稿累計 7 份（10-19 更正，原記 6 份少算 1 份）待手動刪除；10-17 費半文（5,019 字）仍未發佈、時事鉤子已過】【2026-10-21：發文排程正常（《道瓊 +1%、費半 -0.3%》5,013 字發佈成功）；使用者拍板照救援計畫拚滿 90 天（2026-10-10 起算、約 2027-01-08 驗收，標準＝追蹤 100＋單篇平均 100，未達標不硬開付費）】【2026-10-23：vocus-daily-article 發佈成功（5,264 字單次貼上完整、封面一次上傳成功）；另有一篇待發文章卡在「等使用者確認用哪個帳號登入」，其後的 queue.md／published.log 連帶 blocked、未計為已發佈】【2026-10-24：發佈成功（5,990 字一次貼上無損壞、封面一次通過），迴路發佈環節健康】【2026-10-25：發佈成功（韓國熔斷文 7,305 字、封面一次上傳成功；發佈曾卡在封面上傳授權卡、核准一次後完成，未另開草稿重發），迴路發佈環節健康】
2. **爆紅影片工廠**：social.search 找爆款 → muse-video 策劃 → tts 配音 → 發布 → 數據回流
3. **X 經營**：social.search/x-post-reader 找話題 → exa-search 補背景 → 寫文 → 發布
4. **柴犬圖卡**：文案 → image-search 找參考 → media 生成 → threads 發布 → 數據回流
5. **外送單**：外送單照片 → 系統字體為準轉錄（手寫版不採用）→ 以店家起點由近到遠排序 → GitHub（private repo，客戶個資頁面不公開）推 index.html → Cloudflare Pages 自動部署給師傅 ＋ LINE 文字版（條列可搜尋、路線導航連結置頂、導航一律座標版、短連結走 da.gd）【版面鎖定：10/5 index.html 為唯一模板，只換資料；2026-10-08 已走新管線實戰成功 8 筆；舊 Muse Space 版本留作備用】
6. **網站 SEO**：exa-search 長尾關鍵字 → 寫文 → github 推送 → cloudflare（自訂網域／DNS／SSL 上線） → Search Console 數據回流（每週跟使用者要）【2026-10-23：GSC 登入連續第 9 天失效（10/15～10/23；當日被導向介紹頁、工作階段已無登入憑證），數據沿用 10-10 快照；需站長本人在手機瀏覽器重新登入才能恢復；10-20 起儲存帳號遇 Google 帳戶救援本人驗證、代理人無法代過，不要再拿儲存密碼反覆嘗試（會觸發帳戶救援）；SEO 診斷以公開數據為準】【2026-10-24：GSC 登入連續第 10 天失效（10/15～10/24），仍沿用 10-10 快照】【2026-10-25：GSC 登入連續第 11 天失效（10/15～10/25、再被導向介紹頁、無登入憑證、未輸入密碼），仍沿用 10-10 快照（資料截止距今 19 天）】
7. **說書／短劇影片**：選書 → exa-search 找資料 → muse-video 策劃 → tts 配音 → media.generate_image 分鏡 → ffmpeg 成片 → 發布【2026-10-01 短劇實測驗證此鏈】
8. **上線前走查（user_journey_dogfood）**：定 persona＋具體目標 → browser.browse 走公開路徑 → 逐頁對數字／標籤／字串 → 按嚴重度修 → 複走同一旅程乾淨才放行 → github 推送 → cloudflare 部署後再驗正式站。適用所有對外上線（網站工具、改版、參數後台異動後皆應重走）；同一批上線的多個工具共用同一類跨頁數字風險時，一處抓到的口徑問題要順查同批其他頁【2026-10-22 CarePilot 實證：首走 13 項＋複走 1 項全修上線】

## 織網原則
1. 新 skill 上線先回答：它補哪個缺口？跟誰互補？進哪條迴路？
2. Fallback 寫死，不靠臨場想：A 不行自動換 B
3. 錢、帳號、授權、公開發布四個節點永遠是人工閘門
4. 每日自動檢查斷掉的邊（連接器斷開、帳號未授權就標註暫失效），每季人工複檢（API 改版、服務下線就換線）
5. 每日 04:00 自動優化（cron `skill-net-daily-optimize`）：掃新 skill、修斷邊、按實際使用調整工作流、有變動就同步推 GitHub；無事不打擾
