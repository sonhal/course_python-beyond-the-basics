
def escape_unicode(f):
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        return ascii(result)

    return wrap

@escape_unicode
def nothern_city():
    return "Tromsø"


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


@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + "øy"

if __name__ == "__main__":
    print(nothern_city())
    hello("Sondre")
    print(hello.count)
    hello("Mikael")
    print(hello.count)
    l = [1,2,3,4,5]
    print("list: " + str(rotate_list(l)))
    tracer.enabled = False
    print("list: " + str(rotate_list(l)))
    tracer.enabled = True
    print(norwegian_island_maker("Fall"))
