


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    scores =  student_scores[i]
    if scores > 90:
        student_grades[i] = "Outstanding"
    elif scores > 80:
        student_grades[i] = "Exceeds Expectations!"
    elif scores > 70:
        student_grades[i] = 'Acceptable'
    else:
        student_grades[i] = 'Failed.'
print(student_grades)





# Expected output:
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'