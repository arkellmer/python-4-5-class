#andrew kellmer 10/5/18

#grade calculator

print("input the students grades to make an average score and grade")

grade1 = int(input("student 1"))
grade2 = int(input("student 2"))
grade3 = int(input("student 3"))
grade4 = int(input("student 4"))
grade5 = int(input("student 5"))
grade6 = int(input("student 6"))
grade7 = int(input("student 7"))
grade8 = int(input("student 8"))
grade9 = int(input("student 9"))
grade10 = int(input("student 10"))


sum1 = grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 + grade8 + grade9 + grade10

avg = sum1/10

if avg>=90:
    grade = "A"
elif avg>=80:
    grade = "B"
elif avg>=70:
    grade = "C"
elif avg>=60:
    grade = "D"
elif avg>=50:
    grade = "F"
else:
    grade = "F"

print("The average score is",avg,"and the grade is",grade)

    

              
