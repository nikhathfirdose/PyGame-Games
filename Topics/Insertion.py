arr = list(map(int, input().split()))


def InsSort(a):
    for i in range(len(a)):
        j = i-1
        key = a[i]
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
    return a


x = [44, 78, 66, 2, 4, 9, 12, 99]
print(InsSort(x))
