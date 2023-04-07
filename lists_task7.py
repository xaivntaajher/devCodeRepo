students = ["John", "Mary", "Luke"]
grades = [9.0, 8.5, 7.5]
 
n = len(students)
 
for i in range(n):
    student = students[i]
    grade = grades[i]
    print([student]+[grade])
 
# output:
# John got a grade of 9.0
# Mary got a grade of 8.5
# Luke got a grade of 7.5