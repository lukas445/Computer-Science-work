items = [12, 54, 5, 7, 32, 34]

n = len(items) - 1
index = 0

for index in range(0, n):
    if (items[index] > items[index + 1]):
        temp = items[index]
        items[index] = items[index + 1]
        items[index + 1] = temp

print(items)
