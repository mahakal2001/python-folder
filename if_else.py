# if else statement :=
'''
#problem-1:-
num = int(input("Enter the ant integer number = "))

if num>= 25:
    print("pass = ", num)

else:
    print("fail = ", num)
'''
# odd/even
#problem-2:-
''' 
num = int(input("Enter the ant integer number = "))

if num%2 == 0:
    print("EVEN = ", num)

else:
    print("ODD = ", num)
'''
# if/elif/if:-
'''
num = int(input("Enter the marks = "))

if num>=90:
    print("student is pass (AA) = ", num)

elif num>=80:
    print("student is pass (A+)= ", num)

elif num>=70:
    print("student is pass (A)= ", num)

elif num>=60:
    print("student is pass (B+)= ", num)

elif num>=50:
    print("student is pass (B)= ", num)

elif num>=40:
    print("student is pass (C+)= ", num)

elif num>=30:
    print("student is pass (C)= ", num)

else:
    print("student is fail (D) = ", num)
'''
# largest number/small number (inner if statement)
'''
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the thred number : "))

if num1>num2 :
    if num1>num3:
        print("\nlargest number of num1 = ",num1)
    else:
        print("\nlargest number of num3 = ",num3)

if num2>num1 :
    if num2 > num3 :
        print("\nlargest number of num2 = ", num2)
    else:
        print("\nlargest number of num3 = ", num3)
'''
# ternary operator:=
'''
num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

maX = int ( num1 if num1>num2 else num2)
print("largest number = ", maX)

'''
# Two types of logical operator:=
#(1) AND
#(2) OR
#(3) NOT
'''
# (1) AND
num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
num3 = int(input("Enter the thride number = "))

if num1>num2 and num1>num3:
    print("largest number of num1 = ", num1)

elif num2>num1 and num2>num3:
    print("largest number of num2 = ", num2)

else:
    print("largest number of num3 = ",num3)
'''
# (2) OR

while(1):
    char = input("\nEnter the any character = ")

    if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
        print("It is a vowel = " + char)

    else:
        print("It is a consonal = " + char)


