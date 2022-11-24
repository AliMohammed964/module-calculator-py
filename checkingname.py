import re
name = ' '
n = 0
expression = r'^[a-z]$|^([a-z]).*\1$'
while name != 'end':
    name = input("Enter your name : ")
    n = len(name)
    if n >= 8:
        break
    if re.search(expression, name):
        print("good")


print(name)
