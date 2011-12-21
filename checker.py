#!/usr/bin/python
#-*-coding:utf-8-*-

from fractions import Fraction as f

filename = 'result_int.1'
separator = ' '
p, q = 6, 7

answers = open(filename)
string = answers.readline().rstrip()
while string:
    denominators = [int(x) for x in string.split(separator)]
    fraction = 0
    for d in denominators:
        fraction += f(1, d)
    if fraction != f(p, q):
        print 'Wrong: ' + denominators
    string = answers.readline().rstrip()

