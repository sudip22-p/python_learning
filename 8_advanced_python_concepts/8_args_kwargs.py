# ARGS and KWARGS
# In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
# *args allows you to pass a variable number of non-keyword arguments,
# while **kwargs allows you to pass a variable number of keyword arguments.
# This is useful when you don't know beforehand how many arguments might be passed to a function.


# *args example
def fun(arg1, *argv):
    print("First argument :", arg1)  # This is a regular argument
    for arg in argv:
        print("Argument *argv :", arg)


fun("Hello", "Welcome", "to", "Mars")


# **kwargs example
def fun2(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


fun2(s1="Mars", s2="is", s3="Wonderful")


# Combining *args and **kwargs
def fun3(arg1, *args, **kwargs):
    print("First argument:", arg1)
    print("Additional non-keyword arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)


fun3("Hello", "Welcome", "to", "Mars", s1="Mars", s2="is", s3="Wonderful")
