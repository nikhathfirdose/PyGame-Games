# combine
def MergeSort(L, R, A):
    nL = len(L)
    nR = len(R)
    i, j, k = 0, 0, 0

    while(i < nL and j < nR):
        if(L[i] < R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while(i < nL):
        A[k] = L[i]
        i += 1
        k += 1
    while(j < nR):
        A[k] = R[j]
        k += 1
        j += 1
    return A
# split


def Merge(arr):
    n = len(arr)
    if(n <= 1):
        return arr
    mid = n//2
    left = Merge(arr[:mid])
    right = Merge(arr[mid:])
    return MergeSort(left, right, arr)


print(Merge([1, 4, 5, 7, 2, 9, 3, 8]))


# def merge_sort(arr):
#     # The last array split
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     # Perform merge_sort recursively on both halves
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

#     # Merge each side together
#     return merge(left, right, arr.copy())


# def merge(left, right, merged):

#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):

#         # Sort each one and place into the result
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor+right_cursor]=left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1

#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]

#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]

#     return merged
# 0
