dct = {'one':'two' , 'three' : 'one','two': 'three'}
v = dct['three']
# v = one 
# -------- 
# v = two
# v = three 
# v = one 

for k in range(len(dct)):  # 0,3  # 0 - 1 - 2
    v = dct[v]

print(v)
