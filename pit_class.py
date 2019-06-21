#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from os import system,listdir
import argparse

class PIT:
    def __init__(self,*arg,**kwargs):
        if kwargs['filename'] != None:
            self.filename = kwargs['filename']
        else:
            self.filename = ""
        if kwargs['dir'] != None:
            self.outputDirectory = kwargs['dir']
        else:
            self.outputDirectory = "pit_output"
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
    def isPrime(self,number):
        if number > 1:
            for i in range(2,number):
                if number % i == 0:
                    return False
            return True
        else:
            return False

    def getCI(self,TM):
        TM = TM/8
        if TM % 2 == 0:
            return 'R'
        elif isPrime(TM):
            return 'B'
        else :
            return 'G'

    def get2LSB(self,arg):
        bits = format(arg,'b')
        bits = '0'*(8-len(bits))+bits
        return bits[len(bits)-2]+bits[len(bits)-1]

    def execute(self):
        self.createOutputDirectory()
        msglength = []
        if self.verbose:
            print "[+] Name file : "+self.filename
            print "[+] size of img : "+str(self.file.width)+"x"+str(self.file.height)
        for i in range(3):
            msglength.append(format(self.pixel[i,0][0],'b'))
            msglength.append(format(self.pixel[i,0][1],'b'))
            if i < 2 :
                msglength.append(format(self.pixel[i,0][2],'b'))

        for i in range(len(msglength)):
            msglength[i] = '0'*(8-len(msglength[i]))+msglength[i]

        msglength = ''.join(msglength)
        TM = int(msglength,2)
        if self.verbose:
            print '[+] Size of embedded message : '+str(TM)
            print '[+] Size in octets : '+str(TM/8)

        CI = self.getCI(TM)
        parity = format(TM,'b').count('1')

        if CI == 'R':
            if parity % 2 == 0 :
                if self.verbose:
                    print 'parity : EVEN'
                C1 = 'B'
                C2 = 'G'
            else :
                if self.verbose:
                    print 'parity : ODD'
                C1 = 'G'
                C2 = 'B'
        elif CI == 'G':
            if parity % 2 == 0:
                if self.verbose:
                    print 'parity : EVEN'
                C1 = 'B'
                C2 = 'R'
            else:
                if self.verbose:
                    print 'parity : ODD'
                C1 = 'R'
                C2 = 'B'
        elif CI == 'B':
            if parity % 2 == 0:
                if self.verbose:
                    print 'parity : EVEN'
                C1 = 'G'
                C2 = 'R'
            else:
                if self.verbose:
                    print 'parity : ODD'
                C1 = 'R'
                C2 = 'G'

        hiddendata = ''
        count = TM
        if self.verbose:
            print 'indicator channel : '+CI
            print 'Channel 1 : '+C1+';'
            print 'Channel 2 : '+C2+';'

        tosub1 = 2
        tosub2 = 4
        i = 1 #begin to second line
        while i < self.file.height and count > 0 :
            j = 0
            while j < self.file.width and count > 0:
                red = self.pixel[j,i][0]
                green = self.pixel[j,i][1]
                blue = self.pixel[j,i][2]
                if  CI == 'R':
                    if self.get2LSB(red) == '01':
                        if C2 == 'G':
                            hiddendata += self.get2LSB(green)
                        elif C2 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub1
                    elif self.get2LSB(red) == '10':
                        if C1 == 'G':
                            hiddendata += self.get2LSB(green)
                        elif C1 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub1
                    elif self.get2LSB(red) == '11':
                        if C1 == 'G':
                            hiddendata += self.get2LSB(green)
                        elif C1 == 'B':
                            hiddendata += self.get2LSB(blue)
                        if C2 == 'G':
                            hiddendata += self.get2LSB(green)
                        elif C2 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub2


                elif CI == 'G':
                    if self.get2LSB(green) == '01':
                        if C2 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C2 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub1
                    elif self.get2LSB(green) == '10':
                        if C1 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C1 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub1
                    elif self.get2LSB(green) == '11':
                        if C1 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C1 == 'B':
                            hiddendata += self.get2LSB(blue)
                        if C2 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C2 == 'B':
                            hiddendata += self.get2LSB(blue)
                        count -= tosub2


                elif CI == 'B':
                    if self.get2LSB(blue) == '01':
                        if C2 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C2 == 'G':
                            hiddendata += self.get2LSB(green)
                        count -= tosub1
                    elif self.get2LSB(blue) == '10':
                        if C1 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C1 == 'G':
                            hiddendata += self.get2LSB(green)
                        count -= tosub1
                    elif self.get2LSB(blue) == '11':
                        if C1 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C1 == 'G':
                            hiddendata += self.get2LSB(green)
                        if C2 == 'R':
                            hiddendata += self.get2LSB(red)
                        elif C2 == 'G':
                            hiddendata += self.get2LSB(green)
                        count -= tosub2

                j+=1
            i+=1

        hiddenmessage = ''
        for i in range(0,len(hiddendata),8):
            hiddenmessage += chr(int(hiddendata[i:i+8],2))


        print hiddenmessage
        f = open(self.outputDirectory+'/pit_'+self.filename.split('.')[0]+'.'+self.extension,'w')
        f.write(hiddenmessage)
        f.close()
        if self.verbose:
            print 'File with extracted data was created !'

parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename',help="The filename to compute stegano operation",required=True)
parser.add_argument('-dir','--output_directory',help="The output directory to store resultat")
parser.add_argument('-v','--verbose',help="Give more output",action="store_true")
args = parser.parse_args()



if __name__ == '__main__':
    pit = PIT(filename=args.filename,dir=args.output_directory,verbose=args.verbose)
    pit.open(rgb=True)
    pit.execute()
