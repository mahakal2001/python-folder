
# find a program to calculate number of letter,digit,word

numberOfLetter = 0
numberOfDigit = 0
numberOfWord = 0

text = input("Enter of text of number = ")

for x in text:
    x = x.lower()
    if x>= 'a' and 'z':
        numberOfLetter = numberOfLetter+1

    elif x>= '0' and '9':
        numberOfDigit = numberOfDigit+1

    elif x == ' ':
        numberOfWord = numberOfWord+1

print("Number of letter = ",numberOfLetter)
print("Number of digit = ",numberOfDigit)
print("Number of word = ",numberOfWord)

