def intersect_two_sorted_array(A, B):
    i = 0
    j = 0
    intersection_A_B = []
    while (i < len(A) and j < len(B)):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection_A_B.append(A[i])

            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(intersect_two_sorted_array(A, B))
