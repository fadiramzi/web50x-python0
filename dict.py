student = {
    "name": "Ahmed",
    "age":21
}
print(student)
print(student['name'])

student['score'] = 35
print(student)

del student['age']
print(student)

student.clear()

print(student)