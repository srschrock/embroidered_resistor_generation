
# loops to generate the pattern
#right connector, square pad
def pad_right(x,y, xpoint,ypoint,sl,pl,pad_rows):

    #horizontal lines
    for i in range(0,pad_rows):
        for ii in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            x=x+pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        y=y+pl/(pad_rows*2-1);
        for ii in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            x=x-pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        y=y+pl/(pad_rows*2-1);
    #end of the loop to create connector pad (horizontal lines) (right)
    y=y-pl/(pad_rows*2-1); #offset last movement

    #vertical lines
    for i in range(0,pad_rows):
        for ii in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            y=y-pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        x=x+pl/(pad_rows*2-1);
        for ii in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            y=y+pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        x=x+pl/(pad_rows*2-1);
    # end of the loop to create connector (vertical lines) (right)
    x = x - pl / (pad_rows*2-1);  # step back to top of pad
    return x, y, xpoint, ypoint
# end of function pads_right






#second terminal pad (left)
def pad_left(x,y, xpoint,ypoint,sl,pl,pad_rows):
    # vertical lines
    for i in range(0,pad_rows):
        for i in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            y-=pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        x+=pl/(pad_rows*2-1);
        for i in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            y+=pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        x+=pl/(pad_rows*2-1);
    # end of the loop to create connector (vertical lines) (left)
    x-=pl/(pad_rows*2-1);

    #horizontal lines
    for i in range(0,pad_rows):
        for i in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            x-=pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        y-=pl/(pad_rows*2-1);
        for i in range(0,pad_rows):
            xpoint.append(x)
            ypoint.append(y)
            x+=pl/pad_rows;
        xpoint.append(x)
        ypoint.append(y)
        y-=pl/(pad_rows*2-1);
    # end of the loop to create connector pad (horizontal lines) (left)
    y += pl / (pad_rows*2-1);
    return x, y, xpoint, ypoint