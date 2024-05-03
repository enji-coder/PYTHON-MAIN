mylist = [1,2]

for v in range(2):
    mylist.insert(-1,mylist[v])

print(mylist)


"""
0 1
[1,1,1,2]
------insert 

"""