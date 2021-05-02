import numpy

def make_file (xpoint,ypoint,file_name):
    #mm*10
    xpoint = [x*10 for x in xpoint]
    ypoint = [y*10 for y in ypoint]
    
    
    #calc delta-x & y for each stitch
    dx=[]; dy=[]
    for i in range(0,len(xpoint)-1):
        dx.append(xpoint[i+1]-xpoint[i])
        dy.append(ypoint[i+1]-ypoint[i])
    
    #helps filter out the 10's and 237's, important later
    dx = [numpy.round(x) for x in dx]
    dy = [numpy.round(y) for y in dy]
    
    #convert to byte
        #1-127 are forward by that amount 
        #129-255 are backward by that same amount
    dxn=[]; dyn=[]
        #chr(10) and chr(237) mess things up, FYI
        #need to alternate above and below these values to avoid offsets

    xpalt=True; xnalt=True; ypalt=True; ynalt=True;
    for stitch in range(0,len(dx)):
        if dx[stitch] < 0:
            dxn.append(dx[stitch]+256)
            if dxn[stitch] == 237:
                if xnalt==True:
                    dxn[stitch]=238
                else:
                    dxn[stitch]=236
                xnalt=not xnalt
        elif dx[stitch] == 10:
            if xpalt==True:
                dxn.append(11)
            else:
                dxn.append(9)
            xpalt=not xpalt
        else:
            dxn.append(dx[stitch])
    for stitch in range(0,len(dy)):
        if dy[stitch] < 0:
            dyn.append(dy[stitch]+256)
            if dyn[stitch] == 237:
                if ynalt==True:
                    dyn[stitch]=238
                else:
                    dyn[stitch]=236
                ynalt=not ynalt
        elif dy[stitch] == 10:
            if ypalt==True:
                dyn.append(11)
            else:
                dyn.append(9)
            ypalt=not ypalt
        else:
            dyn.append(dy[stitch])
    
    
    # convert movement number to uint8 format (hexad)
    # and merge into one continuous string
    string2=""
    for stitch in range(0,int(len(dxn)/1)):
        string2+=chr(int(dxn[stitch]))
        string2+=chr(int(dyn[stitch]))
    
    
    # write data to .exp file
    with open(file_name, 'w') as filehandle:
        filehandle.write(string2)

    #return values for troubleshooting if needed
    return dxn,dyn

