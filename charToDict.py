# Go through each file in /chars and create a dictionary with the number of white pixels in that .png image as the key and the character as the value.

import os
from PIL import Image
import json

folder = "chars"
charDict = {}

for file in os.listdir(folder):
    img = Image.open(f"{folder}/{file}")
    white = 0
    for pixel in img.getdata():
        if pixel == (255, 255, 255):
            white += 1
    charDict[white] = chr(int(file.split(".")[0]))

# Sort from dictionary with the least white pixels to the most
charDict = dict(sorted(charDict.items()))

# Check for duplicate keys
for key in charDict:
    if list(charDict).count(key) > 1:
        print(f"Duplicate key: {key}")

# Scale 0 and 255 and make a new dictionary
maxWhite = max(charDict.keys())
newCharDict = {}
for key in charDict:
    newCharDict[round((key / maxWhite) * 255, 4)] = charDict[key]

# Export as .json
with open("charDict.json", "w") as f:
    json.dump(newCharDict, f, indent=4)