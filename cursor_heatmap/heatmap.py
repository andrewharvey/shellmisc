#!/usr/bin/python

#Renders mouse position data into a heat map.
#Based on the program http://launchpadlibrarian.net/42498022/heatmap.py
#input file should be in the format,
#(x,y)
#(x,y)
#..

from PIL import Image, ImageDraw
import math
import sys
import re

resolution = (1680, 1050)
background = (0,0,0)

if len(sys.argv) < 3:
	print "Usage: ./heatmap.py logfile dotalpha\n"
	sys.exit()
	
filename = sys.argv[1]

radius = 50

#vary this depend on the size of the input. eg 20 samples should need a higher alpha than 10000000
alpha = (int)(sys.argv[2])

im = Image.new("RGB", resolution, background)
draw = ImageDraw.Draw(im)
circle = Image.new("RGBA", (radius*2, radius*2))

for x in range(radius*2):
	for y in range(radius*2):
		dist = math.sqrt( (x-radius)**2+(y-radius)**2)
		if dist <= radius:
			circle.putpixel((x,y), (255, 0, 0, (int)(alpha-dist/radius*alpha)))

f = open(filename, 'r')

for line in  f.readlines():
	pos = eval(line);
	im.paste(circle, ( pos[0]-radius, pos[1]-radius, pos[0]+radius, pos[1]+radius ), circle)
	
del draw 
im.save(re.sub("\..*$",'',filename)+".jpg", "JPEG")

