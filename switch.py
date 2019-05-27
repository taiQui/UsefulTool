#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from os import system

arg1 = argv[1].split('.')[0]
system('rm -f /usr/local/bin/'+arg1)
system('cp '+argv[1]+' /usr/local/bin/'+arg1)
system('chmod +x /usr/local/bin/'+arg1)
