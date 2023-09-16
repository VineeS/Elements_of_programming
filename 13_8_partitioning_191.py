import collections

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def rearrange_students_by_age(people):
    age_groups = {}

    for student in people:
        if student.age in age_groups:
            age_groups[student.age].append(student)
        else:
            age_groups[student.age] = [student]

    # Reconstruct the array with students of equal age together and sorted by age
    result = []
    for age in sorted(age_groups.keys()):
        result.extend(sorted(age_groups[age], key=lambda student: student.name))

    return result


people = [
    Person('Greg',14),
    Person('John',12),
    Person('Andy',11),
    Person('Jim',13),
    Person('Phil',12),
    Person('Bob',13),
    Person('Chip',13),
    Person('Tim',14)
]
rearranged_students = rearrange_students_by_age(people)

for student in rearranged_students:
    print(f"{student.name} - {student.age}")
