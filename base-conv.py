#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import *
from sys import argv,exit
# VAR --------------------
f_value = ''
manual = False
base = 'none'
verbose = False
#-------------------------
fullcmd = []

def help():
    print '---------------------'
    print ' base-conv [-f : file] [-d : manualEntry] [-b : base]'
    print ' Known base : 85 - 64 - 32 - 16 '
    print '---------------------'

for i in range(1,len(argv)):
    fullcmd.append(argv[i])

# if len(fullcmd) < 2:
#     help()
#     exit()

try:
    if "-f" in fullcmd:
        if fullcmd[fullcmd.index('-f')+1][0] != '-':
            f_value = fullcmd[fullcmd.index('-f')+1]
        else :
            print '[-] bad file given'
            help()
            exit()
except:
    print '[-] Error -f'
    exit()

if "-d" in fullcmd:
    manual = True

if "-b" in fullcmd:
    if fullcmd[fullcmd.index('-b')+1][0] != '-':
        if fullcmd[fullcmd.index('-b')+1].isdigit():
            base = fullcmd[fullcmd.index('-b')+1]
        else:
            print '[-] Error NaN erro for argument -b'
            exit()
    else:
        print '[-] Error value for argument -b'
        exit()


if manual:
    text = raw_input()
    if base == "none":
        try:
            print '[*] Base 85 : '+ a85decode(text)
        except:
            print 'sexe'
        try:
            print '[*] Base 64 : '+ b64decode(text)
        except:
            pass
        try:
            print '[*] Base 32 : '+ b32decode(text)
        except:
            pass
        try:
            print '[*] Base 16 : '+ b16decode(text)
        except:
            pass
    else:
        if base == '85':
            try:
                print '[*] Base 85 : '+ a85decode(text)
            except:
                print '[-] Error decoding'
        elif base == '64':
            try:
                print '[*] Base 64 : '+ b64decode(text)
            except:
                pass
        elif base == '32':
            try:
                print '[*] Base 32 : '+ b32decode(text)
            except:
                pass
        elif base == '16':
            try:
                print '[*] Base 16 : '+ b16decode(text)
            except:
                pass
else:
    file = open(f_value)
    text = file.read()
    text = text.split('\n')
    print text
    for i in text:
        if base == "none":
            try:
                print '[*] Base 85 : '+ a85decode(i)
            except:
                print 'sexe'
            try:
                print '[*] Base 64 : '+ b64decode(i)
            except:
                pass
            try:
                print '[*] Base 32 : '+ b32decode(i)
            except:
                pass
            try:
                print '[*] Base 16 : '+ b16decode(i)
            except:
                pass
        else:
            if base == '85':
                try:
                    print '[*] Base 85 : '+ a85decode(i)
                except:
                    print '[-] Error decoding'
            elif base == '64':
                try:
                    print '[*] Base 64 : '+ b64decode(i)
                except:
                    pass
            elif base == '32':
                try:
                    print '[*] Base 32 : '+ b32decode(i)
                except:
                    pass
            elif base == '16':
                try:
                    print '[*] Base 16 : '+ b16decode(i)
                except:
                    pass
