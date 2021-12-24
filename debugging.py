


def student(*details):
    sum = 0
    for num in details:
        sum = sum+num
    return sum

print(student(10,20))
