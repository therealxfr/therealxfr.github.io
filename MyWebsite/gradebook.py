# Gradebook with students' grades for different assignments
gradebook = [
    [100, 100, 100, 96],  # Student 1
    [97, 87, 92, 88],     # Student 2
    [91, 90, 92, 91]      # Student 3
]

# Number of students and assignments
num_students = len(gradebook)
num_assignments = len(gradebook[0])

# Calculate and display assignment averages
print("Assignment Averages:")
for assignment in range(num_assignments):
    total = 0
    for student in range(num_students):
        total += gradebook[student][assignment]
    average = total / num_students
    print(f"Assignment {assignment + 1}: {average:.2f}")

# Calculate and display student averages
print("\nStudent Averages:")
for student in range(num_students):
    total = sum(gradebook[student])
    average = total / num_assignments
    print(f"Student {student + 1}: {average:.2f}")
