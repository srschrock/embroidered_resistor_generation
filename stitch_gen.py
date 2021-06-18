
def main_block (x,y, xpoint,ypoint,sl,pl,gl,tgl,right_bottom_stitches,width_stitches,height_stitches):
    #start of main block
    tl=0

    #move from start to bottom right corner
    for i in range(0,right_bottom_stitches):
        xpoint.append(x)
        ypoint.append(y)
        x += sl;
        tl += sl;

    #step upwards 2 gap lengths
    for step in range(0,2):
        xpoint.append(x)
        ypoint.append(y)
        y += gl;
        tl += gl;


    #repeating columns for main block
    for i in range(0,width_stitches):
        for i in range (0,height_stitches):
            xpoint.append(x)
            ypoint.append(y)
            y += sl;
            tl += sl;
        xpoint.append(x)
        ypoint.append(y)
        x -= gl;
        tl += gl;
        for i in range(0,height_stitches):
            xpoint.append(x)
            ypoint.append(y)
            y -= sl;
            tl += sl;
        xpoint.append(x)
        ypoint.append(y)
        x -= gl;
        tl += gl;
    #end of while loop, vertical tabs done

    x=x+gl; #cancel x jump of last loop

    for step in range(0,2):
        xpoint.append(x)
        ypoint.append(y)
        y -= gl; #step down to start return path
        tl += gl;


    #return to left terminal pad
    while x < -pl-tgl:
    #for i in range(0,left_bottom_stitches):
        xpoint.append(x)
        ypoint.append(y)
        x += sl;
        tl += sl;
    #print(xpoint)
    return(x,y, xpoint,ypoint,tl)