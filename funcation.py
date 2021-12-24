# Funcation using addition:
'''
def add(x,y):
    suM = x+y
    print(suM)

def addition(x,y,z):
    suM = x + y + z
    print(suM)

add(10,20)
addition(10,20,30)
add(20,30)
'''
# Return value of funcation with addition
'''
def add(x,y):
    sum = x+y
    return sum

print(add(10,20))
'''
# Return value of funcation with large number:=
'''
def large(x,y):
    if x>y:
        return x
    else:
        return y

print(large(10,20))
'''
# X argument:=
# X argument --> tuple er matha kaj karaye
'''
def student(*details):
    sum = 0
    for num in details:
        sum = sum+num
    print(sum)

student(100,200,556)
student(100,20550,556)
student(100,200,556)
student(12500,200,556)
student(100,200,5256)
'''
# XX arguments:=
# XX arguments ---> dictionaries er matha kaj karaye

def students(**details):
    print(details)

students(iD = 10,name = "bhim")

