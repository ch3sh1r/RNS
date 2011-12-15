#!/usr/bin/python
#-*-coding:utf-8-*-

from rns import RNS
import psyco
psyco.full()

log = file('rns.txt', 'w')
modules = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
           31, 37, 41, 43, 47, 53, 59, 61, 67,
           71, 73, 79, 83, 89, 97, 101]
e = RNS(1, modules)
p = RNS(6, modules)
q = RNS(7, modules)
ranges = [RNS(9, modules),
          RNS(18, modules),
          RNS(36, modules),
          RNS(561, modules),
          RNS(59221, modules),
          RNS(779347981, modules),
          RNS(151856223345962941, modules)]
try:
    x1 = RNS(1, modules)
    while x1 <= ranges[0]:
        x1 += e
        numerator = e
        denominator = x1

        x2 = RNS(2, modules)
        while x2 < ranges[1]:
            x2 += e
            numerator = x1 + x2
            denominator = x1 * x2
            if x2 >= x1:

                x3 = RNS(3, modules)
                while x3 < ranges[2]:
                    x3 += e
                    numerator = numerator * x3 + denominator
                    denominator *= x3
                    if x3 >= x2 and q * numerator < p * denominator:

                        x4 = RNS(4, modules)
                        while x4 < ranges[3]:
                            x4 += e
                            numerator = numerator * x4 + denominator
                            denominator *= x4
                            if x4 >= x3 and q * numerator < p * denominator:

                                x5 = RNS(5, modules)
                                while x5 < ranges[4]:
                                    x5 += e
                                    numerator = numerator * x5 + denominator
                                    denominator *= x5
                                    if x5 >= x4 and q * numerator < p * denominator:

                                        x6 = RNS(6, modules)
                                        while x6 < ranges[5]:
                                            x6 += e
                                            numerator = numerator * x6 + denominator
                                            denominator *= x6
                                            if x6 >= x5 and q * numerator < p * denominator:

                                                x7 = RNS(7, modules)
                                                while x7 < ranges[6]:
                                                    x7 += e
                                                    numerator = numerator * x7 + denominator
                                                    denominator *= x7
                                                    if x7 >= x6 and q * numerator == p * denominator:
                                                        [x.to_decimal(x.vector, x.modules) for x
                                                                  in [x1, x2, x3, x4, x5, x6, x7]]
                                                        sample = [x.decimal for x
                                                                  in [x1, x2, x3, x4, x5, x6, x7]]
                                                        print str(sample)
                                                        log.write(str((sample)) + "\n")
except KeyboardInterrupt:
    [x.to_decimal(x.vector, x.modules) for x in [x1, x2, x3, x4, x5, x6, x7]]
    sample = [x.decimal for x in [x1, x2, x3, x4, x5, x6, x7]]
    log.write('\n Last sample was: ' + str(sample) + '\n')
    log.close()

