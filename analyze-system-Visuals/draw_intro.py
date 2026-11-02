#!/usr/bin/env python3
"""analyze-system intro: the lifeboat station slipway, scenery only, nothing readable.
Wet shingle at close focus in the foreground with the two rust red rails entering from the
lower edge and climbing away, open boathouse doors midground with the lifeboat bow on its
carriage in partial shadow, winch cable down the centre, rope coil and two unlit lanterns
against the wall, tide board turned blank side out, surf line and grey green water behind,
low sail cream and pale harbor blue sky with gulls hanging as small still shapes."""
import math, random, sys
from PIL import Image, ImageDraw
random.seed(41)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1600, 680
HARBOR = (39, 80, 110); RUST = (166, 58, 43); TAN = (200, 168, 120); CREAM = (242, 234, 216)
SEA = (110, 131, 120); DARK = (30, 34, 36)
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img, "RGBA")
# low sky, sail cream to pale harbor blue
for y in range(0, 300):
    t = y / 300; d.line([(0, y), (W, y)], fill=(int(242 - 60 * t), int(234 - 52 * t), int(216 - 6 * t)))
# sea band right and behind the bank
d.polygon([(980, 250), (1600, 236), (1600, 470), (1120, 470)], fill=SEA)
for i in range(9):  # short breaking ranks of surf
    y = 300 + i * 20; x0 = 1080 + (i % 3) * 60
    d.line([(x0, y), (x0 + 300, y - 6)], fill=(238, 240, 232, 200), width=5)
# shingle bank: broad slope of rope tan and grey stones
d.polygon([(0, 300), (980, 250), (1120, 470), (1600, 470), (1600, 680), (0, 680)], fill=(168, 150, 118))
for _ in range(2600):
    x, y = random.uniform(0, W), random.uniform(300, H)
    r = random.uniform(3, 9); g = random.choice([(150, 138, 116), (128, 128, 124), (186, 168, 132), (110, 112, 108)])
    if y < 470 and x > 1080: continue
    d.ellipse([x - r, y - r * .6, x + r, y + r * .6], fill=g)
# wet dark band where the surf last reached
d.polygon([(0, 560), (1600, 540), (1600, 680), (0, 680)], fill=(120, 108, 88, 90))
# boathouse at the top of the bank, left of centre
bx, by, bw, bh = 300, 120, 460, 300
d.rectangle([bx, by, bx + bw, by + bh], fill=(214, 205, 184))               # station wall
d.polygon([(bx - 26, by), (bx + bw + 26, by), (bx + bw - 60, by - 62), (bx + 60, by - 62)], fill=(86, 74, 62))  # roof
d.rectangle([bx, by - 8, bx + bw, by + 26], fill=HARBOR)                    # lintel board, left blank in this view
# open doors swung outward
d.polygon([(bx + 60, by + 40), (bx + 196, by + 40), (bx + 150, by + bh), (bx + 22, by + bh)], fill=(70, 62, 52))
d.polygon([(bx + bw - 60, by + 40), (bx + bw - 196, by + 40), (bx + bw - 150, by + bh), (bx + bw - 22, by + bh)], fill=(70, 62, 52))
d.rectangle([bx + 196, by + 40, bx + bw - 196, by + bh], fill=(24, 26, 28))  # dark doorway
# lifeboat bow on its carriage in partial shadow inside the doorway
d.polygon([(bx + 300, by + 110), (bx + 380, by + 190), (bx + 356, by + 268), (bx + 268, by + 268), (bx + 250, by + 190)], fill=HARBOR)
d.polygon([(bx + 262, by + 196), (bx + 368, by + 196), (bx + 356, by + 232), (bx + 268, by + 232)], fill=CREAM)
d.rectangle([bx + 268, by + 268, bx + 352, by + 284], fill=(52, 48, 44))     # carriage
for cx in (bx + 282, bx + 338): d.ellipse([cx - 13, by + 276, cx + 13, by + 302], fill=(30, 30, 30))
# slipway rails from the lower edge climbing to the doorway, rust sides, polished tops
# centre line runs from (720, 690) at the foot to (530, 420) at the doorway
for s in (-1, 1):
    d.line([(720 + s * 330, 690), (530 + s * 62, by + bh)], fill=RUST, width=17)
    d.line([(720 + s * 330, 690), (530 + s * 62, by + bh)], fill=(226, 216, 196), width=5)
# sleepers crossing between the rails at shortening intervals, centred on the same line
for i in range(11):
    t = i / 10; y = 660 - t * 225; cen = 703 - t * 173; half = 312 - t * 238
    d.line([(cen - half, y), (cen + half, y - 6)], fill=(146, 120, 84), width=13)
# winch cable down the centre line, hook resting on the lowest sleeper
d.line([(530, by + bh), (694, 644)], fill=CREAM, width=4)
d.arc([680, 626, 708, 660], 300, 130, fill=(210, 200, 178), width=5)
# rope coil and two unlit oil lanterns against the station wall
for r in (34, 25, 16): d.ellipse([150 - r, 420 - r * .5, 150 + r, 420 + r * .5], outline=TAN, width=6)
for lx in (838, 884):
    d.rectangle([lx, 386, lx + 26, 430], fill=(58, 56, 52)); d.rectangle([lx + 5, 396, lx + 21, 420], fill=(196, 186, 158))
    d.arc([lx - 2, 368, lx + 28, 392], 180, 360, fill=(58, 56, 52), width=4)
# tide board under the eaves, blank side out (v2 flaw: chalk figures left showing)
d.rectangle([806, 150, 936, 262], fill=(188, 176, 150), outline=(96, 84, 66), width=4)
if A == "--v2":
    for yy in range(172, 250, 24): d.line([(822, yy), (920, yy)], fill=(70, 70, 70), width=5)
# gulls hanging as small still shapes
for (x, y, s) in [(1120, 120, 16), (1240, 88, 12), (1360, 150, 19), (180, 96, 13), (90, 150, 10)]:
    d.arc([x - s, y - s // 2, x, y + s // 2], 200, 330, fill=(90, 96, 100), width=3)
    d.arc([x, y - s // 2, x + s, y + s // 2], 210, 340, fill=(90, 96, 100), width=3)
if A == "--v1":  # v1 flaw pass marker: rails drawn thin and grey, reading as a road vanishing point
    d.line([(470, 690), (568, 420)], fill=(120, 122, 120), width=26); d.line([(1130, 690), (692, 420)], fill=(120, 122, 120), width=26)
img.save(sys.argv[2] if len(sys.argv) > 2 else "intro-banner.png")
print("intro saved")
