"""生成數學興趣圓環；百分比只作視覺配置，不代表能力評分。"""
import json
import math
import random
from html import escape
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'assets' / 'interests.json'


def load_subjects(shuffle=False):
    subjects = json.loads(DATA.read_text(encoding='utf-8'))
    assert 1 <= len(subjects) <= 6, '科目數量限 1 至 6'
    if shuffle:
        rng = random.SystemRandom()
        while True:
            weights = [rng.uniform(1, 3) for _ in subjects]
            raw = [weight / sum(weights) * 100 for weight in weights]
            values = [math.floor(value) for value in raw]
            order = sorted(range(len(raw)), key=lambda i: raw[i] - values[i], reverse=True)
            for i in order[:100-sum(values)]:
                values[i] += 1
            if len(set(values)) == len(values):
                break
        for subject, value in zip(subjects, values):
            subject['percent'] = value
        DATA.write_text(json.dumps(subjects, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    assert sum(s['percent'] for s in subjects) == 100
    assert all(isinstance(s['percent'], int) and 0 < s['percent'] <= 100 for s in subjects)
    return subjects


def subject_ring(theme, colors, subjects, mobile=False):
    palette = [colors['accent'], colors['blue']] + (
        ['#c6a5ff', '#dc9872', '#d3b967', '#c1799d'] if theme == 'dark'
        else ['#8550bb', '#a75528', '#826500', '#a44272']
    )
    tx, ty, cx, cy = (28, 268, 94, 84) if mobile else (602, 65, 161, 83)
    circumference = 2 * math.pi * 65
    out = [f'<g transform="translate({tx} {ty})" aria-label="數學興趣圓環">',
           f'<circle cx="{cx}" cy="{cy}" r="65" fill="none" stroke="{colors["line"]}" stroke-width="10"/>',
           f'<circle cx="{cx}" cy="{cy}" r="49" fill="none" stroke="{colors["line"]}" stroke-width=".7"/>',
           f'''<defs><mask id="interestSweep" maskUnits="userSpaceOnUse" x="{cx-73}" y="{cy-73}" width="146" height="146">
<circle class="interest-sweep" cx="{cx}" cy="{cy}" r="65" fill="none" stroke="white" stroke-width="12" stroke-linecap="round"
stroke-dasharray="{circumference:.3f} {circumference:.3f}" stroke-dashoffset="0" transform="rotate(-90 {cx} {cy})"
style="--circ:{circumference:.3f}"/>
</mask></defs><g mask="url(#interestSweep)">''']
    start = 0
    for i, subject in enumerate(subjects):
        percent = subject['percent']
        # 色帶本身不做動畫；共用單一遮罩連續揭露整圈。
        # 微量重疊避免反鋸齒造成色帶交界的細縫。
        length = percent * circumference / 100 + 0.12
        out.append(f'''<circle class="interest-arc" cx="{cx}" cy="{cy}" r="65"
fill="none" stroke="{palette[i]}" stroke-width="10" stroke-linecap="butt"
stroke-dasharray="{length:.3f} {max(0,circumference-length):.3f}" transform="rotate({-90+start*3.6} {cx} {cy})"/>''')
        start += percent
    out.append('</g>')
    out.append(f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-size="23" font-weight="650" letter-spacing="2">MATH</text>')
    out.append(f'<text x="{cx}" y="{cy+21}" text-anchor="middle" class="label" style="font-size:8px;letter-spacing:2px">INTERESTS</text>')
    for i, subject in enumerate(subjects):
        x = 202 if mobile else 12 + (i % 2) * 166
        y = (22+i*27) if mobile else (174+(i//2)*20)
        end_x = 396 if mobile else x+140
        out.append('<g class="interest-label">')
        out.append(f'<circle cx="{x}" cy="{y-4}" r="3" fill="{palette[i]}"/>')
        out.append(f'<text x="{x+12}" y="{y}" font-size="{14 if mobile else 12}">{escape(subject["name"])}</text>')
        out.append(f'<text x="{end_x}" y="{y}" class="mono" text-anchor="end" style="font-size:{14 if mobile else 12}px;fill:{palette[i]}">{subject["percent"]}%</text></g>')
    out.append('</g>')
    return '\n'.join(out)
