#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import argv,exit
from os import system
string = argv[1]
gennumber = 1000
if "-n" in argv:
    try:
        gennumber = int(argv[argv.index("-n")+1])
    except:
        print "error bad format"
        exit()

conv = []

for i in range(0,len(string),2):
    conv.append(string[i]+string[i+1])

conv = conv[::-1]
decod = ""
for i in range(len(conv)):
    decod += conv[i].decode('hex')

print 'found : '+decod
print 'executing gen '+str(gennumber)+" "+decod
system("gen "+str(gennumber)+" "+decod)
