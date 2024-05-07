def func(a,b):
    return b ** a
#SyntaxError: positional argument follows keyword argument
print(func(b=2,2))  # it will return error 