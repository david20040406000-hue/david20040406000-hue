# 像素頭像素材紀錄

- **使用者要求**：以其簡筆畫頭像取代右側大 Z，改用像素風格組成；降低立體感，採簡約風格。
- **來源參考**：帳號 `david20040406000-hue` 的公開 GitHub 頭像，已目視確認為簡筆畫炸蝦。
- **生成方式**：內建 `image_gen` 工具；以原始頭像作為角色參考。
- **正式素材**：`assets/avatar-pixel.png`，透明 PNG，560 × 437；裁去透明留白，以 nearest-neighbor 縮放及 PNG 調色盤編碼。
- **使用位置**：`scripts/avatar.py` 讀取 PNG 並以 data URI 嵌入深／淺色 SVG，無遠端圖片請求。
- **動畫**：1.1 秒分段顯影；減少動態效果時立即顯示完整頭像。
- **限制**：生成結果為像素風格的近似詮釋；日後換頭像需另行更新素材。正式輸出不含原始參考圖片。

## 最終生成提示詞

```text
Use case: style-transfer. Create a VERY SIMPLE FLAT PIXEL ART avatar of the exact smiling shrimp in the reference. This is for a small GitHub header icon, not an elaborate game sprite. Keep its curved plump shrimp body, tail pointing upward at the left, right-side two dot eyes and tiny smiling mouth. Entire image assembled from crisp square pixel clusters with stair-step edges, as if designed at 40x40 or 48x48 and nearest-neighbor enlarged. ONLY 4 or 5 flat solid colors: warm golden yellow body, a small muted amber color along the bottom edge if necessary, flat coral orange tail, thin dark desaturated teal outline and facial features. Match the SIMPLICITY of the reference drawing, translating the outline and face into square pixels. Uniform flat color for almost all of the body. Minimal narrow single-pixel outline. NO 3D volume, NO highlights, NO shiny surfaces, NO cyan rim lighting, NO thick navy shadows, NO complex gradients, NO texture, NO scattered individual dots, NO grid, NO dither noise. Pixelated silhouette but clean large flat color regions. Genuinely TRANSPARENT alpha background outside the shrimp. One isolated icon filling 85 percent of the frame, with slight consistent padding. No text, no other objects, no floor, no external cast shadow, no border or panel. The result should feel like a charming simple retro computer icon, quiet and minimal.
```
