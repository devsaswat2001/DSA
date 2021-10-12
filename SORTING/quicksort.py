def partition(a, si, ei):
    p = a[si]
    c = 0
    for i in range(si, ei + 1):
        if a[i] < p:
            c = c + 1
    a[si + c], a[si] = a[si], a[si + c]
    pi = si + c
    i = si
    j = ei
    while i < j:
        if a[i] < p:
            i = i + 1
        elif a[j] >= p:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return pi


def quickSort(arr, si, ei):
    if si > ei:
        return
    p = partition(arr, si, ei)
    quickSort(arr, si, p - 1)
    quickSort(arr, p + 1, ei)

    # Please add your code here


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, len(arr) - 1)
print(*arr)