# This script requires that you pass in the black and white image as the first paramter, 
# and the hue map image as the second paramter.

import imageio
from PIL import Image
import sys

#convert list into a tuple
def convert(list):
    return tuple(i for i in list)

# the filename should be passed in as an arugment
print ("The image we are working on is: %s" % (sys.argv[1]))
print ("The Map is is: %s" % (sys.argv[2]))

imgObj = imageio.imread(sys.argv[1])
colorMap = imageio.imread(sys.argv[2])

if (colorMap.shape[1] != 255):
	print("Color map must be exactly 255 pixels wide")
	exit()

imgHeight = imgObj.shape[0]
imgLength = imgObj.shape[1]

print("Image height: ", imgHeight)
print("Image length: ", imgLength)
print("Map height: ", colorMap.shape[0])
print("Map length: ", colorMap.shape[1])

# create the outbound image
outImg = Image.new('RGBA', (imgLength, imgHeight), (255,0,0,0))
editableImg = outImg.load()

print ("Processing image...")

for row in range(imgHeight):   
	for col in range (imgLength):        
		# if pixel is gray, use its value as index
		if ((imgObj[row, col][0] == imgObj[row, col][1]) and (imgObj[row, col][1] == imgObj[row, col][2])):
			index = imgObj[row, col][0] if imgObj[row, col][0] < 255 else 254
			editableImg[col, row] = convert(colorMap[0, index])
		else:
		# if not gray, convert to luminance first
			luminance = (0.2126 * imgObj[row, col][0] + 0.7152 * 
				imgObj[row, col][1] + 0.0722 * imgObj[row, col][2])
			if luminance > 254: 
				luminance = 254

			editableImg[col, row] = convert(colorMap[0, round(luminance)])
			
# save the image
imageio.imwrite("colored_img.png", outImg)
