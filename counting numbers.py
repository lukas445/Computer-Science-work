maxNumber = 0
num = [23, 54, 54, 60, 12, 11, 15, 22]

for x in range(len(num)):
    if (num[x] > maxNumber):
        maxNumber = num[x]

print(maxNumber)