#!/usr/bin/python
#-*-coding:utf-8-*-

import psyco
psyco.full()

def dump(i, X, log, interrupt = False):
    message = '%d %d %d %d %d %d %d' % (X[0], X[1], X[2], X[3], X[4], X[5], X[6])
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
    print array[:-2],
    print '%d/%d' % (array[-2], array[-1])

def margin(last, n, d):
    neo = 7 * d / (6 * d - 7 * n)
    if neo < last:
        return last
    return neo

log = file('result_int.txt', 'w')
i = 0
try:
    for x1 in range(2, 9):

        x2 = margin(x1, 1, x1)
        m1 = x2 * 6
        while x2 < m1:#18:
            x2 += 1
            numerator2 = x1 + x2
            denominator2 = x1 * x2
            #debug([x1, x2, numerator2, denominator2])
            if 7 * numerator2 < 6 * denominator2:

                x3 = margin(x2, numerator2, denominator2)
                m2 = x3 * 5
                while x3 < m2:#36:
                    x3 += 1
                    numerator3 = numerator2 * x3 + denominator2
                    denominator3 = denominator2 * x3
                    #debug([x1, x2, x3, numerator3, denominator3])
                    if 7 * numerator3 < 6 * denominator3:

                        x4 = margin(x3, numerator3, denominator3)
                        m3 = x4 * 4
                        while x4 < m3:#561:
                            x4 += 1
                            numerator4 = numerator3 * x4 + denominator3
                            denominator4 = denominator3 * x4
                            #debug([x1, x2, x3, x4, numerator4, denominator4])
                            if 7 * numerator4 < 6 * denominator4:

                                x5 = margin(x4, numerator4, denominator4)
                                m4 = x5 * 3
                                while x5 < m4:#59221:
                                    x5 += 1
                                    numerator5 = numerator4 * x5 + denominator4
                                    denominator5 = denominator4 * x5
                                    #debug([x1, x2, x3, x4, x5, numerator5, denominator5])
                                    if 7 * numerator5 < 6 * denominator5:

                                        x6 = margin(x5, numerator5, denominator5)
                                        m5 = x6 * 2
                                        while x6 < m5:#779347981:
                                            x6 += 1
                                            numerator6 = numerator5 * x6 + denominator5
                                            denominator6 = denominator5 * x6
                                            #debug([x1, x2, x3, x4, x5, x6, numerator6, denominator6])
                                            if 7 * numerator6 < 6 * denominator6:

                                                x7 = margin(x6, numerator6, denominator6)
                                                numerator7 = numerator6 * x7 + denominator6
                                                denominator7 = denominator6 * x7
                                                #debug([x1, x2, x3, x4, x5, x6, x7, numerator7, denominator7])
                                                if 7 * numerator7 == 6 * denominator7:
                                                    dump(i, [x1, x2, x3, x4, x5, x6, x7], log)
                                                    i += 1

except KeyboardInterrupt:
    dump(i, [x1, x2, x3, x4, x5, x6, x7], log, True)

