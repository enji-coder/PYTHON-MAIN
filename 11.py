my_list = [x * x for x in range(0,5)]

"""
0  - 0
1  - 1 
4  - 2
9  - 3 
16 - 4

index = lst[2]
index = 4

0  - 0
1  - 1 
4  - 2
9  - 3 

"""

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
