# GitHub 個人首頁維護

## 目的與範圍

為 `david20040406000-hue`（公開顯示名稱 `Zhaxia`）建立獨立 GitHub Profile README。此專案存放動畫名片、頭像素材及其產生程式；首頁 README 僅顯示一張自適應動畫圖片。

GitHub 首頁功能要求公開、與帳號同名的儲存庫，根目錄包含非空白 `README.md`。預定目的為 `david20040406000-hue/david20040406000-hue`。

## 內容依據

- **使用者要求**：參考 Dstnexe 首頁，增加動畫、專業感與科技感。
- **公開資料已確認**：帳號名稱、顯示名稱。
- **使用者後續要求**：作品區改為 Screeps 演算法，移除會考複習。
- **原始碼觀察**：在使用者指定的 Screeps 專案中確認 `task.dispatcher.js` 的優先度與距離評分、`room.planner.js` 的雙向掃描距離變換，以及 `main.js` 的每 tick 快取與 CPU 預算分層。首頁只撰寫概要，不放原始碼、內部參數、基地位置、部署入口或私人儲存庫連結。
- **編輯提案**：「Code. Adapt. Evolve.」與簡介是本次撰寫的品牌文案，不代表已驗證的職稱、年資或專業資格。
- **設計選擇**：石墨色搭配青綠與淡藍、終端機文字、依使用者公開炸蝦頭像生成的簡約平面像素圖示。裝飾線條不表示流量、服務狀態或真實統計。

- **頭像依據**：使用者要求將大 Z 改成其簡筆畫頭像。已目視確認其 GitHub 公開頭像為炸蝦。依後續回饋採用實心方形像素、少量平面色塊與簡單笑臉，降低立體光影。使用內建 imagegen 生成透明 PNG，並以 SVG 嵌入顯示。

- **首頁呈現**：依使用者最新要求，移除名片下方的專案介紹、表格、導覽連結、獨立簡介與 About 區塊，僅保留動畫名片；名片內既有 Screeps 小卡保留。

## 更新方式

1. 修改 `scripts/build_profile.py` 的文案、座標或色票；頭像素材在 `assets/avatar-pixel.png`，嵌入方式在 `scripts/avatar.py`。
2. 執行 `python3 scripts/build_profile.py`，一次產生深／淺色及桌面／手機共四個 SVG。
3. 同步調整 `README.md` 的圖片來源與替代文字；不新增獨立專案介紹區塊。
4. 瀏覽器檢查深色、淺色、390px 寬度、正常動畫與減少動態效果。
5. 更新 `CHANGELOG.md`，審核 staged diff 與檔案大小後提交。

## 架構與限制

- README 使用 `<picture>` 選擇主題與手機圖片；SVG 為自包含資產，內嵌頭像 PNG；無 JavaScript、外部字型、第三方統計 API 或排程。
- 動畫使用 SVG 內的 CSS，約 2.2 秒內顯示全部終端機內容；動畫不支援時仍保留基礎文字。以 `prefers-reduced-motion` 關閉動畫。
- 圖片內文字無法當作一般網頁文字選取，SVG 圖片內卡片不是可點選按鈕。
- 頭像以 base64 PNG 嵌入 SVG；輸出時不需連接外部頭像服務。透明背景，短暫的像素分段顯影（1.1 秒）只播放一次；減少動態模式立即顯示。手機版延續簡化排版，不展示右側大圖。
- 生成方式、完整提示詞與素材來源見 `docs/AVATAR.md`。
- 視覺靈感來自 [Dstnexe 的終端機式個人首頁](https://github.com/Dstnexe/Dstnexe)，版面、圖形與程式另行製作；來源紀錄保留於維護文件。
- 圖片內容不會隨帳戶自動更新；新增作品時需手動修改文案並重建。
- GitHub 決定整站導覽、頭像、側欄與欄位尺寸；本專案僅客製個人首頁 README 區域。
- 瀏覽器動畫、快取及佈景主題策略可能影響外觀；以實際 GitHub 顯示為最終驗證。

## 資料來源

- [GitHub Profile README 官方說明](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [參考設計](https://github.com/Dstnexe/Dstnexe)
- 演算法來源：使用者指定的私人 Screeps 專案（首頁僅展示概要）。
