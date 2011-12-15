#!/usr/bin/python
#-*-coding:utf-8-*-

from rns import RNS
import psyco
psyco.full()

def check(s):
    x = []
    modules = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
               31, 37, 41, 43, 47, 53, 59, 61, 67,
               71, 73, 79, 83, 89, 97, 101]
    up = RNS(0, modules)
    down = RNS(1, modules)
    for n in s:
        x.append(RNS(n, modules))
    for n in x:
        down *= n
    up = x[1] * x[2] * x[3] * x[4] * x[5] * x[6] + \
         x[0] * x[2] * x[3] * x[4] * x[5] * x[6] + \
         x[0] * x[1] * x[3] * x[4] * x[5] * x[6] + \
         x[0] * x[1] * x[2] * x[4] * x[5] * x[6] + \
         x[0] * x[1] * x[2] * x[3] * x[5] * x[6] + \
         x[0] * x[1] * x[2] * x[3] * x[4] * x[6] + \
         x[0] * x[1] * x[2] * x[3] * x[4] * x[5]
    if down.vector[3] != 0:
        return False
    up *= RNS(7, modules)
    down *= RNS(6, modules)
    if down != up:
        return False
    return True

log = file('semi.txt', 'w')
try:
    for x1 in xrange(2, 9):
        for x2 in xrange(3, 18):
            if x2 >= x1:
                for x3 in xrange(4, 36):
                    if x3 >= x2:
                        for x4 in xrange(5, 561):
                            if x4 >= x3:
                                for x5 in xrange(6, 59221):
                                    if x5 >= x4:
                                        x6 = 6
                                        while 6 <= x6 <=  779347980:
                                            x6 += 1
                                            if x6 >= x5:
                                                x7 = 7
                                                while 7 <= x7 <= 151856223345962940:
                                                    x7 += 1
                                                    if x7 >= x6:
                                                        sample = [x1, x2, x3, x4, x5, x6, x7]
                                                        if check(sample):
                                                            print str(sample)
                                                            log.write(str((sample)) + "\n")
except KeyboardInterrupt:
    log.write('\n Last sample was: ' + str(sample) + '\n')
    log.close()

