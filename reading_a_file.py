# Reading a file:=
'''
file = open("bhim.html","r+")

text = file.read()
print(text)
size = len(text)
print(size)
file.close()
'''

# Write a file:=
'''
file = open("bhim.html","w")
file.write("\n my name bhim charan bhakta")
file.close()
'''


num2 = int(input("enter a number"))
result =