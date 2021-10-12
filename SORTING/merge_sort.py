def merge_sort(a, start, end):
    l = len(a)
    if l > 1:
        mid = (start + end) // 2
        lst1 = a[:mid]
        lst2 = a[mid:]

        merge_sort(lst1, 0, len(lst1))
        merge_sort(lst2, 0, len(lst2))

        i = 0
        j = 0
        k = 0

        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                a[k] = lst1[i]
                i += 1
            else:
                a[k] = lst2[j]
                j += 1
            k += 1

        while i < len(lst1):
            a[k] = lst1[i]
            i += 1
            k += 1

        while j < len(lst2):
            a[k] = lst2[j]
            j += 1
            k += 1


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
merge_sort(arr, 0, n)
print(*arr)
