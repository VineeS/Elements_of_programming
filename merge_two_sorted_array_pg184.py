def merge_two_sorted_array(A, m, B, n):
    a, b, write_index = m-1, n-1, m+n-1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1
        write_index -= 1

    while b >= 0:
        A[write_index] = B[b]
        write_index, b = write_index-1, b-1
    return A


A = [5, 13, 17, 0, 0, 0, 0, 0]
B = [6, 7, 11, 19]
m = 3
n = 4
print(merge_two_sorted_array(A, m, B, n))
