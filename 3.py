# decimal to binary 

n = 27
b = bin(n)[2:]
print(b)

# print(27/2) 
n = 15
b = bin(n)[2:]
print(b)
"""
27 decimal to binary : binary base is 2 

27%2 = 13    = 1
13%2 = 6     = 1
6%2 = 6      = 0
3%2 = 1      = 1
1%2 = 1      = 1

-----------------
15%2 = 7     = 1
7%2  = 3     = 1
3%2 = 1      = 1
1%2 = 1      = 1
     3
     ----
   2|7
    |6
    -----
      1
"""