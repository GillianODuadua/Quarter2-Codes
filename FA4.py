
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

total_class_score = 0   
total_entries = num_students * num_subjects

print()


for s in range(1, num_students + 1):
    print(f"Student {s}")
    student_total = 0

    
    for subj in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subj}: "))
        student_total += score

    
    student_avg = student_total / num_subjects
    print(f"Average for Student {s} = {student_avg}\n")

    
    total_class_score += student_total


class_avg = total_class_score / total_entries
print(f"Class Average = {class_avg}")
