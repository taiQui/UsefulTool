#!/usr/bin/env python
#__*__coding:utf8__*__
import os
import sys

def help():
    print 'uncomp file'
    sys.exit()


def uncompress(file,ext):

    if ext == 'zip':
        print 'zip detected'
        print 'Using unzip'
        os.system('unzip '+file)
    elif ext == 'gz':
        print 'gzip detected'
        print 'Using gunzip'
        os.system('gunzip '+file)
    elif ext == 'apk':
        print 'apk detected'
        print 'using apktool'
        os.system('apktool d '+file)
    elif ext =='bz2':
        print 'bz2 detected'
        print 'using bzip2'
        os.system('bzip2 -d '+file)
    elif ext == 'tz':
        print 'tz detected'
        print 'using tar'
        os.system('tar -xvf '+file )
    elif ext == 'tar':
        print 'tar detected'
        print 'using tar'
        os.system('tar -xvf '+file)

if len(sys.argv) < 1:
    help()
    sys.exit()


File = sys.argv[1]
filename = File.split('.')[0]
extension = File.split('.')
i = len(extension)-1
while i >= 1 :
    name = ''
    for j in range(0,i+1):
        if j == i :
            name += extension[j]
        else:
            name += extension[j]+'.'
    uncompress(name,extension[i])
    i-=1
