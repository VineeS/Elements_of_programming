import bisect


def intersect_two_sorted_array(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        print(i)
        return i < len(B) and B[i] == k

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and is_present(a)]


A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
B = [5, 5, 6, 8, 2, 8, 9, 10, 10]
print(intersect_two_sorted_array(A, B))
