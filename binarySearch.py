def binarySearch(A, key):
    l = 0
    r = len(A)-1
    while (l <= r):
        mid = round((l+r)/2)
        print("l", l, "r", r, "mid", mid, "A[mid]", A[mid], "key", key)

        if A[mid] == key:
            return mid
        elif A[mid] > key:
            print("A[mid] > key", "A[mid]", A[mid], "key", key)
            r = mid-1
        else:
            print("A[mid]", A[mid], "key", key)
            l = mid+1

    if (A[mid] != key):
        print("Search completed......")
        print("Number not in list")


A = [3, 6, 8, 12, 14, 17, 25, 29, 36, 42]
print(binarySearch(A, 42))
