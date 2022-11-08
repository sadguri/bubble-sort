array = [7, 3, 1, 9, 2, 5]
print(array)
n = len(array)

count = 0
for run in range(n-1):
    for i in range(n-1):
        if array[i] > array[i+1]:
            count += 1
            array[i], array[i+1] = array[i+1], array[i]

print(count)
print(array)