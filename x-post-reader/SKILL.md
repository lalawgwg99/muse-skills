---
name: "x_post_reader"
description: "Read an X (Twitter) post from a user-supplied x.com status URL and return a Traditional Chinese digest. Trigger when the user sends an X post link and wants it read or summarized."
---

# X Post Reader

## Purpose
Read a single X post the user linked and return a faithful Traditional Chinese digest with engagement stats.

## Workflow
1. Take the exact URL the user supplied. Never guess, rewrite, or shorten it.
2. Try `browser.open` with that URL.
3. If the fetch fails, use `browser.spawn_task` with a self-contained, read-only assignment. The browser task cannot see the conversation, so `task` must include the full URL and these rules verbatim:
   - Open the exact URL in read-only mode.
   - Do NOT log in. Do NOT enter any credentials.
   - If a login wall blocks the post text, STOP and report exactly what is visible. Do not attempt to bypass it.
   - Report: author display name and handle, full post text, post date if visible, visible engagement numbers.
4. The browser task is async: acknowledge briefly, end the turn, and wait for the handoff. Never poll or sleep.
5. Build the digest from the handoff result.

## Output Contract
- 作者（顯示名稱＋帳號）與發布時間
- 貼文全文或忠實的繁體中文摘要（註明原文語言）
- 互動數據：瀏覽／回覆／轉發／喜歡／書籤（頁面有顯示才列）
- 若被登入牆擋住：如實說明看不到，不要編造內容
- 最後一段簡短看法：這篇和使用者手邊專案（慢錢研究所、說書影片、開源 repo 等）的關聯，誠實評估價值，不要硬湊；有關聯才提具體下一步，沒關聯就直說

## Operating Rules
1. Read-only. Never log in, never enter credentials, never bypass a login wall.
2. Never invent post content. If it cannot be read, say so plainly.
3. Reply in Traditional Chinese.
4. Keep tool mechanics out of the reply; one plain line of status ("讀到跟你說") is enough while waiting.
