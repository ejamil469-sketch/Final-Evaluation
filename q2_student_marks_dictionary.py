students = {
    "Aarav": 78,
    "Diya": 45,
    "Rohan": 92,
    "Meera": 50,
    "Kabir": 36,
}

print("All students and marks:")
for name, marks in students.items():
    print(name, ":", marks)

print("\nStudents who scored 50 or above:")
for name, marks in students.items():
    if marks >= 50:
        print(name)

highest = max(students.values())
print("\nHighest mark:", highest)
