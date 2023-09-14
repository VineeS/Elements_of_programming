def non_constructable_change(A):
    max_constructable_change = 0
    for a in sorted(A):
        if a > max_constructable_change+1:
            print("In If", "a", a, "max_constructable_change",
                  max_constructable_change)
            break
        else:
            max_constructable_change += a
            print("Else", "a", a, "max_constructable_change",
                  max_constructable_change)

    return max_constructable_change+1


print(non_constructable_change([1, 1, 1, 1, 1, 5, 10, 25]))
