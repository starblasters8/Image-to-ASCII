# Ascii characters 32-126
# Creates a .png file of each character in folder /chars

import os
from PIL import Image, ImageDraw, ImageFont

folder = "chars"

if not os.path.exists(folder):
    os.makedirs(folder)

range_start = 32
range_end = 127
ignore = [92]

for i in range(range_start, range_end):
    if i not in ignore:
        img = Image.new('RGB', (100, 100), color = (0, 0, 0))
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('arial.ttf', 75)
        d.text((5,0), chr(i), font=fnt, fill=(255,255,255))
        img.save(f"{folder}/{i}.png")