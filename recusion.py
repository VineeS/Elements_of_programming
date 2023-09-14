def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod,
              "to rod", to_rod, "use rod", aux_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod,
          "to rod", to_rod, "use rod", aux_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# n = int(input("Enter the number of disks"))
# TowerOfHanoi(n, 0, 1, 2)


def compute_tower(number_of_rings):
    def coumpute_tower_steps(number_of_rings, from_rod, to_rod, aux_rod):
        if number_of_rings > 0:
            coumpute_tower_steps(number_of_rings-1, from_rod, aux_rod, to_rod)
            pegs[to_rod].append(pegs[from_rod].pop())
            result.append([from_rod, to_rod])
            coumpute_tower_steps(number_of_rings-1, aux_rod, to_rod, from_rod)

    result = []
    pegs = [list(reversed(range(1, number_of_rings+1)))] + [[]
                                                            for _ in range(1, number_of_rings)]
    coumpute_tower_steps(number_of_rings, 0, 1, 2)
    return result


ans = compute_tower(6)
print(len(ans))
