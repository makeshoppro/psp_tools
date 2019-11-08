import imageio
from PIL import Image
import sys

#convert list into a tuple
def convert(list):
    return tuple(i for i in list)

# the filename should be passed in as an arugment
print ("The image we are working on is: %s" % (sys.argv[1]))

imgObj = imageio.imread(sys.argv[1])

imgHeight = imgObj.shape[0]
imgLength = imgObj.shape[1]

# create the outbound image
outImg = Image.new('RGBA', (imgLength, imgHeight), (255,0,0,0))
editableImg = outImg.load()

print ("Processing image...")

lastColor = imgObj[0,0];
for row in range(imgHeight):
    # reset to fully transparent
    lastColor = (0,0,0,0)
    
    for col in range (imgLength):        
        #look for non-transparent pixels
        if imgObj[row, col][3] > 0:
            lastColor = convert(imgObj[row,col]);

    # fill the row of the outbound image
    for ocol in range (imgLength):
        editableImg[ocol, row] = lastColor

# save the pixel stretch image
imageio.imwrite("pixel_stretch.png", outImg)
