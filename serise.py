'''
                                        series is a most improtent
                                        [1] katho theka suru.
                                        [2] katha projontho cholba.
                                        [3] and , babodhan katho.
          EXAMPLE:- for x in range ( [1] katho theka suru , [2] katha projontho cholba , [3] babodhan katho  )
        --->>  nichaye explian kora a6a.
'''
# 1,2,3,....... n find series:
"""
n = int(input("Enter the last number = "))

for x in range(1,n):
    print(x)
"""
''' 
# 2,4,6,....... n find series:

n = int(input("Enter the last number = "))

for x in range(2,n+1,2):

    print(x)
  '''
'''
# 1,3,5,....... ,n find series:

n = int(input("Enter the last number = "))

for x in range(1,n+1,2):

    print(x)
'''
'''
# 1+2+3+4+5+.......+n find series:

n = int(input("Enter the last number = "))
add = 0
for x in range(1,n+1,2):
    add = add + x
print(add)
'''
# 1*1,2*2,3*3,4*4,.......n find series:

n = int(input("Enter the last number = "))
add = 0
for x in range(1,n+1,1):
    add = x*x
    print(add)

