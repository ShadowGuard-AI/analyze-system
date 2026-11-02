#!/usr/bin/env python3
"""analyze-system banner: the boathouse at the top of a shingle bank in the hour before a launch
that may not be needed. Big doors open on a slipway dropping in a straight iron run to the surf
line, rails bright where keels polished them. The lifeboat sits on its carriage in shadow inside,
bow toward the sea. A rocket flare post stands left beside a coiled rope and oil lanterns; a tide
table board hangs right under the eaves with its chalk wiped clean. Gulls hold over the shingle.
The name is painted in BBH Hegarty in sail cream across the harbor blue lintel board above the
doors, one board only, salt dulled at the letter edges, and no other readable mark anywhere."""
import random, sys
from PIL import Image, ImageDraw, ImageFont
random.seed(97)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1600, 680
HARBOR = (39, 80, 110); RUST = (166, 58, 43); TAN = (200, 168, 120); CREAM = (242, 234, 216); SEA = (110, 131, 120)
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 260):
    t = y / 260; d.line([(0, y), (W, y)], fill=(int(240 - 54 * t), int(232 - 48 * t), int(214 - 4 * t)))
# sea across the lower right and behind the slipway foot
d.polygon([(0, 470), (1600, 440), (1600, 680), (0, 680)], fill=SEA)
for i in range(10):
    y = 486 + i * 19; x0 = (i * 173) % 700
    d.line([(x0, y), (x0 + 420, y - 5)], fill=(240, 242, 234, 210), width=5)
# shingle bank in the foreground left and centre
d.polygon([(0, 380), (980, 430), (820, 680), (0, 680)], fill=(172, 154, 120))
for _ in range(1500):
    x, y = random.uniform(0, 980), random.uniform(390, 680)
    if y > 430 + (980 - x) * .28: continue
    r = random.uniform(3, 8); d.ellipse([x - r, y - r * .6, x + r, y + r * .6], fill=random.choice([(150, 138, 116), (130, 130, 126), (188, 170, 134)]))
# boathouse on the bank, upper left of centre
bx, by, bw, bh = 190, 96, 620, 330
d.rectangle([bx, by, bx + bw, by + bh], fill=(218, 209, 188))
d.polygon([(bx - 30, by), (bx + bw + 30, by), (bx + bw - 70, by - 66), (bx + 70, by - 66)], fill=(84, 72, 60))
# lintel board with the name (ship version); v1 puts the name on a board planted beside the doors
base = __file__.rsplit("/", 1)[0]
f = ImageFont.truetype(base + "/fonts/BBH-Hegarty.ttf", 54)
name = "analyze-system"
d.rectangle([bx, by - 4, bx + bw, by + 44], fill=HARBOR)
if A != "--v1":
    d.text(((bx + bx + bw) / 2, by + 20), name, font=f, fill=CREAM, anchor="mm")
    if A != "--v2":  # salt dulling at the letter edges (v2 keeps the paint implausibly fresh)
        for _ in range(160):
            x = random.uniform(bx + 90, bx + bw - 90); y = random.uniform(by + 2, by + 40)
            d.ellipse([x - 3, y - 1.4, x + 3, y + 1.4], fill=(39, 80, 110, 120))
else:
    d.rectangle([880, 300, 1240, 356], fill=HARBOR); d.rectangle([1052, 356, 1068, 430], fill=(70, 62, 52))
    d.text((1060, 328), name, font=f, fill=CREAM, anchor="mm")
# open doors and the boat in shadow
d.polygon([(bx + 70, by + 56), (bx + 218, by + 56), (bx + 168, by + bh), (bx + 26, by + bh)], fill=(72, 64, 54))
d.polygon([(bx + bw - 70, by + 56), (bx + bw - 218, by + 56), (bx + bw - 168, by + bh), (bx + bw - 26, by + bh)], fill=(72, 64, 54))
d.rectangle([bx + 218, by + 56, bx + bw - 218, by + bh], fill=(22, 24, 26))
d.polygon([(bx + 452, by + 130), (bx + 540, by + 226), (bx + 512, by + 316), (bx + 402, by + 316), (bx + 386, by + 226)], fill=HARBOR)
d.polygon([(bx + 396, by + 232), (bx + 528, by + 232), (bx + 512, by + 272), (bx + 404, by + 272)], fill=CREAM)
d.rectangle([bx + 404, by + 316, bx + 508, by + 332], fill=(52, 48, 44))
# shingle apron continuing right under the tide board down to the water
d.polygon([(810, 300), (1240, 380), (1180, 520), (820, 470)], fill=(176, 158, 124))
for _ in range(500):
    x, y = random.uniform(830, 1220), random.uniform(320, 500)
    r = random.uniform(3, 7); d.ellipse([x - r, y - r * .6, x + r, y + r * .6], fill=random.choice([(150, 138, 116), (130, 130, 126), (188, 170, 134)]))
# slipway: straight iron run from the doorway to the surf line, centre from (500,426) to (580,664)
for s in (-1, 1):
    d.line([(500 + s * 96, by + bh), (580 + s * 276, 664)], fill=RUST, width=15)
    d.line([(500 + s * 96, by + bh), (580 + s * 276, 664)], fill=(230, 220, 200), width=4)
for i in range(9):
    t = i / 8; y = by + bh + 14 + t * 210; cen = 506 + t * 68; half = 94 + t * 168
    d.line([(cen - half, y), (cen + half, y)], fill=(148, 122, 86), width=11)
d.line([(500, by + bh), (574, 640)], fill=CREAM, width=3)  # winch cable
# rocket flare post left, with coiled rope and a stack of oil lanterns
d.rectangle([92, 300, 104, 470], fill=(96, 74, 54)); d.ellipse([82, 282, 114, 314], fill=RUST)
for r in (36, 26, 17): d.ellipse([196 - r, 452 - r * .5, 196 + r, 452 + r * .5], outline=TAN, width=6)
for i, lx in enumerate((268, 268, 268)):
    yy = 452 - i * 46; d.rectangle([lx, yy - 34, lx + 26, yy], fill=(58, 56, 52)); d.rectangle([lx + 5, yy - 26, lx + 21, yy - 8], fill=(198, 188, 160))
# tide table board right under the eaves, chalk wiped clean
d.rectangle([bx + bw + 44, 150, bx + bw + 196, 272], fill=(196, 186, 158), outline=(96, 84, 66), width=4)
for yy in (178, 208, 238): d.line([(bx + bw + 62, yy), (bx + bw + 178, yy)], fill=(214, 206, 182), width=4)
# gulls holding over the shingle
for (x, y, s) in [(1150, 110, 17), (1280, 76, 12), (1420, 140, 20), (1040, 190, 11)]:
    d.arc([x - s, y - s // 2, x, y + s // 2], 200, 330, fill=(90, 96, 100), width=3)
    d.arc([x, y - s // 2, x + s, y + s // 2], 210, 340, fill=(90, 96, 100), width=3)
img.save(sys.argv[2] if len(sys.argv) > 2 else "banner.png")
print("banner saved")
