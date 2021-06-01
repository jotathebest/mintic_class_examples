# Example 1
x = "global"


def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

# Example 2
x = "global"


def foo():
    x = x * 2
    print(x)


foo()

# Example 3


def foo():
    y = "local"


foo()
print(y)

# Example 4


def foo():
    y = "local"
    print(y)


foo()

# Example 5

x = "global "


def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


foo()

# Example 6

x = 5


def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

# Example 7


def outer():
    test = 1

    def inner():
        test = 2
        print("inner", test)

    inner()
    print("outer", test)


test = 0
print("global", test)
