"""以標準函式庫產生個人首頁 SVG；不讀取帳戶、機密或外部服務。"""
from pathlib import Path
from html import escape
from avatar import portrait

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    'dark': dict(bg='#0b1016', panel='#101923', fg='#edf5f4', muted='#9aaebb', line='#273945', accent='#71f6c5', blue='#7ebaff', grid='#1b2d38'),
    'light': dict(bg='#f4f8f7', panel='#ffffff', fg='#122d31', muted='#526b74', line='#ccdcde', accent='#007759', blue='#205da8', grid='#dce9e7'),
}

def build(theme, mobile=False):
    c = PALETTES[theme]
    w, h = (480, 870) if mobile else (960, 650)
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">Zhaxia — Code. Adapt. Evolve.</title>
<desc id="desc">Zhaxia 的個人首頁。自主決策與演算法；作品：Screeps Empire AI；任務調度、空間規劃與 CPU 預算管理。桌面版右側為炸蝦頭像的簡約平面像素圖示，搭配像素顯影動畫。</desc>
<defs>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['blue']}"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="{c['accent']}" stop-opacity=".13"/><stop offset="1" stop-color="{c['accent']}" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{c['grid']}" stroke-width=".6"/></pattern>
  <clipPath id="frame"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20"/></clipPath>
  <clipPath id="typing"><rect class="type-reveal" x="0" y="-22" width="380" height="30"/></clipPath>
</defs>
<style>
  text {{font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; fill:{c['fg']};}}
  .mono {{font-family: 'SF Mono', Menlo, Consolas, monospace; font-size:14px;}}
  .label {{font-family: 'SF Mono', Menlo, Consolas, monospace; font-size:11px; letter-spacing:2px; fill:{c['muted']};}}
  .muted {{fill:{c['muted']};}} .green {{fill:{c['accent']};}} .blue {{fill:{c['blue']};}}
  .reveal {{animation:appear .65s both;}} .row1 {{animation-delay:.55s;}} .row2 {{animation-delay:.8s;}} .row3 {{animation-delay:1.05s;}} .row4 {{animation-delay:1.3s;}} .row5 {{animation-delay:1.55s;}}
  .type-reveal {{animation:typing 1.25s steps(28,end) both;}}
  .pixel-reveal {{animation:pixelBoot 1.1s steps(16,end) both;}}
  .flow {{stroke-dasharray:38 520;animation:flow 7s linear infinite;}}
  .cursor {{animation:blink 1.4s step-end infinite;}}
  @keyframes appear {{from {{opacity:0;transform:translateY(5px);}} to {{opacity:1;transform:translateY(0);}}}}
  @keyframes typing {{from {{width:0;}} to {{width:380px;}}}}
  @keyframes pixelBoot {{from {{height:0;}} to {{height:230px;}}}}
  @keyframes flow {{to {{stroke-dashoffset:-558;}}}}
  @keyframes blink {{0%,60% {{opacity:1;}} 61%,100% {{opacity:0;}}}}
  @media (prefers-reduced-motion: reduce) {{ .reveal,.type-reveal,.pixel-reveal,.flow,.cursor {{animation:none !important;}} }}
