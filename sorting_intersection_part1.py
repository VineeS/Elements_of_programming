# def intersection(A, B):
#     return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and a in B]


def intersection(A, B):
    list_final = []
    for i, a in enumerate(A):
        print("a", a, "A[i-1]", A[i-1])

        if (i == 0 or a != A[i-1] and a in B):
            list_final.append(a)

    return list_final


A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
B = [5, 5, 6, 8, 2, 8, 9, 10, 10]

print(intersection(A, B))
