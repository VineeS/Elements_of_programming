class Name():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return (self.name < other.name
                if self.name != other.name else
                self.surname < other.surname)

    def __repr__(self):
        return '{} {}'.format(self.name, self.surname)


def eliminate_duplicates(A):
    A.sort()
    print(A)

    write_indx = 1
    for cand in A[1:]:
        print(A[1:])
        if cand != A[write_indx-1]:
            print("In If statement A", A[write_indx:])
            A[write_indx] = cand
            write_indx += 1
    print("For loop ended A", A[write_indx:])
    del A[write_indx:]
    return A


A = []
s1 = Name("Ian", "Botham")
s2 = Name("David", "Gower")
s3 = Name("Ian", "Bell")
s4 = Name("Ian", "Chappel")
s5 = Name("James", "Jewel")
s6 = Name("Kames", "Kewel")

A.append(s1)
A.append(s2)
A.append(s3)
A.append(s4)
A.append(s5)
A.append(s6)


print(eliminate_duplicates(A))
