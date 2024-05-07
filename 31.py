a = 1 
b = 0

x = a or b 
y = not(a and b)

# x = a or b: In Python, the or operator returns the first operand if it evaluates to True, otherwise, it returns the second operand. In this case, a is True because it's a non-zero value (1), and b is False because it's zero. Since a evaluates to True, x will be assigned the value of a, which is 1.

print(x+y)

a = 0 
b = 1 
x = a or b 
y = not(a and b)
print(x+y)