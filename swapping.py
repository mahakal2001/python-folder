# swapping using tempary variable:=

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

temp = num1
num1 = num2
num2 = temp

print("\n\nSwapping first number = ",num1)
print("Swapping second number = ",num2)