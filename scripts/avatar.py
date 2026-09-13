"""將已生成的透明像素頭像嵌入 SVG，避免外部圖片依賴。"""
import base64
from pathlib import Path


def portrait(theme, colors):
    image_path = Path(__file__).resolve().parents[1] / 'assets' / 'avatar-pixel.png'
    encoded = base64.b64encode(image_path.read_bytes()).decode('ascii')
    return f'''<g transform="translate(638 58)" aria-label="炸蝦頭像的簡約平面像素圖示：橘黃身體、橘紅尾巴、方形眼睛與笑臉">
<defs><clipPath id="pixelBoot"><rect class="pixel-reveal" width="288" height="230"/></clipPath></defs>
<g clip-path="url(#pixelBoot)"><image x="10" y="0" width="268" height="210" preserveAspectRatio="xMidYMid meet" style="image-rendering:pixelated" href="data:image/png;base64,{encoded}"/></g>
<text x="144" y="228" text-anchor="middle" class="label" style="font-size:9px;letter-spacing:2.4px">ZHAXIA / PIXEL AVATAR</text>
</g>'''
