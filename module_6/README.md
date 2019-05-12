# Numeric and Scalar types


#### int
unlimited precision Integer

#### float
double precision (64 bit)
15 to 17 bits of decimal precision.

Get info about system float implementation
```python
import sys
sys.float_info
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

```
Since integers can be unlimited in size but not floats. There can be information loss when converting int to float in Python.

Example

```python
i = 2**53
i
# 9007199254740992
float(i)
# 9007199254740992.0
i = 2**53 + 1
float(i)
# 9007199254740992.0
i = 2**53 + 2
float(i)
# 9007199254740994.0
i = 2**53 + 3
float(i)
# 9007199254740996.0
i = 2**53 + 4
float(i)
# 9007199254740996.0
```

#### decimal
Standard library module containg the class `Decimal`.
Decimal floating point. Configurable (although finite) precision. Defaults to 28 digits of decimal precision.

Get info on how Decimal is implemented for system.
```python
import decimal
decimal.getcontext()
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

```

Creating decimals. Be careful when creating Decimals from floats directly.
Always qoute literal fractional values

```python
from decimal import Decimal

Decimal("0.8") - Decimal("0.7") # Decimal('0.1')

Decimal(0.8) - Decimal(0.7) # Decimal('0.1000000000000000888178419700')

```

#### fractions
The standard library module fractions contains the `Fraction` class for rational numbers.

Example

```python
from fractions import Fraction
two_thirds = Fraction(2, 3)
two_thirds
# Fraction(2, 3)
Fraction(2, 0)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/usr/lib64/python3.7/fractions.py", line 178, in __new__
#     raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
# ZeroDivisionError: Fraction(2, 0)
Fraction(0.5)
# Fraction(1, 2)
Fraction(0.1)
# Fraction(3602879701896397, 36028797018963968)

from decimal import Decimal
Fraction(Decimal("0.1"))
Fraction(1, 10)

Fraction(2,3) * Fraction(4, 5)
# Fraction(8, 15)
```


#### complex
Built-in type `complex` for complex numbers.

Python uses the electrical engineering notation for imaginary numbers
```python
2j
# 2j
type(2j)
# <class 'complex'>
3 + 4j
# (3+4j)

```


#### abs()
Built-in function. Returns distance from zero

#### round()
Round to decimal place.
Can show sunrising behaviour with float values.


#### Base conversion

```python
bin(42)
# '0b101010'
oct(42)
# '0o52'
hex(42)
# '0x2a'

int("2a", base=16)
# 42

```

#### datetime
Standard library module `datetime`

Types:
- date => gregorian calender
- time => time within a day
- datetime => date & time

```python

import datetime
datetime.date(2014, 1, 6)
# datetime.date(2014, 1, 6)

datetime.date.fromtimestamp(1000000000)
# datetime.date(2001, 9, 9)
d = datetime.date.today()
d.year
# 2019
d.day
# 12

```
`d.strftime()`
Format data as a string



