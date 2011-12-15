#!/usr/bin/python
#-*-coding:utf-8-*-

from fractions import Fraction
import psyco
psyco.full()

log = file('fractions.txt', 'w')
m = Fraction()
try:
    for x1 in xrange(2, 9):
        a = Fraction(1, x1)

        for x2 in xrange(3, 18):
            if x2 >= x1:
                b = a + Fraction(1, x2)
                if b < Fraction(6,7):

                    for x3 in xrange(4, 36):
                        if x3 >= x2:
                            c = b + Fraction(1, x3)
                            if c < Fraction(6,7):

                                for x4 in xrange(5, 561):
                                    if x4 >= x3:
                                        d = c + Fraction(1, x4)
                                        if d < Fraction(6,7):

                                            for x5 in xrange(6, 59221):
                                                if x5 >= x4:
                                                    e = d + Fraction(1, x5)
                                                    x6 = 6

                                                    while 6 <= x6 <=  779347980:
                                                        x6 += 1
                                                        if x6 >= x5:
                                                            f = e + Fraction(1, x6)
                                                            x7 = 7

                                                            while 7 <= x7 <= 151856223345962940:
                                                                x7 += 1
                                                                if x7 >= x6:
                                                                    g = f + Fraction(1, x7)
                                                                    sample = [x1, x2, x3, x4, x5, x6, x7]

                                                                    if g == Fraction(6,7):
                                                                        print (sample)
                                                                        log.write(str(sample) + "\n")
except KeyboardInterrupt:
    log.write('\n Last sample was: ' + str(sample) + '\n')
    log.close()

