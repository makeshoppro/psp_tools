import numpy as np
from PIL import Image
import sys
import glob
import imageio
import random

imageList = []

#check for number of available images
numImages = len(glob.glob(".\Input\*.jpg")) + len(glob.glob(".\Input\*.png"))

if numImages < 1:
	print("Did not detect images, did you create a folder called 'Input' and places the images in it?")
	exit()

print("Number of images: " + str(numImages))
print("Reference Image is: " + sys.argv[1])

dimImage = imageio.imread(sys.argv[1])
dimHeight = dimImage.shape[0]
dimWidth = dimImage.shape[1]
image_ratio = dimHeight / dimWidth

print("Dimensions are [Height, Length] = [ " + str(dimHeight) + ", " + str(dimWidth) + "]")
print("Image ratio: ", image_ratio)

# get the resolution of the mosaic (as measured by number of images in width)
print("===============================")
resolution = int(input("How many images along width: "))
print("===============================")
numCols = resolution
numRows = resolution
cellWidth = round(dimWidth / resolution)
cellHeight = round(dimHeight / resolution)
totalCells = numCols * numRows

print("Mosaic Dimensions [Cells High, Cells Wide]: [" + str(numRows) + ", " + str(numCols) + "]")
print("Single cell is [Height, Length] = [ " + str(cellHeight) + ", " + str(cellWidth) + "]")
print("Total Cells: ", totalCells)

# load and resize all jpgs and pngs
print("Loading Input Images...")
for file in glob.glob(".\Input\*.jpg"):
	tempImage = Image.open(file)
	smallTemp = tempImage.resize((cellWidth, cellHeight), Image.NEAREST)
	imageList.append(smallTemp)
	
for pfile in glob.glob(".\Input\*.png"):
	tempImage = Image.open(file)
	smallTemp = tempImage.resize((cellWidth, cellHeight), Image.NEAREST)
	imageList.append(smallTemp)

print("Building Mosaic...")
for row in range(0, numRows, 1):
	for col in range(0, numCols, 1):
		if  col == 0:
			mergedCols = imageList[random.randint(0, numImages-1)]
		else:
			mergedCols = np.concatenate((mergedCols, imageList[random.randint(0, numImages-1)]), axis = 1)

	# merge rows into final image
	if row == 0:
		outPng = mergedCols
	else:
		outPng = np.concatenate((outPng,mergedCols),axis=0)

finalImage = Image.fromarray(outPng)
finalImage.save('mosaic.png')

print("Script Finished")
