students = [
    {
        "name": "Alice",
        "grades": [
            {"subject": "Math", "score": 88},
            {"subject": "Science", "score": 92},
            {"subject": "History", "score": 79}
        ]
    },
    {
        "name": "Bob",
        "grades": [
            {"subject": "Math", "score": 75},
            {"subject": "Science", "score": 85},
            {"subject": "History", "score": 90}
        ]
    },
    {
        "name": "Charlie",
        "grades": [
            {"subject": "Math", "score": 95},
            {"subject": "Science", "score": 78},
            {"subject": "History", "score": 84}
        ]
    }
]

# TODO:
# 1. Print each student's name and their average score.

highest_avg = 0
student_name =""

# 2. Print the name of the student with the highest average.
for student in students:
    total = 0
    for grade in student["grades"]:
        score = grade['score']
        total += score
    avg = total/len(student['grades'])
    print(f"The average of {student['name']}'s grades is : {avg}")
    if avg > highest_avg:
        highest_avg = avg
        student_name = student['name']
print(f"The student {student_name} is having highest average :{highest_avg}")

# # 3. Print the average score for each subject across all students.

subject_totals = {} # to store total per subject
subject_count = {} # to know how many students took subject
for student in students:
    for grade in student['grades']:
        subject = grade['subject']
        score = grade['score']
        if subject in subject_totals:
            subject_totals[subject] +=score
            subject_count[subject] += 1
        else:
            subject_totals[subject] = score
            subject_count[subject] =1
for subject in subject_totals:
    avg = subject_totals[subject]/subject_count[subject]
    print(f"avg score for  {subject} is : {avg:.2f}")





# 4. Bonus: List the names of students who scored more than 90 in any subject.
