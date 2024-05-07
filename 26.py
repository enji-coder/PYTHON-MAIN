x = int(input()) # 3
y = int(input()) # 2

x = x % y   # 1
x = x % y   # 1
y = y % x   # 0

print(x)  # 1

"""  
      1         0         2
     -----     -----     ----
    2|3       2|1       1|2
      2         0         2
      --        ---       --
      1         1         0

"""


