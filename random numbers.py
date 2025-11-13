import random

numberlist = []

for x in range(100):
    number = random.randint(1,500)
    numberlist.append(number)

for item in numberlist:
    print(item, end = ' ')
