# partial unit test for gmpy/decimal interoperability
# relies on Tim Peters' "doctest.py" test-driver
r'''
>>> dir(f)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '_copy', 'acos', 'acosh', 'add', 'agm', 'ai', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'binary', 'cbrt', 'ceil', 'check_range', 'cos', 'cosh', 'cot', 'coth', 'csc', 'csch', 'digamma', 'digits', 'div', 'eint', 'erf', 'erfc', 'exp', 'exp10', 'exp2', 'expm1', 'f2q', 'floor', 'fmod', 'frac', 'gamma', 'hypot', 'is_inf', 'is_integer', 'is_lessgreater', 'is_nan', 'is_number', 'is_regular', 'is_unordered', 'is_zero', 'j0', 'j1', 'jn', 'lgamma', 'li2', 'lngamma', 'log', 'log10', 'log1p', 'log2', 'max', 'min', 'modf', 'mul', 'next_above', 'next_below', 'next_toward', 'pow', 'precision', 'qdiv', 'rc', 'rec_sqrt', 'reldiff', 'remainder', 'remquo', 'rint', 'rint_ceil', 'rint_floor', 'rint_round', 'rint_trunc', 'root', 'round', 'round2', 'sec', 'sech', 'sign', 'sin', 'sin_cos', 'sinh', 'sinh_cosh', 'sqrt', 'square', 'sub', 'tan', 'tanh', 'trunc', 'y0', 'y1', 'yn', 'zeta']
>>>
'''
try: import decimal as _d
except ImportError: _d = None

import gmpy2 as _g, doctest, sys
__test__={}
f=_g.mpfr('123.456')
q=_g.mpq('789123/1000')
z=_g.mpz('234')
if _d:
    d=_d.Decimal('12.34')
    fd=_d.Decimal('123.456')
    qd=_d.Decimal('789.123')
    zd=_d.Decimal('234')

__test__['compat']=\
r'''
>>> f == fd
True
>>> fd == f
True
>>> q == qd
True
>>> qd == q
True
>>> z == zd
True
>>> zd == z
True
>>> f > d
True
>>> d > f
False
'''


__test__['elemop']=\
r'''
>>> print(_g.mpz(23) == _d.Decimal(23))
True
>>> print(_g.mpz(d))
12
>>> print(_g.mpq(d))
617/50
>>> print(_g.mpfr(d))
12.34
>>> print(f+d)
135.79599999999999
>>> print(d+f)
135.79599999999999
>>> print(q+d)
801.46300000000008
>>> print(d+q)
801.46300000000008
>>> print(z+d)
246.34
>>> print(d+z)
246.34
>>> print(_g.ceil(d))
13.0
>>> print(_g.floor(d))
12.0
>>> print(_g.trunc(d))
12.0
>>> _g.mpfr(d).precision
53
>>> _g.sqrt(d)==_g.mpfr(d).sqrt()
1
>>>
'''

def _test(chat=None):
    if chat:
        print("Unit tests for gmpy2 (decimal interoperation)")
        print("    on Python %s" % sys.version)
        print("Testing gmpy2 {0}".format(_g.version()))
        print("  Mutliple-precision library:   {0}".format(_g.mp_version()))
        print("  Floating-point library:       {0}".format(_g.mpfr_version()))
        print("  Complex library:              {0}".format(_g.mpc_version()))
        print("  Caching Values: (Number)      {0}".format(_g.get_cache()[0]))
        print("  Caching Values: (Size, limbs) {0}".format(_g.get_cache()[1]))
    if not _d:
        if chat:
            print("Can't test, since can't import decimal")
        return 0, 0
    thismod = sys.modules.get(__name__)
    doctest.testmod(thismod, report=0)

    if chat:
        print()
        print("Overall results for dec:")
    return doctest.master.summarize(chat)

if __name__=='__main__':
    _test(1)