</style>
<g clip-path="url(#frame)">
<rect width="{w}" height="{h}" fill="{c['bg']}"/>
<rect width="{w}" height="280" fill="url(#grid)"/>
<ellipse cx="{w-100}" cy="110" rx="330" ry="230" fill="url(#halo)"/>
<path d="M28 1H{w-28}" stroke="url(#accent)" stroke-width="3"/>
''']
    def text(x,y,s,cls='',size=None,extra=''):
        out.append(f'<text x="{x}" y="{y}" class="{cls}" {f"font-size={chr(34)}{size}{chr(34)}" if size else ""} {extra}>{escape(s)}</text>')
    def rect(x,y,rw,rh,rx=12,fill=None,stroke=None):
        out.append(f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" rx="{rx}" fill="{fill or c["panel"]}" stroke="{stroke or c["line"]}"/>')
    def line(x,y,x2,y2):
        out.append(f'<path d="M{x} {y}L{x2} {y2}" stroke="{c["line"]}"/>')

    pad = 28 if mobile else 36
    text(pad,38,'ZX / PERSONAL SPACE', 'label')
    text(w-pad,38,'GITHUB PROFILE', 'label',extra='text-anchor="end"')
    line(pad,56,w-pad,56)
    text(pad,94,'HELLO, WORLD.', 'label green')
    text(pad-3,168 if mobile else 181,'ZHAXIA',size=70 if mobile else 96,extra='font-weight="800" letter-spacing="-5"')
    text(pad,208 if mobile else 224,'Code. Adapt. Evolve.',size=24 if mobile else 29,extra='font-weight="500"')
    text(pad,240 if mobile else 259,'讓程式感知、決策，持續演化。','muted',16)

    if not mobile:
        out.append(portrait(theme,c))

    ty = 282 if mobile else 300
    tw = w-2*pad if mobile else 546
    th = 292
    rect(pad,ty,tw,th)
    for i,color in enumerate(['#fa817c','#e8be68','#65c799']):
        out.append(f'<circle cx="{pad+20+i*16}" cy="{ty+21}" r="4" fill="{color}"/>')
    text(pad+82,ty+25,'zhaxia / profile.json','mono muted',extra='style="font-size:12px"')
    line(pad,ty+42,pad+tw,ty+42)
    out.append(f'<g transform="translate({pad+20} {ty+76})"><text class="mono green">❯</text><g transform="translate(24 0)" clip-path="url(#typing)"><text class="mono">cat ./profile.json</text></g></g>')
    rows = [('{','muted'), ('  "name": "Zhaxia",',''), ('  "focus": "Autonomous agents",',''), ('  "tools": ["JavaScript"],',''), ('  "approach": "Build. Refine. Repeat."',''), ('}','muted')]
    # 窄螢幕避免長字串縮小成不可讀的字。
    if mobile:
        rows[4] = ('  "approach": "Build & refine"','')
    for i,(s,cls) in enumerate(rows):
        out.append(f'<g class="reveal row{min(i+1,5)}">')
        text(pad+20,ty+111+i*23,s,'mono '+cls,extra='xml:space="preserve"')
        out.append('</g>')
    text(pad+20,ty+270,'❯','mono green')
    out.append(f'<rect class="cursor" x="{pad+43}" y="{ty+258}" width="8" height="15" rx="1" fill="{c["accent"]}"/>')

    px,py,pw = (pad,ty+308,tw) if mobile else (602,ty,322)
    rect(px,py,pw,174)
    text(px+20,py+28,'01 / SCREEPS ALGORITHMS','label')
    text(px+20,py+66,'Screeps Empire AI',size=22,extra='font-weight="650"')
    text(px+20,py+94,'任務調度 · 空間規劃 · CPU 預算','muted',16)
    line(px+20,py+114,px+pw-20,py+114)
    text(px+20,py+144,'JAVASCRIPT · PRIVATE SOURCE','mono green',extra='style="font-size:12px"')


    if not mobile:
        rect(px,py+190,pw,102)
        text(px+20,py+218,'AGENT LOOP','label')
        text(px+20,py+249,'SENSE','mono',extra='style="font-size:12px"')
        text(px+130,py+249,'PLAN','mono green',extra='style="font-size:12px"')
        text(px+236,py+249,'ACT','mono',extra='style="font-size:12px"')
        line(px+60,py+245,px+115,py+245)
        line(px+176,py+245,px+222,py+245)
        out.append(f'<path class="flow" d="M{px+20} {py+274}H{px+pw-20}" stroke="url(#accent)" stroke-width="2"/>')

    fy = 806 if mobile else 622
    line(pad,fy-19,w-pad,fy-19)
    text(pad,fy+6,'CRAFTED WITH CURIOSITY.', 'label')
    text(w-pad,fy+6,'ZX / 01','label green',extra='text-anchor="end"')
    if mobile:
        out.append(f'<path class="flow" d="M{pad} 844H{w-pad}" stroke="url(#accent)" stroke-width="2"/>')
    out.append(f'</g><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20" fill="none" stroke="{c["line"]}"/></svg>')
    return '\n'.join(out)+'\n'

if __name__ == '__main__':
    for theme in PALETTES:
        for mobile in (False, True):
            target = ROOT/'assets'/f'profile-{theme}{"-mobile" if mobile else ""}.svg'
            target.write_text(build(theme,mobile),encoding='utf-8')
            print(f'{target.name}: {target.stat().st_size:,} bytes')
