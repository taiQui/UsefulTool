#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from os import system,listdir

class LSB:
    def __init__(self,*arg,**kwargs):
        if 'filename' in kwargs:
            self.filename = kwargs['filename']
        else:
            self.filename = ""
        if 'dir' in kwargs:
            self.outputDirectory = kwargs['dir']
        else:
            self.outputDirectory = "./lsb_output"
        if 'verbose' in kwargs:
            self.verbose = True
        else:
            self.verbose = False
        self.file = ""
    def setFile(self,arg):
        if self.verbose:
            print '[+] Filename set to '+arg
        self.filename=arg

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
        return ('lsb_ouput' in directory)

    def open(self,*arg,**kwargs):
        try:
            if 'rgb' in kwargs:
                self.file = Image.open(self.filename).convert('RGB')
                self.fileaux = Image.open(self.filename).convert('RGB')
            else:
                self.file = Image.open(self.filename)
                self.fileaux = Image.open(self.filename)
            self.extension = self.filename.split('.')[-1]
        except Exception as e:
            print 'Error opening file '
            print e
        self.getPixel()

    def getPixel(self):
        try:
            self.pixel = self.file.load()
            self.pixelaux = self.fileaux.load()
        except Exception as e:
            print 'Error getting pixel'
            print e

    def getBin(self,arg,i,j):
        r,g,b = arg[i,j]
        r = format(r,'b')
        while len(r) < 8:
            r = '0'+r
        g = format(g,'b')
        while len(g) < 8:
            g = '0'+g
        b = format(b,'b')
        while len(b) < 8:
            b = '0'+b
        return r,g,b

    def find(self,*arg,**kwargs):
        if self.file == "":
            print '[-] Need to open file first => method open'
            exit()
        self.createOutputDirectory()
        if self.verbose:
            print '[+] Find methode'
        self.numberLsbTakenForOutput = [0,9]
        if 'nblsb' in kwargs:
            self.numberLsbTakenForOutput = kwargs['nblsb']
        if 'line' in kwargs:
            self.nbLine = kwargs['line']
        else:
            self.nbLine = self.file.height
        for k in range(self.numberLsbTakenForOutput[0],self.numberLsbTakenForOutput[1]):
            for i in range(0, self.nbLine):
        	    for j in range(0,self.file.width):
        		    r,g,b = self.pixel[j,i]
        		    raux = bin(r).split('b')[1]
        		    while len(raux) < 8:
        		        raux = '0'+raux
        		    gaux = bin(g).split('b')[1]
        		    while len(gaux) < 8:
        		        gaux = '0'+gaux
        		    baux = bin(b).split('b')[1]
        		    while len(baux) < 8:
        		        baux = '0'+baux
        		    self.pixelaux[j,i] = (int(raux[k:9]+'0'*k,2),int(gaux[k:9]+'0'*k,2),int(baux[k:9]+'0'*k,2))

            self.fileaux.save(self.outputDirectory+'/decod'+str(k)+'.'+self.extension)
            if self.verbose:
                print '     [*]  file saved with '+str(int(8-k))+' lsb in '+self.outputDirectory+'/decod'+str(k)+'.'+self.extension


    def filter(self,filter):
        self.createOutputDirectory()
        if self.verbose:
            print '[+] Filter methode'
            print '[+] with filter : '+filter
        for i in range(self.file.height):
            for j in range(self.file.width):
                r = 0
                g = 0
                b = 0
                for k in filter:
                    if k == 'r':
                        r = self.pixel[j,i][0]
                    elif k == 'g':
                        g = self.pixel[j,i][1]
                    elif k == 'b':
                        b = self.pixel[j,i][2]
                self.pixel[j,i] = (r,g,b)
        self.file.save(self.outputDirectory+'/filter_'+filter+'.'+self.extension)
        if self.verbose:
            print '[+] filter saved !'

    def extract(self,*arg,**kwargs):
        rgb_value = ""
        if 'rgb' in kwargs:
            rgb_value = kwargs['rgb']
        else:
            rgb_value = [1,1,1,1]
        if 'line' in kwargs:
            self.nbLine = kwargs['line']
        else:
            self.nbLine = self.file.height
        if self.verbose:
            print '[+] EXTRACT execution'
            print '[+] will take '+str(rgb_value[0])+" red - "+str(rgb_value[1])+" green - "+str(rgb_value[2])+' blue with a jumps of '+str(rgb_value[3])+' between each pixel'
        hidden = ''
        for i in range(0, self.nbLine):#Line
            for j in range(0,self.file.width,rgb_value[3]): #collumn
                r,g,b = self.pixel[j,i]
                r =format(int(r),'b')
                r = r.zfill(8-len(r))
                g =format(int(g),'b')
                g = g.zfill(8-len(g))
                b =format(int(b),'b')
                b = b.zfill(8-len(b))
                hidden+=r[8-rgb_value[0]:]+g[8-rgb_value[1]:]+b[8-rgb_value[2]
                :]
        plain = ''
        for i in range(0,len(hidden),8):
            plain+=chr(int(hidden[i:i+8],2))
        if self.verbose:
            print 'plain text :'
        print plain
        f = open(self.outputDirectory+'/ext.'+self.extension,'w')
        f.write(plain)
        f.close()
        if self.verbose:
            print '[+] File with extracted data created in output directory'

    def decode(self,key,*arg,**kwargs):
        if 'line' in kwargs:
            self.nbLine = kwargs['line']
        else:
            self.nbLine = self.file.height

        if self.verbose:
            print '[+] Decode methoded'
            print '[*] key : '+key
        data = ''
        j = 0
        yolo = False
        while j < self.nbLine:
            k = 0
            while k < self.file.width:
                #Get pixel of the img
                r1,g1,b1 = self.getBin(self.pixel,k,j)
                l = 0
                m = 0
                while m < len(key):
                    if l >= 3:
                        if k+1 < self.file.width:
                            k+=1
                            r1,g1,b1 = self.getBin(self.pixel,k,j)
                        else:
                            k=0
                            if j+1 < self.file.height:
                                yolo = True
                                j+=1
                                r1,g1,b1 = self.getBin(self.pixel,k,j)
                            else:
                                break
                        l=0
                    else:
                        if key[m] == '1':
                            data += r1[len(r1)-1]
                        elif key[m] == '2':
                            data += g1[len(g1)-1]
                        elif key[m] == "3":
                            data += b1[len(b1)-1]

                        l+=1
                        m+=1
                k+=1
            if not yolo:
                j+=1
            else:
                yolo = False
        decod = ''
        for i in range(0,len(data),8):
            decod += chr(int(data[i:i+8],2))
        if self.verbose:
            print 'plain text :'
        print decod
        f = open(self.outputDirectory+'/dec.'+self.extension,'w')
        f.write(decod)
        f.close()
        if self.verbose:
            print '[+] File with extracted data created in output directory'

if __name__ == '__main__':
    a = LSB(filename='seh1.png',verbose='True')
    a.open(rgb='RGB')
    a.decode('132123')
