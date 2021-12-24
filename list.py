'''
number = [10, 20, 30, 40, 50, 30]
string = ("a", "b", "c", "d", "e", "f")
number.append(66)
number.insert(1, 33)
number.remove(10)
print(string)
print(number)
'''

# list as input from user:=
'''
n = input("Enter the list of number = ")
list = n.split()

sum = 0

for x in list:
    sum = sum + int (x)
print("list of number = ",sum)
'''
# List comprehensions:=

num = [1,2,3,4,5]

# expration for item in list
.............................
result = [x*x for x in num]
print(result)
