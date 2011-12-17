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
    down = RNS(1, modules)
    for n in s:
        rns = RNS(n, modules)
        x.append(rns)
        down *= rns
    if down.vector[3] == 0:
        up = x[1] * x[2] * x[3] * x[4] * x[5] * x[6] + \
             x[0] * x[2] * x[3] * x[4] * x[5] * x[6] + \
             x[0] * x[1] * x[3] * x[4] * x[5] * x[6] + \
             x[0] * x[1] * x[2] * x[4] * x[5] * x[6] + \
             x[0] * x[1] * x[2] * x[3] * x[5] * x[6] + \
             x[0] * x[1] * x[2] * x[3] * x[4] * x[6] + \
             x[0] * x[1] * x[2] * x[3] * x[4] * x[5]
        up *= RNS(7, modules)
        down *= RNS(6, modules)
        if down == up:
            return True
    else:
        return False

def dump(X, log, interrupt = False):
    message = '%d %d %d %d %d %d %d' % (X[0], X[1], X[2], X[3], X[4], X[5], X[6])
    if interrupt:
        print
        print '^C peressed. Dumping...'
        message = '  Last sample was: ' + message
        print message
        log.write(str(message) + '\n')
        log.close()
    else:
        print message
        log.write(str(message) + '\n')

def debug(array):
    print array[:-2],
    print '%d/%d' % (array[-2], array[-1])

def margin(last, n, d):
    neo = 7 * d / (6 * d - 7 * n)
    if neo < last:
        return last
    return neo

log = file('result_semi.txt', 'w')
try:
    for x1 in range(2, 9):

        x2 = x1 - 1
        x2 = margin(x1, 1, x1)
        while x2 < 18:
            x2 += 1
            numerator2 = x1 + x2
            denominator2 = x1 * x2
            debug([x1, x2, numerator2, denominator2])
            if 7 * numerator2 < 6 * denominator2:

                x3 = margin(x2, numerator2, denominator2)
                while x3 < 36:
                    x3 += 1
                    numerator3 = numerator2 * x3 + denominator2
                    denominator3 = denominator2 * x3
                    debug([x1, x2, x3, numerator3, denominator3])
                    if 7 * numerator3 < 6 * denominator3:

                        x4 = margin(x3, numerator3, denominator3)
                        while x4 < 561:
                            x4 += 1
                            numerator4 = numerator3 * x4 + denominator3
                            denominator4 = denominator3 * x4
                            debug([x1, x2, x3, x4, numerator4, denominator4])
                            if 7 * numerator4 < 6 * denominator4:

                                x5 = margin(x4, numerator4, denominator4)
                                while x5 < 59221:
                                    x5 += 1
                                    numerator5 = numerator4 * x5 + denominator4
                                    denominator5 = denominator4 * x5
                                    debug([x1, x2, x3, x4, x5, numerator5, denominator5])
                                    if 7 * numerator5 < 6 * denominator5:

                                        x6 = margin(x5, numerator5, denominator5)
                                        while x6 < 779347981:
                                            x6 += 1
                                            numerator6 = numerator5 * x6 + denominator5
                                            denominator6 = denominator5 * x6
                                            debug([x1, x2, x3, x4, x5, x6, numerator6, denominator6])
                                            if 7 * numerator6 < 6 * denominator6:

                                                x7 = margin(x6, numerator6, denominator6)
                                                numerator7 = numerator6 * x7 + denominator6
                                                denominator7 = denominator6 * x7
                                                debug([x1, x2, x3, x4, x5, x6, x7, numerator7, denominator7])
                                                if 7 * numerator7 == 6 * denominator7:
                                                    dump([x1, x2, x3, x4, x5, x6, x7], log)
                                                elif 7 * numerator7 > 6 * denominator7:
                                                    break

except KeyboardInterrupt:
    dump([x1, x2, x3, x4, x5, x6, x7], log, True)

