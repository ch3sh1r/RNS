#!/usr/bin/python
#-*-coding:utf-8-*-

from rns import RNS
import psyco
psyco.full()

def dump(i, X, log, interrupt = False):
    s = [x.decimal for x in X]
    message = '%d %d %d %d %d %d %d' % (s[0], s[1], s[2], s[3], s[4], s[5], s[6])
    if interrupt:
        print
        print '^C peressed. Dumping...'
        message = '  Last sample was: ' + message
        print message
        log.write(str(message) + '\n')
        log.close()
    else:
        print str(i) + '. ' + message
        log.write(str(message) + '\n')

def debug(array):
    array = [x.decimal for x in array]
    print array[:-2],
    print '%d/%d' % (array[-2], array[-1])

def margin(last, n, d):
    neo = q * d / (p * d - q * n)
    if neo < last:
        return last
    return neo

modules = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
           31, 37, 41, 43, 47, 53, 59, 61, 67,
           71, 73, 79, 83, 89, 97, 101, 103]
e = RNS(1, modules)
p = RNS(6, modules)
q = RNS(7, modules)
i = 1

log = file('result_rns.txt', 'w')
try:
    x1 = RNS(1, modules)
    while x1 <= RNS(9, modules):
        x1 += e

        x2 = margin(x1, e, x1)
        m1 = x2 * p
        while x2 < m1:
            x2 += e
            numerator2 = x1 + x2
            denominator2 = x1 * x2
            #debug([x1, x2, numerator2, denominator2])
            if q * numerator2 < p * denominator2:

                x3 = margin(x2, numerator2, denominator2)
                m2 = x3 * RNS(5, modules)
                while x3 < m2:
                    x3 += e
                    numerator3 = numerator2 * x3 + denominator2
                    denominator3 = denominator2 * x3
                    #debug([x1, x2, x3, numerator3, denominator3])
                    if q * numerator3 < p * denominator3:

                        x4 = margin(x3, numerator3, denominator3)
                        m3 = x4 * RNS(4, modules)
                        while x4 < m3:
                            x4 += e
                            numerator4 = numerator3 * x4 + denominator3
                            denominator4 = denominator3 * x4
                            #debug([x1, x2, x3, x4, numerator4, denominator4])
                            if q * numerator4 < p * denominator4:

                                x5 = margin(x4, numerator4, denominator4)
                                m4 = x5 * RNS(3, modules)
                                while x5 < m4:
                                    x5 += e
                                    numerator5 = numerator4 * x5 + denominator4
                                    denominator5 = denominator4 * x5
                                    #debug([x1, x2, x3, x4, x5, numerator5, denominator5])
                                    if q * numerator5 < p * denominator5:

                                        x6 = margin(x5, numerator5, denominator5)
                                        m5 = x6 * RNS(2, modules)
                                        while x6 < m5:
                                            x6 += e
                                            numerator6 = numerator5 * x6 + denominator5
                                            denominator6 = denominator5 * x6
                                            #debug([x1, x2, x3, x4, x5, x6, numerator6, denominator6])
                                            if q * numerator6 < p * denominator6:

                                                x7 = margin(x6, numerator6, denominator6)
                                                numerator7 = numerator6 * x7 + denominator6
                                                denominator7 = denominator6 * x7
                                                #debug([x1, x2, x3, x4, x5, x6, x7, numerator7, denominator7])
                                                if q * numerator7 == p * denominator7:
                                                    dump(i, [x1, x2, x3, x4, x5, x6, x7], log)
                                                    i += 1

except KeyboardInterrupt:
    dump(i, [x1, x2, x3, x4, x5, x6, x7], log, True)

