#!/usr/bin/env python3
"""analyze-system logo: a lifeboat slipway rail seen from the foot of the shingle, looking up.
Two parallel rust red rails run from the bottom corners and meet near the top centre, where the
keel of a lifeboat rests on its carriage, the hull a broad harbor blue curve cut off by the top
edge. Weathered rope tan sleepers cross at shortening intervals, a sail cream winch cable runs
down the centre with its hook resting empty on the lowest sleeper. Below, the name is set in
BBH Hegarty in sail cream on harbor blue, spaced like the boards of a station nameboard."""
import sys
from PIL import Image, ImageDraw, ImageFont
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1000, 780
HARBOR = (39, 80, 110); RUST = (166, 58, 43); TAN = (200, 168, 120); CREAM = (242, 234, 216)
img = Image.new("RGB", (W, H), (206, 196, 172)); d = ImageDraw.Draw(img, "RGBA")
# shingle ground
for y in range(0, 590): d.line([(0, y), (W, y)], fill=(196 - y // 14, 182 - y // 16, 152 - y // 18))
# hull curve cut off by the top edge: v1 draws it far too small so the rails read as a railway
if A == "--v1":
    d.pieslice([-60, -150, 340, 60], 0, 180, fill=HARBOR)
    top_y, spread = 60, 60
else:
    d.pieslice([-260, -330, 1260, 210], 0, 180, fill=HARBOR)
    d.pieslice([-260, -300, 1260, 190], 0, 180, fill=(52, 98, 130))
    d.line([(-200, 96), (1200, 96)], fill=CREAM, width=10)  # sail cream strake along the hull
    top_y, spread = 118, 120
# carriage under the keel
d.rectangle([500 - spread // 2, top_y, 500 + spread // 2, top_y + 26], fill=(52, 48, 44))
# rails from the bottom corners converging near the top centre
for s in (-1, 1):
    xb = 500 + s * 470; xt = 500 + s * (spread // 2 + 8)
    d.line([(xb, 596), (xt, top_y + 20)], fill=RUST, width=22)
    d.line([(xb, 596), (xt, top_y + 20)], fill=(228, 218, 198), width=6)
# sleepers at shortening intervals
for i in range(8):
    t = i / 7; y = 560 - t * 400; half = 430 - t * 330
    d.line([(500 - half, y), (500 + half, y)], fill=(150, 124, 86), width=16)
    d.line([(500 - half, y - 6), (500 + half, y - 6)], fill=(178, 150, 104), width=4)
# winch cable down the centre, hook resting empty on the lowest sleeper
d.line([(500, top_y + 26), (500, 548)], fill=CREAM, width=5)
d.arc([482, 522, 518, 566], 300, 140, fill=(216, 206, 184), width=7)
# nameboard: harbor blue plate, name spaced board by board in BBH Hegarty
d.rectangle([0, 596, W, H], fill=HARBOR)
d.rectangle([0, 596, W, 606], fill=RUST)
name = "analyze-system"
base = __file__.rsplit("/", 1)[0]
if A == "--v2":  # v2 flaw: name set as plain reading text in the text face, unspaced
    f = ImageFont.truetype(base + "/fonts/Barlow.ttf", 62)
    d.text((500, 688), name, font=f, fill=CREAM, anchor="mm")
else:
    f = ImageFont.truetype(base + "/fonts/BBH-Hegarty.ttf", 58)
    # letter by letter with even board spacing
    widths = [d.textlength(ch, font=f) for ch in name]
    gap = 17; total = sum(widths) + gap * (len(name) - 1); x = (W - total) / 2
    for ch, wch in zip(name, widths):
        d.text((x, 660), ch, font=f, fill=CREAM); x += wch + gap
img.save(sys.argv[2] if len(sys.argv) > 2 else "logo.png")
print("logo saved")
