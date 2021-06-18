# RESISTOR FILE GENERATION TOOL (v3)
# 
# This program is for creating embroidery files for electrical resistors
#
# Developed in Python 3.8
#
# Last edit: June 17, 2021
#
# writes directly to .exp (Melco, Bravo, and Bernina machines)
# includes conversion tool for all major embroidery file types


################################
#### USER INPUTS
################################

r = 75_000 # desired resistance (Ohms)
rho=90_000 # thread unit resistance (Ohms/m)
gl = 1; #gap length (spacing between rows) (mm)
sl = gl; #stitch length (gap between stitches) (mm)
tgl = 2*gl; #gap length between terminal pads (mm)
pl = 3.8; #pad length (mm)
pad_rows = 4 #terminal pad stitch density (number of stitch rows)

# supported file types to write to:
    #dst,pec,pes,exp,vp3,jef,u01,svg,csv,xxx,png,txt,gcode
file_type="dst" #desired file type

# making a filename reflective of target resistance and thread unit resistance
file_name="".join(["R_",str(round(r/1000,1)),"kOhms_UR_",
                   str(round(rho/1000,1)),"kOhmpm."])

# rename to your own filename if you so choose, otherwise leave as is
# file_name="manual_name." # be sure to include a "." at the end of the name


################################
#### Initialize counters, lists, and (x,y) coords
################################

tl = 0; #total length of thread used (initialize counter)
xpoint=[]; ypoint=[] #initialize stitch coordinate lists
x = y = 0; #initial coordinates (0,0)


################################
#### Pattern Calculations
################################

import numpy as np
import math

length = (r/rho)*1000; #desired length of thread (mm)

#width of resistor
w=(-8*gl+math.sqrt(gl)*math.sqrt(16*gl+24*length+24*tgl+48*pl))/4; 

h=w*2/3; #height of the tines (mm)

width_stitches = int((w/2)/gl)+1
height_stitches = int(h/sl)

right_bottom_stitches = int((w/2-tgl/2-pl)/sl)


##################################
#### Start of stitching process
##################################

import stitch_gen
import pads

#right terminal pad
x,y,xpoint,ypoint = pads.pad_right(x,y, xpoint,ypoint,sl,pl,pad_rows)

# main body of the resistor
x,y,xpoint,ypoint,tl =stitch_gen.main_block(x,y, xpoint,ypoint,sl,pl,gl,tgl,
                        right_bottom_stitches,width_stitches,height_stitches)

#add left terminal pad
x,y,xpoint,ypoint = pads.pad_left(x,y, xpoint,ypoint,sl,pl,pad_rows)


################################
#### Calculate dx & dy
################################

xpoint = np.asarray(xpoint); ypoint = np.asarray(ypoint)

#calc delta-x & y for each stitch
dx=[]; dy=[]
for i in range(0,int(len(xpoint))-1):
    dx.append(xpoint[i+1]-xpoint[i])
    dy.append(ypoint[i+1]-ypoint[i])


################################
#### File Generation .EXP
################################

import exp_generation
exp_generation.make_file(dx,dy,file_name)


################################
#### File Generation .DST
################################

# needs development, better off converting from the created.exp 
    # with conversion tool pyembroidery

# import dst_generation
# dst_generation.make_file(dx,dy,file_name)


################################
#### File Conversion (to any file type)
################################

# supported file types to write to:
    #dst,pec,pes,exp,vp3,jef,u01,svg,csv,xxx,png,txt,gcode

# if package not yet downloaded, use command "pip install pyembroidery"

if file_type != "exp":
    import pyembroidery
    
    # two step process:
    # pattern = pyembroidery.read("".join([file_name,"exp"]))
    # pyembroidery.write(pattern,"".join([file_name,file_type]))
    
    # or in one step:
    pyembroidery.convert("".join([file_name,"exp"]), 
                         "".join([file_name,file_type]))

# to show which file was created
print("File name: ","".join([file_name,file_type])) 


# to show file location:
# import os
# print("File location: ",os.getcwd()) 
    
################################
#### Plot Resistor Pattern
################################

import matplotlib.pyplot as plt
plt.plot(xpoint,ypoint,'r-',xpoint,ypoint,'x')
plt.ylabel('y coordinate (mm)')
plt.xlabel('x coordinate (mm)')
plt.title('Resistor Pattern')
plt.show()

