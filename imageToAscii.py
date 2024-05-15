# Takes in an image, converts it to grayscale, and then to ascii characters and outputs a .txt file with the ascii art.

from PIL import Image
import json

# Number of characters in each line
width = 300

# Image path
imgPath = "samples/2.png"
outPath = "asciiArt.txt"

# Load the dictionary
with open("charDict.json", "r") as f:
    charDict = json.load(f)

# Load the image
img = Image.open(imgPath)
img = img.convert("L")

# Resize the image
aspectRatio = img.width / img.height
img = img.resize((width, int(width / aspectRatio)))


# Convert the image to ascii
asciiArt = ""
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        
        # Get the closest key in the dictionary
        closestKey = min(charDict.keys(), key=lambda key: abs(int(key) - (255-pixel)))
        asciiArt += 2 * charDict[closestKey]

    asciiArt += "\n"

# Output to file
with open(outPath, "w") as f:
    f.write(asciiArt)