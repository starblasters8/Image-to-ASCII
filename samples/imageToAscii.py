# Takes in an image, converts it to grayscale, and then to ascii characters and outputs a .txt file with the ascii art.

from PIL import Image
import json
import os

# Number of characters in each line
width = 500

clamp = True
mult = 1.0
sub = 0.0

# Load the dictionary
with open("charDict.json", "r") as f:
    charDict = json.load(f)

# Image path
imgPath = "samples/input/"
outPath = "samples/output/"

for file in os.listdir(imgPath):
    filename = os.path.splitext(file)[0]

    # Load the image
    img = Image.open(imgPath+file)
    img = img.convert("L")

    # Resize the image
    aspectRatio = (2*img.width) / img.height
    img = img.resize((width, int(width / aspectRatio)))

    # Clamp the image
    if clamp:
        # Find the min and max pixel values
        minVal = 255
        maxVal = 0

        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                minVal = min(minVal, pixel)
                maxVal = max(maxVal, pixel)

        sub = minVal
        mult = 255.0 / maxVal

    # Convert the image to ascii
    asciiArt = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            pixel = (pixel-sub)*mult
            
            # Get the closest key in the dictionary
            closestKey = min(charDict.keys(), key=lambda key: abs(float(key)-(255.0-pixel)))
            asciiArt += charDict[closestKey]

        asciiArt += "\n"

    # Output to file
    with open(outPath + filename + '.txt', "w") as f:
        f.write(asciiArt)