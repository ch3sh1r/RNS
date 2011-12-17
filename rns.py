#!/usr/bin/python
#-*-coding:utf-8-*-

from __future__ import division
from itertools import izip
import numbers
import operator
import psyco
psyco.full()


__all__ = ['RNS', 'negative', 'mul', 'comparer']


def negative(a, m):
    """Negative element for element a in field Z_m.
    """
    n = a % m;
    (b, x, y, n) = (m, 1, 0, 0);
    while a != 0:
        n = int(b / a);
        (a, b, x, y) = (b - n * a, a, y - n * x, x);
    return y % m

def mul(a):
    x = 1
    for i in a:
        x *= i
    return x

def comparer(A, B):
    if A == B:
        return '='
    a = A.amrs(A.vector, A.modules, [])
    b = B.amrs(B.vector, B.modules, [])
    for i in range(len(a)):
        if a[i] > b[i]:
            return '>'
        elif a[i] < b[i]:
            return '<'

class RNS(numbers.Number):
    """This class represents numbers in residue number system (RNS).
    """

    __slots__ = ('_vector', '_modules')

    def __new__(cls, number = 0, modules = ()):
        """Constructs an RNS number.
        When executing like this: GCD(X, Y), possible arguments types are:
            * Both X and Y are integer. Then we get GCD representation
              in system with Y limit;
            * When X is integer and Y is tuple or list. Then we get X
              representation in system of Y modules;
            * Finally, when X and Y are tuple or list. Then we generate GCD
              object with X vector and Y modules without any verification.
        """
        self = super(RNS, cls).__new__(cls)
        if type(number) in (int, long):
            if type(modules) is int:
                self.generate_modules(modules)
            elif type(modules) in (tuple, list) and len(modules) > 0:
                representation = [number % m for m in modules]
                self._vector = representation
                self._modules = modules
                return self
        elif type(number) in (tuple, list) and len(number) == len(modules):
            self._vector = number
            self._modules = modules
            return self

    @property
    def vector(a):
        return a._vector

    @property
    def modules(a):
        return a._modules

    @classmethod
    def decimal(self, vector, modules):
        """Garner algorithm:
        Converts an RNS number to a decimal number.
        """
        c = {}
        for i in range(2, len(modules) + 1):
            c[i] = 1
            for j in range(1, i):
                u = negative(modules[j - 1], modules[i - 1])
                c[i] = (c[i] * u) % modules[i - 1]
        x = u = vector[0]
        for i in range(2, len(modules) + 1):
            u = ((vector[i - 1] - x) * c[i]) % modules[i - 1]
            x = x + u * mul(modules[:i - 1])
        return x

    @classmethod
    def amrs(self, vector, modules, result = []):
        """Convention to the associated mixed radix system.
        """
        if vector:
            a1 = vector[0]
            result.append(a1)
            Ai = [(a - a1) for a in vector[1:]]
            Mn = [negative(modules[0], m) for m in modules[1:]]
            Aj = [(a*m)%mi for (a,m,mi) in izip(Ai,Mn,modules[1:])]
            return self.amrs(Aj, modules[1:], result)
        else:
            result.reverse()
            return result

    @classmethod
    def generate_modules(self, system_limit):
        """Generates modules with system_limit coverage.
        """
        numbers = range(3, system_limit, 2)
        mroot = system_limit ** 0.5
        half = len(numbers)
        i = 0
        m = 3
        while m <= mroot:
            if numbers[i]:
              j = (m ** 2 - 3) // 2
              numbers[j] = 0
              while j < half:
                numbers[j] = 0
                j += m
            i += 1
            m = 2 * i + 3
        coprimes = [x for x in numbers if x]
        i = 0
        m = 1
        while m <= system_limit:
            m *= coprimes[i]
            i += 1
        self._modules = coprimes[:i]

    def __repr__(self):
        """repr(self)"""
        return '[ ' + ''.join('(%d mod %d) ' % (x, y)
            for (x, y) in izip(self._vector, self._modules)) + ']'

    def __str__(self):
        """str(self)"""
        return 'RNS_number [ ' + str(self._vector) + ', ' + str(self._modules) + ' ]'

    def _add(a, b):
        """a + b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("can't operate with numbers in different modular systems.")
        return RNS([(x + y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    def _sub(a, b):
        """a - b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("can't operate with numbers in different modular systems.")
        return RNS([(x - y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    def _mul(a, b):
        """a * b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("can't operate with numbers in different modular systems.")
        return RNS([(x * y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    def _div(a, b):
        """a / b"""
        raise NotImplemented

    def __hash__(self):
        """hash(self)"""
        return hash((self._vector, self._modules))

    def __nonzero__(a):
        """a != 0"""
        return (a._vector == [0 for i in range(0, len(a._vector))])

    def __eq__(a, b):
        """a == b"""
        if isinstance(b, RNS):
            return (a._vector == b.vector and a._modules == b.modules)

    def __lt__(a, b):
        """a < b"""
        if isinstance(b, RNS):
            if comparer(a, b) == '<':
                return True
            else:
                return False

    def __gt__(a, b):
        """a > b"""
        if isinstance(b, RNS):
            if comparer(a, b) == '>':
                return True
            else:
                return False

    def __le__(a, b):
        """a <= b"""
        if isinstance(b, RNS):
            if a == b or a < b:
                return True
            else:
                return False

    def __ge__(a, b):
        """a >= b"""
        if isinstance(b, RNS):
            if a == b or a > b:
                return True
            else:
                return False

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """Generates forward and reverse operators given a purely-rational
        operator and a function from the operator module.
        """
        def forward(a, b):
            if isinstance(b, (int, long, RNS)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, (int, long, RNS)):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, numbers.Real):
                return fallback_operator(float(a), float(b))
            elif isinstance(a, numbers.Complex):
                return fallback_operator(complex(a), complex(b))
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__
        return forward, reverse

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)
    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)
    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == RNS:
            return self
        return self.__class__(self._vector, self._modules)

    def __deepcopy__(self, memo):
        if type(self) == RNS:
            return self
        return self.__class__(self._vector, self._modules)

