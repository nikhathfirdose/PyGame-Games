a = [1, 2, 3, 4]
b = 2


def rotateArray(a, b):
    ret = []
    for i in range(len(a)):
        print("val=", (i+b) % len(a))
        ret.append(a[(i+b) % len(a)])
    return ret


print(rotateArray(a, b))
