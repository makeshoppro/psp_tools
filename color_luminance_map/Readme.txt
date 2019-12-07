Instructions
----------------------------------
To run this script, open a command prompt and navigate to the folder where this script lives.  Then enter the command:

python color_luminance_map.py <your_bw_image> <skin_map_image>

The skin_map_image can be any height, but must be exactly 255 pixels in width.  The darkest pixels should be on the left, and the lightest on the right.

Using the provided example map and image would look something like this:

python color_luminance_map.py bw.png skin_map.png

When the script is completed running, a new file called 'colored_img.png' should be created.

