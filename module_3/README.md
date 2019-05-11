# Closures and Decorators

``def`` define new functions, executed at runtime.

That makes it possible to define function inside other functions
commonly called local functions.
```python

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

```

**Remember the LEGB rule:**
local, enclosing, global, built-in


#### First-class functions
functions can be treated like any other object


#### Closures
Mantains references to objects from earlier scopres

```python

def outer():
    x = 3
    def inner(y):
        return x + y
    return inner

i = outer()
print(i(2)) # 5

```
In Python closures have a special attrubute `__closure__` containg the closed over objects.

```python
i.__closure__
# (<cell at 0x7fe8e842efd8: int object at 0x7fe8f68ef520>,)
```

#### Function factories
Functions that returns new, specialized functions

Example:

```python
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
cube = raise_to(3)

square(2) # 4
```

#### ``global`` keyword
Introduce names from global namespace into the local namespace.

#### ``nonlocal`` keyword
Introduce names from the enclosing namespace into the local namespace.

Example
``make_timer`` returns a new function that keeps track of time since last it was called.

```python
import time

def make_timer():
    last_called = None
    
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed

```


#### Decorators
Modify or enhance functions without changing their definition.
Implemented as callables that take and return other callables.

```python
@my_decorator
def my_function():
    ...

```

Above Python will create ``my_function`` and then pass it to ``my_decorator``as a parameter.
``my_decorator`` returns a callable object and Python binds this object to the function name ``my_function``.


Example

```python

def escape_unicode(f):
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        return ascii(result)

    return wrap

@escape_unicode
def nothern_city():
    return "Tromsø"


if __name__ == "__main__":
    print(nothern_city())

```

Functions can be decorators, but other objects can be as well.

#### Classes as decorators
Classes are callable. If classes are to be used as decorators they must implement the ``__call__`` special method.

Example

```python
class CallCount:
    """
    Class decorator

    Keeps track of times called
    """

    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count +=1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print(f"Hello {name}!")
    
hello("Sondre")
print(hello.count)
hello("Mikael")
print(hello.count) # 2
```

#### Instances as decorators
Decorating with an instance calls the instance. The return value of the instance ``__call__`` must be callable.


Example

```python
class Trace:
    """
    Instance decorator

    Traces the function called. Can be toggled
    """

    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, *kwargs)
        return wrap


tracer = Trace()
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1,2,3,4,5]
print("list: " + str(rotate_list(l)))
tracer.enabled = False
print("list: " + str(rotate_list(l)))
    
# Calling <function rotate_list at 0x7fa419e0d378>
# list: [2, 3, 4, 5, 1]
# list: [2, 3, 4, 5, 1]
```

#### Multiple decorators
It is possible to stack decorators on a single function. The decorators are applied from the bottom to the top.

Example

```python

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + "øy"

print(norwegian_island_maker("Fall"))
# Calling <function escape_unicode.<locals>.wrap at 0x7fc366b76620>
# 'Fall\xf8y'


```


#### Decorators and function metadata
Naive decorators can lose importat metadata

```python

import functools


def hello():
    """prints hello world"""
    print("Hello, world!")


def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper


@noop
def hello_2():
    """prints hello world"""
    print("Hello, world!")


def non_naive_noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper


@non_naive_noop
def hello_3():
    """prints hello world"""
    print("Hello, world!")


if __name__ == "__main__":
    # help contains usefull metadata
    print(hello.__doc__)
    # But hello_2 has lost the metadata because of the wrapping
    print(hello_2.__doc__)
    # non_naive_noop function use functools.wraps to persist the metadata to the wrapper
    print(hello_3.__doc__)

```

#### Remember 
- Decorators are a powerfull tool
- Decorators are widely used in Python
- It's possible to overuse decorators; be mindful