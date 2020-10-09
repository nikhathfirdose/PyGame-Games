def Bub(a):
    for i in range(len(a)):
        flag = 0
        for j in range(len(a)-i-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                flag += 1
            elif(flag == 0):
                return a, "fla"
    return a


arr = [1, 2, 3, 5, ]
print([float(r) for r in arr])
