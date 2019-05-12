# Strings and Representations

`str()` and `repr()`
Functions for making string representations from Python objects.
They call the special methods `__str__()` and `__repr__()` on the passed in objects.

**Rule of thumb**
- `repr()` is for developers
- `str()` is for clients


#### `repr()`
Built-in function. Produces a unambiguous string representation of the object.
 - Should include type of the object
 - Should include identifying fields.
Some Pythonistas argue repr of a object should return a valid Python code that when executed will recreate the object. 
This not suitable for all objects, but is fine rule of thumb.

- Suited for debugging
- Exact
- Includes identifying information
- Well suited to logging
- Should generally contain more information than the result of `str()`

**As a rule you should always write a repr() for your classes**
The default repr() is not very usefull.

**Example**

```python

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"


p = Point2D(2, 56)
repr(p) # Point2D(x=2, y=56)

```

Without implemented `__repr__()`
```python
p = Point2D(2, 56)
repr(p) # '<__main__.Point2D object at 0x7fe4e83d6d68>'
```

#### `str()`
Produces a readable, human-friendly representation of an object.
- Might be used to integration into normal text.


Example with Point2D class
```python

p = Point2D(2, 56)
str(p)
'(2, 56)'

```

Could be used with text like this:
```python
print(f"Circle is centered at: {p}") # Circle is centered at: (2, 56)
```

#### Printing
Python `print()` calls `str()` when passed a object. By default `str()` calls `repr()`.
But `repr()` does not call `str()`.

#### Printing collections
When printing a collection of objects. The `repr()` implementation is used.

Example:

```python

pl = [Point2D(i, i * 2) for i in range(3)]
print(pl) # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4)]

```


#### `str().format()`
`format()` does not call `str()` or `repr()` it calls the objects `__format__()`.
`__format__()` does by default call `__str__()`.

`__format__()` can be passed a format argument which can change the formating of the objects representation.

You can force the use of `__repr__()` when formatting by using !r
```python
"{!r}".format(p) # 'Point2D(x=2, y=56)'
```

You can force the use of `__str__()` when formatting by using !s
```python
"{!s}".format(p) # '(2, 56)'
```

#### reprlib
Standard library module. Supports alternative implementations of repr().

Features
- limits otherwise excessive string length
- useful for large collections

```python
reprlib.repr()
```
is a drop-in replacement of repr()

Example with long list of Point2D objects

```python
pl = [Point2D(i, i * 2) for i in range(1000)]
print(pl) # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4), Point2D(x=3, y=6), Point2D(x=4, y=8), Point2D(x=5, y=10), Point2D(x=6, y=12), Point2D(x=7, y=14), Poi....Continues

reprlib.repr(pl) # '[Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4), Point2D(x=3, y=6), Point2D(x=4, y=8), Point2D(x=5, y=10), ...]'

```

A log entry with thousands of objects represented in a list would be detrimental.


#### ASCII
Escapes non-ascii letters

```python
x = "Hållø"
y = ascii(x)
print(y) #"'H\\xe5ll\\xf8'"

```

#### ord
Converts a single character to its integer Unicode codepoint

```python
x = ord("a")
print(x) # 97
```

#### chr
Converts an interger Unicode codepoint to a single character string

```python
y = chr(97)
print(y) # a

```
