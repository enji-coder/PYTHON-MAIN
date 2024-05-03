#XOR  ^  bitwise operator 
"""
if both bits are same it will return false (0)
if both bits are not same it will return true (1)

"""

a = 10 
b = 7 

a = int(bin(10)[2:])
b = int(bin(7)[2:])

result = a^b
print(result)
if a^b:
    print("Both are different - 1")
else:
    print("Both are same - 0 ")