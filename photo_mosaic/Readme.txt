Instructions
----------------------------------
This script takes a set of images and creates a photo grid which can be combined with a 'reference image' which will be overlayed to create a faux photo mosaic.

Setup
----------------------------------
If you haven't already (from other scripts), install the following libraries with the following commands:

	pip install imageio

First create a folder named "Input".  Then copy the images you want included in the photo gride into this folder.  Note that only JPGs and PNGs are supported by this script.  Also note, that the shape of the images will be modified to match the 'reference image', so to minimize distoration, have the images in this folder match the 'reference image' as close as possible.

Copy your reference image (the one image you will combine with the photo grid), into the folder with the script.

Run the Script
----------------------------------
To run this script, open a command prompt and navigate to the folder where this script lives.  Then enter the command:

	python PhotoMosaic.py <referenc image to overlay>

The script will ask you how many images you want placed in a single row.  This essentially determines the resolution of the grid.  If you want a lot of small images, choose a high number.  If you want a grid with few but large images, choose a small number.

After entering this number, the script will load the images from your Input folder, and then generate the photo grid.  The final file will be called mosaic.png.
