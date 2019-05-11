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

