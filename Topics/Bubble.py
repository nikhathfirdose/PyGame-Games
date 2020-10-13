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


print(Bub([1, 7, 9]))
