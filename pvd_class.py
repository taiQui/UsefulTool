#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from os import system,listdir
from math import log
import argparse

class PVD:
    def __init__(self,*arg,**kwargs):
        if kwargs['filename'] != None:
            self.filename = kwargs['filename']
        else:
            self.filename = ""
        if kwargs['dir'] != None:
            self.outputDirectory = kwargs['dir']
        else:
            self.outputDirectory = "pvd_output"
        if kwargs['verbose'] != None:
            self.verbose = True
        else:
            self.verbose = False

    def setFilename(self,arg):
        self.filename = arg

    def setOutputDirectory(self,arg):
        self.outputDirectory = arg

    def createOutputDirectory(self):
        if not self.checkOutputDirectory():
            system('mkdir '+self.outputDirectory)
            if self.verbose:
                print '[+] Output directory created'
        else:
            print '[-] Output directory still here'

    def checkOutputDirectory(self):
        directory = listdir('.')
        return (self.outputDirectory in directory)

    def open(self,*arg,**kwargs):
        try:
            if kwargs['rgb'] != None:
                self.file = Image.open(self.filename).convert('RGB')
            else:
                self.file = Image.open(self.filename)
            self.extension = self.filename.split('.')[-1]
        except Exception as e:
            print 'Error opening file '
            print e
            exit()
        self.getPixel()

    def getPixel(self):
        try:
            self.pixel = self.file.load()
        except Exception as e:
            print 'Error getting pixel'
            print e

    def pvd (self,pix1,pix2):
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

    def pvd_zigzag(self,*arg,**kwargs):
        self.createOutputDirectory()
        if kwargs['line'] != None:
            try:
                self.nbLine = int(kwargs['line'])
            except Exception as e:
                print '[-] Error in \'line\' arguments'
                print e
        else:
            self.nbLine = self.file.height
        if kwargs['rgb'] != None:
            if kwargs['rgb'] < 0 or kwargs['rgb'] >= 3:
                print '[-] Error on given rgb argument'
                exit()
            self.rgb = kwargs['rgb']
        else:
            self.rgb = 0

        data = ''
        if self.verbose:
            print '[+] zigzag'
        for i in range(self.nbLine):
            if i % 2 == 0:
                min = 1
                max = self.file.width
                step = 2
            else:
                min = self.file.width-2
                max = -1
                step = -2
            for j in range(min,max,step):
                val =  self.pixel[j,i][self.rgb]
                if i % 2 == 0:
                    val2 = self.pixel[j-1,i][self.rgb]
                else:
                    val2 = self.pixel[j+1,i][self.rgb]

                data += self.pvd(val,val2)
        msg = ""
        for i in range(0,len(data),8):
            msg += chr(int(data[i:i+8],2))
        f = open(self.outputDirectory+'/pvd_'+self.filename.split('.')[0]+'.'+self.extension,'w')
        f.write(msg)
        f.close()
        print msg
        if self.verbose:
            print '[+] File with extracted data was created.'
    def pvd_regular(self,*arg,**kwargs):
        self.createOutputDirectory()
        if 'line' in kwargs:
            try:
                self.nbLine = int(kwargs['line'])
            except Exception as e:
                print '[-] Error in \'line\' arguments'
                print e
        else:
            self.nbLine = self.file.height
        if 'rgb' in kwargs:
            if len(kwargs['rgb']) > 1:
                print '[-] Error in given rgb argument, must be size=1 and range 0-2 ( red : 0, green : 1, blue : 2)'
                exit()
            if not kwargs['rgb'].isdigit():
                print '[-] Error in given rgb argument, not an integer'
                exit()
            self.rgb = int(kwargs['rgb'])
        else:
            self.rgb = 0
        data = ''
        if self.verbose:
            print '[*] Regular'
        for i in range(self.nbLine):
            for j in range(1,self.file.width,2):
                chromato1 = self.pixel[j,i][self.rgb]
                chromato2 = self.pixel[j-1,i][self.rgb]
                data += self.pvd(chromato2,chromato1)
        msg = ""
        for i in range(0,len(data),8):
            msg += chr(int(data[i:i+8],2))
        f = open(self.outputDirectory+'/pvd_'+self.filename.split('.')[0]+'.'+self.extension,'w')
        f.write(msg)
        f.close()
        print msg
        if self.verbose:
            print '[+] File with extracted data was created.'



parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename',help="The filename to compute stegano operation",required=True)
parser.add_argument('-dir','--output_directory',help="The output directory to store resultat")
parser.add_argument('-v','--verbose',help="Give more output",action="store_true")
parser.add_argument('-rgb','--rgb',help="Give the pixel to applicate pvd",type=int)
parser.add_argument('-l','--line',help="The line's number which applicate pvd",type=int)
parser.add_argument('-m','--method',default="zigzag",help="Give method to use to go through pixel => zigzag | regular",required=True)
args = parser.parse_args()

if __name__ == '__main__':
    pvd = PVD(filename=args.filename,dir=args.output_directory,verbose=args.verbose)
    pvd.open(rgb=True)
    if args.method == "zigzag":
        pvd.pvd_zigzag(line=args.line,rgb=args.rgb)
    elif args.method == "regular":
        pvd.pvd_regulat(line=args.line,rgb=args.rgb)
