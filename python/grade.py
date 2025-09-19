m = int(input("enter marks of maths: "))
m1 = int(input("enter marks of science: "))
m2 = int(input("enter marks of physics: "))
total_marks = m+m1+m2
average_marks = total_marks/3
percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = "A"
elif percentage > 80 and percentage <=90:
    grade = "B"
elif percentage > 70 and percentage <=80:
    grade = "C"
else:
    grade = "P"
    print(f"Total_marks: {total_marks}\nAverage_marks: {average_marks}\nGrade: {grade}")

