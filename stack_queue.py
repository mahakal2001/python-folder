# STACK :=
# stack is use to list
'''
book = []
book.append("learn c")
book.append("learn c++")
book.append("learn css")
book.append("learn java")
book.append("learn python")

print(book)

book.pop()
print("\nNow the top book is : ",book[-1])

book.pop()
print("\nNow the top book is : ",book[-1])

book.pop()
print("\nNow the top book is : ",book[-1])

book.pop()
print("\nNow the top book is : ",book[-1])

book.pop()
if not book:
    print("there are no book is a stack")
'''

# QUEUE:


from collections import deque

bank = deque(["bhim","subha","shib","krison"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()

if not bank:
    print("No person left")

