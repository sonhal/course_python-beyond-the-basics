# Beyond basic functions

#### Callable instances and the ```__call__()``` special method
Implementing ```__call__()``` makes user made objects *callable* just like functions.


#### Callable classes
Calling a class invokes the constructor. Note: Class objects an instance objects are two different things!


#### Conditional expression

Conditional statement:

```python
if condition:
    result = true_value
else:
    result = false_value

```

Conditional expression:

```python
result = true_value if condition else false_value
```

See PEP 308 for more


#### Lambda expression
In many cases declaring a full fledge function is overkill. Lambdas are a way to create anonymous functions in Python.
The Python method ``sorted()`` is a function that takes a function as a parameter. We can pass a lambda instead.

```python
scientists = ["Marie", "Albert", "Niels", "Isaac", "Charles", "Antoine"]
print(sorted(scientists, key=lambda name: name[-1]))
```

**Difrences between lambda and def**

| def        | lambda         |
| ------------- |-------------| 
| *statement* which defines a function and binds it to a name | *expression* which evaluates to a function | 
| must have a name | Anonymous  |   
| Argument list is delimited by parentheses, separated by commas | Argument list is terminated by colon, separated by commas   |    
| Body is and indented block of statements | Body is a single expression |
Function declaration and lambda declaration with binding to variable |
| return statement is needed to return anything other than None | return value is given by the body expression. No return statement is permitted |


```python
def first_name(name):
    return name.split()[-1]
    
first_name = lambda name: name.split()[-1]

```

#### Determine if a object is callable
built-in function ``callable()`` can determine if a object is callable.

#### Extended formal argument syntax
Function than can take a arbitrary amount of positional or keyword arguments.

``*``prefix for arbitrary amount of positional arguments. ``**`` prefix for arbitrary amount of keyword arguments.
```python
def extendend(*args, **kwargs):
```

#### Extended actual argument syntax

```python
def fun(arg1, arg2, arg3):
    pass

t = (1,2,3)

fun(*t)

```

One of the main uses of extended arguments are wrapper functions which takes a function and all the function arguments
and do additionally work before calling the passed in function.