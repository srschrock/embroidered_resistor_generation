# RESISTOR FILE GENERATION TOOL (v2)
# 
# This program is for creating embroidery files for electrical resistors
#
# Developed in Python 3.8
# Last edit: May 1, 2021
# writes to .exp (Melco, Bravo, and Bernina machines)

import exp_generation
import stitch_gen
import pads
import numpy as np
import math
import matplotlib.pyplot as plt

################################
#### user inputs
################################

r = 6_000 # desired resistance (Ohms)
rho=25_000 # thread unit resistance (Ohms/m)
gl = 1; #gap length (spacing between rows) (mm)
sl = gl; #stitch length (gap between stitches) (mm)
tgl = 2*gl; #gap length between terminal pads (mm)
pl = 2.5; #pad length (mm)
pad_rows = 3 #terminal pad stitch density (number of stitch rows)

#making a filename reflective of target resistance and thread unit resistance
#rename to your own filename if you so choose, otherwise leave as is
file_name="".join(["R_",str(round(r/1000,1)),"kOhms_UR_",str(round(rho/1000,1)),"kOhmpm.exp"])


################################
#### initialize counters, lists, and (x,y) coords
################################

tl = 0; #total length of thread used (initialize counter)
xpoint=[]; ypoint=[] #initialize stitch coordinate lists
x = y = 0; #initial coordinates (0,0)


################################
#### pattern calculations
################################

len = r/rho; #desired length of thread (ft)
len = len*1000; #length of wire (mm)

w=(-8*gl+math.sqrt(gl)*math.sqrt(16*gl+24*len+24*tgl+48*pl))/4; #width of resistor
h=w*2/3; #height of the tines

width_stitches = int((w/2)/gl)+1
height_stitches = int(h/sl)

right_bottom_stitches = int((w/2-tgl/2-pl)/sl)


##################################
#### Start of stitching process
##################################

#right terminal pad
right_pad_matrix = pads.pad_right(x,y, xpoint,ypoint,sl,pl,pad_rows)
x=right_pad_matrix[0]; y=right_pad_matrix[1] #(x,y) coords of current stitch
xpoint=right_pad_matrix[2]; ypoint=right_pad_matrix[3]

# main body of the resistor
main_matrix=stitch_gen.main_block(x,y, xpoint,ypoint,sl,pl,gl,tgl,right_bottom_stitches,width_stitches,height_stitches)

x=main_matrix[0]; y=main_matrix[1] #(x,y) coords of current stitch

xpoint=main_matrix[2]; ypoint=main_matrix[3] #list of (x,y) stitches
tl=main_matrix[4] #length of thread used in resistor (no pads)

#add left terminal pad
main_matrix = pads.pad_left(x,y, xpoint,ypoint,sl,pl,pad_rows)
xpoint=main_matrix[2]; ypoint=main_matrix[3]


################################
#### file generation (convert to .exp)
################################

xpoint = np.asarray(xpoint); ypoint = np.asarray(ypoint)

dx,dy = exp_generation.make_file(xpoint,ypoint,file_name)


################################
#### plotting resistor pattern
################################

plt.plot(xpoint,ypoint,'r-',xpoint,ypoint,'x')
plt.ylabel('y coordinate (mm)')
plt.xlabel('x coordinate (mm)')
plt.title('Resistor Pattern')
plt.show()