#!/usr/bin/python
#-*-coding:utf-8-*-

from fractions import Fraction
import psyco
psyco.full()

m = Fraction()
for x1 in range(2, 9):
    a = Fraction(1, x1)

    for x2 in range(3, 18):
        if x2 >= x1:
            b = a + Fraction(1, x2)

            for x3 in range(4, 36):
                if b < Fraction(6,7) and x3 >= x2:
                    c = b + Fraction(1, x3)
                    if c < Fraction(6,7):

                        for x4 in range(5, 560):
                            if x4 >= x3:
                                d = c + Fraction(1, x4)
                                if d < Fraction(6,7):

                                    for x5 in range(6, 59220):
                                        if x5 >= x4:
                                            e = d + Fraction(1, x5)

                                            if m < e < Fraction(6,7):
                                                m = e
                                                print "%d %d %d %d %d with %s" % (x1, x2, x3, x4, x5, d)

