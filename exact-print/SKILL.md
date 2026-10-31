# exact-print

Requires：python3＋fpdf2（PDF）或 Pillow＋numpy（PNG 橫幅）；中文字體 Noto Sans CJK TC（系統字體目錄的 TTC 需先抽出 TC 單體，見 Procedure）。

來源：2026-10-31 實戰——萬聖節猜題卷（A4、5 頁、每頁 2 題）與 HERAN 店內橫幅（100×30 公分）皆用此流程交付，AI 生圖路線在文字精確度上被證偽後改用程式繪製。

## When to Use
- 交付物必須印在精確尺寸上、文字一個字不能錯時：考卷、店內橫幅、海報、標籤、傳單。
- 尺寸、頁數、題號、價格、型號任一項錯了就會造成實質損失時。
- 不用在：純欣賞用的配圖、封面、社群圖卡（那些走 AI 生圖或 Canva 更快）。

## Procedure
1. 不用 AI 生圖做文字主體：生圖的文字必糊、必錯字、必改品牌字，無法驗收。文字與尺寸精確的列印品一律用程式畫。
2. 選工具：要印成 PDF（考卷、文件）用 fpdf2；要印成大圖（橫幅、海報）用 Pillow。
3. 備字體：Noto Sans CJK TC 在系統是 TTC 合集，先用 fontTools 的 TTCollection 取出 `Noto Sans CJK TC` 單體存成 TTF，fpdf2／Pillow 才能註冊使用。
4. 算尺寸：像素＝公分 ÷ 2.54 × dpi。例：100×30 公分 @200dpi＝7874×2362 像素（已超過 4K，店內橫幅夠用）；A4 用 fpdf2 的 A4 格式，不要自己換算。
5. 品牌橫幅只放品牌字：價格、機型、檔期活動只要使用者沒給，一律不編，留白等使用者補字。
6. 畫完必做三重驗證（見 Verification），驗證通過才交付。

## Pitfalls
- 本環境的 headless 瀏覽器列印走不通：meta-chromium 需 browser-daemon 的 WebGL 政策，直接命令列啟動會被擋。不要在這條路上耗時間，改走程式繪製。
- fpdf2 2.9 沒有公開的 rounded_rect：用內部的 `_draw_rounded_rect`（RenderStyle.D／F／DF）或自繪，不要假裝有公開 API。
- fpdf2 的 `header()`／`footer()` 會被 `add_page()` 自動呼叫：自訂頁首頁尾要改名（例如 draw_header），否則簽名對不上直接報錯。
- TTC 字體不先抽面就註冊會失敗或缺字；抽完要確認檔名與粗細（Regular／Bold）分開。
- PNG 大圖檔案小是正常的：平坦漸層與大色塊壓縮率極高，驗收看像素尺寸，不看檔案大小。

## Verification
- PDF：`pdfinfo` 確認頁數與紙張尺寸（A4＝595.28×841.89 pts）；`pdftotext` 逐題對稿，題號、選項、答案圈一個不能少。
- PNG：`identify` 或 Pillow 確認像素尺寸等於公分×dpi 的換算值。
- 版面：用 `pdftoppm`（PDF）或縮圖（PNG）實際看一遍渲染結果，確認沒有溢出、沒有重疊、沒有留白過大的空卡。
- 三項全過才交付；任一項不過就修程式重畫，不要手動修圖。
