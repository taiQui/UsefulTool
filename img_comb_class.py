#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from os import system,listdir
import argparse


class IMG_COMB:
    def __init__(self,*arg,**kwargs):

        if kwargs['file1'] != None:
            self.file1 = kwargs['file1']
        else:
            self.file1 = ""
        if kwargs['file2'] != None:
            self.file2 = kwargs['file2']
        else:
            self.file2 = ""
        if kwargs['dir'] != None:
            self.outputDirectory = kwargs['dir']
        else:
            self.outputDirectory = "img_comb_output"
        if kwargs['verbose'] != None:
            if kwargs['verbose'] == True:
                self.verbose = True
            else:
                self.verbose = False
        else:
            self.verbose = False
        self.file = ""
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
            if 'rgb' in kwargs:
                self.img1 = Image.open(self.file1).convert('RGB')
                self.img2 = Image.open(self.file2).convert('RGB')
                self.imgaux = Image.open(self.file1).convert('RGB')
            else:
                self.img1 = Image.open(self.file1)
                self.img2 = Image.open(self.file2)
                self.imgaux = Image.open(self.file1)
            self.extension = self.file1.split('.')[-1]
        except Exception as e:
            print 'Error opening file '
            print e
            exit()
        self.getPixel()

    def getPixel(self):
        try:
            self.pixelim1 = self.img1.load()
            self.pixelim2 = self.img2.load()
            self.pixelaux = self.imgaux.load()
        except Exception as e:
            print 'Error getting pixel'
            print e

    def execute(self,*arg,**kwargs):
        self.createOutputDirectory()
        if kwargs['action'] != None:
            for i in range(self.img1.height):
                for j in range(self.img1.width):
                    r1,g1,b1 = self.pixelim1[j,i]
                    r2,g2,b2 = self.pixelim2[j,i]

                    if kwargs['action'] == 'and':
                        self.pixelaux[j,i] = ((r1 and r2),(g1 and g2),(b1 and b2))
                    elif kwargs['action'] == 'or':
                        self.pixelaux[j,i] = ((r1 or r2),(g1 or g2),(b1 or b2))
                    elif kwargs['action'] == 'xor':
                        self.pixelaux[j,i] = ((r1 ^ r2),(g1 ^ g2),(b1 ^ b2))
                    elif kwargs['action'] == 'add':
                        self.pixelaux[j,i] = (((r1 + r2)%255),((g1 + g2)%255),((b1 + b2)%255))
                    elif kwargs['action'] == 'sub':
                        self.pixelaux[j,i] = (((r1 - r2)%255),((g1 - g2)%255),((b1 - b2)%255))
                    elif kwargs['action'] == 'mul':
                        self.pixelaux[j,i] = (((r1 * r2)%255),((g1 * g2)%255),((b1 * b2)%255))
            self.imgaux.save(self.outputDirectory+'/imgcmb_'+kwargs['action']+'.'+self.extension)
            if self.verbose:
                print '[+] Image combined saved.'
        else:
            for k in range(6):
                for i in range(self.img1.height):
                    for j in range(self.img1.width):
                        r1,g1,b1 = self.pixelim1[j,i]
                        r2,g2,b2 = self.pixelim2[j,i]

                        if k == 0:
                            self.pixelaux[j,i] = ((r1 and r2),(g1 and g2),(b1 and b2))
                        elif k == 1:
                            self.pixelaux[j,i] = ((r1 or r2),(g1 or g2),(b1 or b2))
                        elif k == 2:
                            self.pixelaux[j,i] = ((r1 ^ r2),(g1 ^ g2),(b1 ^ b2))
                        elif k == 3:
                            self.pixelaux[j,i] = (((r1 + r2)%255),((g1 + g2)%255),((b1 + b2)%255))
                        elif k == 4:
                            self.pixelaux[j,i] = (((r1 - r2)%255),((g1 - g2)%255),((b1 - b2)%255))
                        elif k == 5:
                            self.pixelaux[j,i] = (((r1 * r2)%255),((g1 * g2)%255),((b1 * b2)%255))
                self.imgaux.save(self.outputDirectory+'/imgcmb_'+str(k)+'.'+self.extension)
                if self.verbose:
                    print '[+] Image combined saved.'

parser = argparse.ArgumentParser()
parser.add_argument('-i1','--image1',help="Image 1 for image combiner",required=True)
parser.add_argument('-i2','--image2',help="Image 2 for image combiner",required=True)
parser.add_argument('-dir','--output_directory',help="The output directory to store resultat")
parser.add_argument('-v','--verbose',help="Give more output",action="store_true")
parser.add_argument('-a','--action',help="Give action in combiner image\nor | and | xor | add | sub | mul\n If no action given, all are executed")
args = parser.parse_args()

if __name__ == "__main__":
    a = IMG_COMB(file1=args.image1,file2=args.image2,verbose=args.verbose,dir=args.output_directory)
    a.open(rgb=True)
    a.execute(action=args.action)
