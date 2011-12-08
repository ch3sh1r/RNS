#!/usr/bin/python
#-*-coding:utf-8-*-

import rns

a = rns.RNS(4, (3, 5))
b = rns.RNS(1, (3, 5))
a.generate_modules(1000)
print a.modules

