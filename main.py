students = [
    ("Alice", 85),
    ("Bob", 78),
    ("Charlie", 92),
    ("David", 85),
    ("Eve", 78),
    ("Frank", 85),
    ("Mark", 50),
    ("George", 21)
]
def uniqueGrades(list_of_students):
    grades = []
    for student in list_of_students:
        grades.append(student[1])
    uniqueGrades = list(set(grades))
    return uniqueGrades

def topPerformer(list_of_students):
    list_of_students.sort(key=lambda student: student[1], reverse=True)
    topStudents = []
    for student in range(3):
        topStudents.append(list_of_students[student])
    return f"Top Students:{topStudents}"

print(topPerformer(students))

def failingStudents(list_of_students):
    failedStudents = []
    for student in list_of_students:
        if(student[1] <= 51):
            failedStudents.append(student)
    return f"failed students: {failedStudents}"

