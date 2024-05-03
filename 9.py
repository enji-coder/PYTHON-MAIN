"""
Operator precedence 

1) () : Parentheses 

"""

result = (3 + 4) * 2  # 14
print(result)

"""
2) ** : Exponentiation 

"""

result = (2 + 4) + 2 ** 4 #   6 + 2*2*2*2  = 6 + 16  = 22
print(result)

"""
3) *  /  //  % : multiplication , division , floor division , modulo 

have same precendence - so, it will execute from left to right 

"""

result = 12 / 4 * 4 // 5 % 3
# 12/4  = 3
# 3 * 4  = 12
# 12 // 5 = 2
# 2 % 3 = 2

"""   0
     ----
    3|2
      2
      --
      2
"""

print(result)

"""
4) +   -  : Addition and substraction have same precendence  and it execute left to right 

"""

result = 2 + 3 - 4 + 12 
# 5 - 4 + 12
# 1 + 12
# 13
print(result)

"""
5) << , >>  : bitwise left shift and right shift 
6) &  : bitwise AND 
7) ^  : bitwise XOR 
8) |  : bitwise OR 
9) comparision operator 
10) ! : bitwise Not 
11) +=,-=,/= Assignment Operator 
"""

result = (2+3) * 5 / 3 + 6 // 7 ** 3 % 6 - 3
# 5 * 5 / 3 + 6 // 7 ** 3  % 6 - 3 
# 5 * 5 / 3 + 6 // 343 % 6 - 3
# 25 / 3 + 6 // 343 % 6 - 3
# 8.0 +6 // 343 % 6 -3 
# 8.0 + 6 % 6 - 3
# 8.0 + 0 - 3
# 5.0
print(result)



