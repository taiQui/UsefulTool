#!/usr/bin/env python

import sys
import os
import platform
#ARG 1 : type
#       - search file
#       - count file   + extension ou pas
#       -

list = []
if platform.system() == "Linux":
    PATH = "/home"
elif platform.system() == "Windows":
    PATH = "C:\\User"
else:
    print 'FUCK YOU WITH YOUR MAC OR OTHER SHIT'
    sys.exit()


def help():
    print '#------------------------------------------------------------------------------'
    print '# search [PartielNameOfFile]'
    print '# dirtool search hello.txt'
    print '# count [extension {.pdf - .txt ...} | name ] [path of occurency where found yes/no]'
    print '# dirtool count .pdf'
    print '# default path = \'/home\''
    print '#------------------------------------------------------------------------------'

def inspect(files):
    for path,dir,file in os.walk(PATH):
        for i in file:
            if files in i:
                list.append((i,path))

def count(arg,bool):
    count = 0
    for path,dir,file in os.walk(PATH):
        for i in file:
            if arg[0]=='.':
                if '.'  in i:
                    if i.split('.')[1] == arg.split('.')[1]:
                        if bool == True:
                            list.append(path+str(i))
                        count+=1
            elif '.' not in arg:
                if '.' in i:
                    if i.split('.')[0] == arg:
                        if bool == True:
                            list.append(path+str(i))
                        count+=1
                else:
                    if i == arg:
                        if bool == True:
                            list.append(path+str(i))
                        count+=1
            else:
                if i == arg:
                    if bool == True:
                        list.append(path+str(i))
                    count +=1
    return count




if len(sys.argv) <= 1:
    help()
    sys.exit()
print 'You are on '+str(platform.system())+' machine\n'
ch = raw_input("Enter your path - default \'/home\'\n")
if ch != "":
    PATH = ch
print "executing..."
if sys.argv[1] == "search":
    if len(sys.argv)<=1:
        print 'Miss name of file\n'
        sys.exit()
    inspect(sys.argv[2])
    for i,j in list:
        print 'found '+str(i)+' at '+str(j)+'\n'
    print 'we found '+str(len(list))+' element for '+str(sys.argv[2])
elif sys.argv[1] == "count":
    if len(sys.argv) <= 1:
        print 'Miss name or file\'s extension'
        sys.exit()
    if len(sys.argv) == 4:
        compt = count(sys.argv[2],True)
        for i in list:
            print ' at '+str(i)+'\n'
        print 'We found '+str(compt)+' times \''+sys.argv[2]+'\''
    else:
        compt = count(sys.argv[2],False)
        print 'We found '+str(compt)+' times \''+sys.argv[2]+'\''
elif sys.argv[1] == 'help':
    help()
    sys.exit()
