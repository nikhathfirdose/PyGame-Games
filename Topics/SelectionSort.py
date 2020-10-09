arr = [2, 5, 6, 8, 1, 4]
temp = arr
for i in range(len(arr)-1):
    minIndex = i
    for j in range(i+1, len(arr)):
        if(arr[j] < arr[minIndex]):
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
print(arr)
