#Write a program to calculate the highest score from a list of scores.
#eg student_scores = [76, 65, 89, 86, 55, 91, 64, 89]
#output: The highest score in the class is: X
def HighScoreFunc():
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
      student_scores[n] = int(student_scores[n])
    print(student_scores)
    highScore = 0
    for scores in student_scores:
        if scores > highScore:
            highScore = scores
    print(highScore)
HighScoreFunc()    