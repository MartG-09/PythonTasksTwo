total = 0
count = 0
for count in range(3):
    scorces = int(input("Enter scores  "))
    total = total + scorces
    count += 1

average = float(total) / count

grade = ""
if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
elif 0 <= average < 60:
    grade = "F"



print(f"Average is {average:.2f} , and your letter grade is {grade}")
