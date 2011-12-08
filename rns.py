from __future__ import division
from itertools import izip
import numbers
import operator

__all__ = ['RNS']

class RNS(numbers.Number):
    """This class represents numbers in residue number system (RNS)."""

    __slots__ = ('_vector', '_modules')

    # We're immutable, so use __new__ not __init__
    def __new__(cls, number = 0, modules = ()):
        """Constructs an RNS number."""
        self = super(RNS, cls).__new__(cls)
        if type(number) in (int, long) and len(modules) > 0:
            representation = [number % m for m in modules]
            self._vector = representation
            self._modules = modules
            return self
        elif type(number) is list and len(number) == len(modules):
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
    def to_decimal(cls, f):
        """Converts an RNS number to a decimail number, exactly."""

    def __repr__(self):
        """repr(self)"""
        return 'RNS_number [ ' + str(self._vector) + ', ' + str(self._modules) + ' ]'

    def __str__(self):
        """str(self)"""
        return '[ ' + ''.join('(%d mod %d) ' % (x, y)
            for (x, y) in izip(self._vector, self._modules)) + ']'

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """Generates forward and reverse operators given a purely-rational
        operator and a function from the operator module."""
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

    def _add(a, b):
        """a + b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("Cannot operate with numbers in different modular systems.")
        return RNS([(x + y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        """a - b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("Cannot operate with numbers in different modular systems.")
        return RNS([(x - y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        """a * b"""
        if a.modules != b.modules or len(a.vector) != len(b.vector):
            raise TypeError("Cannot operate with numbers in different modular systems.")
        return RNS([(x * y) % m for (x, y, m) in izip(a.vector, b.vector, a.modules)], a.modules)

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        """a / b"""

    def __hash__(self):
        """hash(self)"""
        return hash((self._vector, self._modules))

    def __eq__(a, b):
        """a == b"""
        if isinstance(b, RNS):
            return (a._vector == b.vector and a._modules == b.modules)

    def __lt__(a, b):
        """a < b"""

    def __gt__(a, b):
        """a > b"""

    def __le__(a, b):
        """a <= b"""

    def __ge__(a, b):
        """a >= b"""

    def __nonzero__(a):
        """a != 0"""

    # support for pickling, copy, and deepcopy
    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == RNS:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._vector, self._modules)

    def __deepcopy__(self, memo):
        if type(self) == RNS:
            return self     # My components are also immutable
        return self.__class__(self._vector, self._modules)

