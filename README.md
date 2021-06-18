# EMBROIDERED ELECTRONIC RESISTOR GENERATION (v3.0)

## Background / info
This is part of a research project to develop flexible wearable electronics. 

This python tool generates .exp files which are used by Melco, Bravo, and Bernina machines.

The embroidery package pyembroidery is used to convert to the file type of your choice (dst,pec,pes,exp,vp3,jef,u01,svg,csv,xxx,png,txt,gcode)


Give the program input parameters such as target resistance and unit resistance of the conductive thread. 

All parameters are adjustable, such as gap length between lines, stitch length, terminal pad length, etc. 


The program will create a resistor to your specifications, save the .exp file, convert the file to your specified file type, and show the generated resistor in a plot. 


## Links:
Instructions on package use:
https://www.appropedia.org/w/index.php?title=Embroidered_Electrical_Resistor_Generation

Cloud manufacturing page for embroidered electronics:
https://socl.frigate.me/
(still in development, this resistor generation package will be added as a functionality to the website soon)

Literature review on this and related technologies:
https://www.appropedia.org/Open_Source_Wearable_Electronics_from_Embroidery_Machines_literature_review

## Note
(Requires libraries: numpy, math, matplotlib, pyembroidery)
(Made in Python 3.8, last edit June 17, 2021)
