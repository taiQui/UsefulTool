#!/usr/bin/env python
# -*- coding:utf-8 -*-
from math import log
from PIL import Image
from sys import argv,exit


# Arg ----------
f_value = ''
type = 0
l_value = 0
verbose = False
rgb_value = 0
#---------------
def help():
    print '# HELP ------------------------'
    print '# pvd [-way [zigzag - regular] ] [-f file] [-l line] [-rgb r|g|b]'
    print '#------------------------------'
# Gestion des arguments ----------------
fullcmd = []
for i in range(1,len(argv)):
    fullcmd.append(argv[i])
try:
    if "-f" in fullcmd:
        if fullcmd[fullcmd.index('-f')+1][0] != '-':
            f_value = fullcmd[fullcmd.index('-f')+1]
        else :
            print '[-] bad file given'
            help()
            exit()
    else:
        print '[-] Error no file given'
        exit()
except:
    print '[-] Error -f'
    exit()
if "-v" in fullcmd:
    verbose = True

if "-way" in fullcmd:
    if fullcmd[fullcmd.index('-way')+1][0] != '-':
        if "zigzag" == fullcmd[fullcmd.index('-way')+1]:
            type = 1
        elif "regular" == fullcmd[fullcmd.index('-way')+1]:
            type = 2
    else:
        print '[-] Errot with -way arg'
        exit()
try:
    if "-rgb" in fullcmd:
        if fullcmd[fullcmd.index('-rgb')+1][0] != '-':
            if len(fullcmd[fullcmd.index('-rgb')+1])> 1:
                print '[-] Error len max 1 contain : r or  g or b'
                exit()
            if fullcmd[fullcmd.index('-rgb')+1] == 'r':
                rgb_value = 0
            elif fullcmd[fullcmd.index('-rgb')+1] == 'g':
                rgb_value = 1
            elif fullcmd[fullcmd.index('-rgb')+1] == 'b':
                rgb_value = 2
        else:
            print '[-] Error in rgb arg'
            exit()
    else:
        rgb_value = 2
except:
    print '[-] Error with -rgb value'
    help()
    exit()
#---------------------------------------

def pvd (pix1,pix2):
    dif = abs(pix2-pix1)
    #nb bite to get in difference
    nbit = 0
    #byte steam hidden
    bsh = 0
    if dif >= 0 and dif <= 7:
        nbit = int(log(7-0+1,2))
        bsh = dif - 0
    elif dif >= 8 and dif <= 15:
        nbit = int(log(15-8+1,2))
        bsh = dif - 8
    elif dif >= 16 and dif <= 31:
        nbit = int(log(31-16+1,2))
        bsh = dif - 16
    elif dif >= 32 and dif <= 63:
        nbit = int(log(63-32+1,2))
        bsh = dif - 32
    elif dif >= 64 and dif <= 127:
        nbit = int(log(127-64+1,2))
        bsh = dif - 64
    elif dif >= 128 and dif <= 255:
        nbit = int(log(255-128+1,2))
        bsh = dif - 128
    data = format(bsh,'b').zfill(nbit)
    return data

im = Image.open(f_value).convert('RGB')
pix = im.load()

# ARG ---------------------------------

if "-l" in fullcmd:
    if fullcmd[fullcmd.index('-l')+1][0] != '-':
        if fullcmd[fullcmd.index('-l')+1].isdigit():
            l_value = int(fullcmd[fullcmd.index('-l')+1])
        else:
            print '[-] Error NaN for -l arguments'
            exit()
    else:
        print '[-] Error in arguments of -l'
        help()
        exit()
else:
    l_value = im.height
#--------------------------------------





if verbose:
    print '[*] File loaded : '+f_value
    print '[*] Size : '+str(im.width)+"*"+str(im.height)
data = ''
def zigzag():
    data = ''
    if verbose:
        print '[*] Way in zigzab executing'
    for i in range(l_value):
        if i % 2 == 0:
            min = 1
            max = im.width
            step = 2
        else:
            min = im.width-2
            max = -1
            step = -2
        for j in range(min,max,step):
            val =  pix[j,i][rgb_value]
            if i % 2 == 0:
                val2 = pix[j-1,i][rgb_value]
            else:
                val2 = pix[j+1,i][rgb_value]

            data += pvd(val,val2)
    return data
def regular():
    data = ''
    if verbose:
        print '[*] Regular way executing'
    for i in range(l_value):
        for j in range(1,im.width,2):
            r,g,b = pix[j,i]
            r2,g2,b2 = pix[j-1,i]
            data += pvd(b2-b)
    return data

if type == 0:
    print '[-] ERROR no action given'
    help()
    exit()
elif type == 1:
    data = zigzag()
elif type == 2:
    data = regular()
yolo = ''
for i in range(0,len(data),8):
    yolo += chr(int(data[i:i+8],2))
print yolo
