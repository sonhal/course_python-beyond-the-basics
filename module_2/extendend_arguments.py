
def extended_pos_args(*args):
    print(args)
    print(type(args))

# implementation with extended arguments
def hypervolume(*args):
    i = iter(args)
    v = next(i)
    for length in i:
        v *= length
    return v

# implementation with regular argument first to avoid no argument bug
def hypervolume_pos(length, *lengths):
    v = length
    for length in lengths:
        v *= length
    return v


def extended_keyword_args(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag(name, **attributes):
    result = "<" + name
    for key, value in attributes.items():
        result += f' {key}="{str(value)}"'
    result += ">"
    return result


def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

# wrapper function
def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
    result = f(*args, **kwargs)
    print("result = ", result)
    return result


if __name__ == "__main__":
    extended_pos_args("s", "sad", "asdasd", 1)
    extended_pos_args(1)
    print(hypervolume(2,2,2))
    print(hypervolume_pos(1))
    print(tag("img", src="monet.jpg", alt="Sunrise by Claude Monet", border=1))
    # explode tuple to parameters
    t = (1,2,3,4,5)
    print_args(*t)
    trace(int, "ff", base=16)