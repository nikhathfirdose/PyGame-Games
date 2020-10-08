def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(len(A)):
        B.append([0] * n)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

B = performOps(A)
print(B)


def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in range(len(A)):
        B[i] = A[i]
        print("re=", (len(A) - i) % len(A))
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B


A = [5, 10, 2, 1]
B = performOps(A)
for i in range(len(B)):
    print(B[i],)
print("val", 2 % 4)
