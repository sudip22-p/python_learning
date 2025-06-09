# Typecasting in Python: converting one data type to another

# int to float
a = 10
b = float(a)
print(b)  # Output: 10.0

# float to int (truncates decimal part)
c = 3.99
d = int(c)
print(d)  # Output: 3

# int to string
e = 25
f = str(e)
print(f)  # Output: '25'

# string to int (only if string is numeric)
g = "123"
h = int(g)
print(h)  # Output: 123

# string to float
i = "3.14"
j = float(i)
print(j)  # Output: 3.14

# list to tuple
k = [1, 2, 3]
l = tuple(k)
print(l)  # Output: (1, 2, 3)

# tuple to list
m = (4, 5, 6)
n = list(m)
print(n)  # Output: [4, 5, 6]

# Using bool conversion
o = 0
p = bool(o)
print(p)  # Output: False

q = "hello"
r = bool(q)
print(r)  # Output: True (non-empty string is True)


"""
Note:
- Typecasting changes the data type of a variable explicitly.
- Conversions must be valid; e.g., int("123") works but int("abc") raises ValueError.
- When converting float to int, decimal part is truncated (not rounded).
- bool conversion: zero values (0, 0.0, '', None) become False, others True.
- Use try-except to handle invalid conversions safely.
"""
demo="Sud"
# demo2=int(demo)  # This will raise an error since 'Sud' cannot be converted to int
""" error:
Traceback (most recent call last):
  File "/root/Python/learning/python-basics/typecasting.py", line 57, in <module>
    demo2=int(demo)  # This will raise an error since 'Sud' cannot be converted to int
          ^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'Sud'
"""