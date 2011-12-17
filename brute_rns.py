#!/usr/bin/python
#-*-coding:utf-8-*-

from rns import RNS
import psyco
psyco.full()

modules = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
           31, 37, 41, 43, 47, 53, 59, 61, 67,
           71, 73, 79, 83, 89, 97, 101, 103]
ranges = [RNS(9, modules),
          RNS(18, modules),
          RNS(36, modules),
          RNS(561, modules),
          RNS(59221, modules),
          RNS(779347981, modules),
          RNS(151856223345962941, modules)]
e = RNS(1, modules)
p = RNS(6, modules)
q = RNS(7, modules)

def dump(i, X, log, interrupt = False):
    s = [x.decimal(x.vector, x.modules) for x in X]
    message = '%d. %d %d %d %d %d %d %d' % (i, s[0], s[1], s[2], s[3], s[4], s[5], s[6])
    if interrupt:
        print
        print '^C peressed. Dumping...'
        message = '  Last sample was: ' + message
        print message
        log.write(str(message) + '\n')
        log.close()
    else:
        print message
        log.write(message + '\n')

def debug(X, d, n):
    for x in X:
        print x.decimal(x.vector, x.modules),
    n = n.decimal(n.vector, n.modules)
    d = d.decimal(d.vector, d.modules)
    print '(%d < %d) => %d/%d < 6/7' % (n * 7, 6 * d, n, d)
    print

def margin(last, n, d):
    neo = q * d / (p * d - q * n)
    if neo < last:
        return last
    return neo

i = 0
log = file('result_rns.txt', 'w')
try:
    x1 = RNS(3, modules)
    while x1 <= ranges[0]:
        x1 += e

        x2 = margin(x1, e, x1)
        while x2 < ranges[1]:
            x2 += e
            numerator2 = x1 + x2
            denominator2 = x1 * x2
            debug([x1,x2],numerator2,denominator2)
            if x2 >= x1:

                x3 = margin(x2, numerator2, denominator2)
                while x3 < ranges[2]:
                    x3 += e
                    numerator3 = numerator2 * x3 + denominator2
                    denominator3 = denominator2 * x3
                    debug([x1,x2,x3],numerator3,denominator3)
                    if q * numerator3 < p * denominator3:

                        x4 = margin(x3, numerator3, denominator3)
                        while x4 < ranges[3]:
                            x4 += e
                            numerator4 = numerator3 * x4 + denominator3
                            denominator4 = denominator3 * x4
                            debug([x1,x2,x3,x4],numerator4,denominator4)
                            if q * numerator4 < p * denominator4:

                                x5 = margin(x4, numerator4, denominator4)
                                while x5 < ranges[4]:
                                    x5 += e
                                    numerator5 = numerator4 * x5 + denominator4
                                    denominator5 = denominator4 * x5
                                    debug([x1,x2,x3,x4,x5],numerator5,denominator5)
                                    if q * numerator5 < p * denominator5:

                                        x6 = margin(x5, numerator5, denominator5)
                                        while x6 < ranges[5]:
                                            x6 += e
                                            numerator6 = numerator5 * x6 + denominator5
                                            denominator6 = denominator5 * x6
                                            debug([x1,x2,x3,x4,x5,x6],numerator6,denominator6)
                                            if q * numerator6 < p * denominator6:

                                                x7 = margin(x6, numerator6, denominator6)
                                                numerator7 = numerator6 * x7 + denominator6
                                                denominator7 = denominator6 * x7
                                                debug([x1,x2,x3,x4,x5,x6,x7],numerator7,denominator7)
                                                if denominator7.modules[3] == 0:
                                                    if q * numerator7 == p * denominator7:
                                                        dump(i, [x1, x2, x3, x4, x5, x6, x7], log)
                                                        i += 1
                                                        break
except KeyboardInterrupt:
    dump(i, [x1, x2, x3, x4, x5, x6, x7], log, True)

