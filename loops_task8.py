# Get number of students from user
num_of_students = input('How many students are in your class? ')

# Convert user response to int
num_of_students = int(num_of_students)

# create empty list to hold student names
students = []

# loop over number of students using range() and a for loop
for number in range(num_of_students):
  # ask user for the name of each student 1 at a time
  name_of_student = input(f'What is the name of student #{number + 1}: ')
  # add the user's response to students list 1 at a time (append!!)
  students.append(name_of_student)

# loop over students list and print each to the console 1 at a time.
# for loop cheatsheet: FOR EACH {ITEM} IN {LIST}
for student in students:
  print(student)