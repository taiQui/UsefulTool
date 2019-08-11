#!/usr/bin/env python
# coding:utf-8
from PIL import Image
from sys import exit
import argparse

one = "1"
zero = "0"

def createQR(text,nb,args):
    h,w = getsquare(text)
    img = Image.new('RGB',(h,w),color="white")
    pix = img.load()
    text = text.split('\n')[:h]
    if args.verbose:
        print "[+] Square number "+str(nb)
        print "[+]      Creating new picture to store pixel"
        print "[+]      Height : "+str(h)
        print "[+]      Weight : "+str(w)
    for i in range(h):
        for j in range(w):
            if text[i][j] == one:
                pix[j,i] = (0,0,0)
            elif text[i][j] == zero:
                pix[j,i] = (255,255,255)
    img.save(args.output+str(nb)+".png")
    if args.verbose:
        print "[+]      Image save \""+args.output+str(nb)+".png\""
    else:
        print "[+] Image save \""+args.output+str(nb)+".png\""
def getsquare(arg):
    j = 0
    for i in arg.split('\n'):
        if one in i or zero in i:
            j+=1
        else:
            break
    return j,len(arg.split('\n')[0])
def main(args):
    if args.verbose:
        one = args.one
        zero = args.zero
        print "[+] Binary 1 => "+str(one)
        print "[+] Binary 0 => "+str(zero)
        print "[+] Opening file"
    file = open(args.filename,'r')
    text = file.read()
    liste = []
    if args.big:
        max = 1000
    else:
        max = 100
    for i in range(2,max):
        tmp = ""
        for j in [text[k:k+len(text)/i] for k in range(0,len(text),len(text)/i)]:
            tmp += j+"\n"
        a,b = getsquare(tmp)
        if a == b:
            if args.verbose:
                print "[+] Square found !"
            liste.append(tmp)
    if len(liste) == 0:
        print "[-] No square found"
        exit()
    for i in range(len(liste)):
        createQR(liste[i],i,args)

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',help="The filename to read",required=True)
    parser.add_argument('-o','--output',help="The output to store resultat",default="qr")
    parser.add_argument('-v','--verbose',help="Give more output",action="store_true")
    parser.add_argument('-1','--one',help="The format of 1",default="1")
    parser.add_argument('-0','--zero',help="The format of 0",default="0")
    parser.add_argument('-b','--big',help="If the file is big",action="store_true")
    return parser.parse_args()

if __name__ == "__main__":
    args = setup()
    main(args)
