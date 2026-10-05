---
name: "exa-search"
description: "Exa AI 語義搜尋：全網搜尋、新聞搜尋、指定網站搜尋。用於慢錢研究所選題研究、X 話題挖掘、任何需要高品質網頁搜尋的任務。"
---

# Exa Search

## Purpose
用 Exa AI 做語義搜尋，比關鍵字搜尋更懂問題。適用：找新聞事件背景、特定主題的全網資料、指定網站內的內容。

## Tooling
API key 放在 `~/workspace/skills/agent-reach/.env`（`EXA_API_KEY=`，chmod 600，不進 repo）。呼叫時從該檔讀取，不要把 key 寫進任何其他檔案或對話紀錄。

全網搜尋：
```bash
source ~/workspace/skills/agent-reach/.env
curl -s -X POST https://api.exa.ai/search \
  -H "x-api-key: $EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"<問題>","numResults":5,"type":"neural"}'
```

指定網站搜尋（加 `includeDomains`）：
```bash
-d '{"query":"<問題>","numResults":5,"includeDomains":["vocus.cc"]}'
```

取全文（search 回傳的 url 拿去 contents）：
```bash
curl -s -X POST https://api.exa.ai/contents \
  -H "x-api-key: $EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urls":["<url>"],"text":true}'
```

## Auth
Key 是榮德的 Exa 免費版（每月 1000 次額度）。他 2026-10-05 明確說可以直接用、可以記住。用完額度就停手並告訴他。

## Operating Rules
1. 每次搜尋約 $0.005–0.01 美元，省著用：先想好 query，一次要夠，不要來回試。
2. 回傳的 `costDollars` 可留意花費。
3. 搜尋結果的時間敏感性：Exa 的索引有延遲，突發新聞類先用 `browser.search`（news vertical）交叉確認。
4. 繁體中文 query 可直接用，Exa 支援多語言。
