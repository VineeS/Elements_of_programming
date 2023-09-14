class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __repr__(self):
        return '{} {}'.format(self.name, self.grade)


L = []

s1 = Student('A', 4.6)
s2 = Student('C', 2.6)
s3 = Student('E', 3.6)
s4 = Student('D', 1.6)
s5 = Student('B', 1.2)
L.append(s1)
L.append(s2)
L.append(s3)
L.append(s4)
L.append(s5)

List_sort = sorted(L)
print(List_sort)

for i in List_sort:
    print(i)
