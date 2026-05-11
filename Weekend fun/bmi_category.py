weight = int(input("Enter weight (kg) :  "))
height = int(input("Enter height (m) :  "))

compute_bmi = weight / (height * height)

if (compute_bmi < 18.5):
    print("Underweight")
elif(18.5 < compute_bmi < 24.9):
    print("Normal")
elif (25 < compute_bmi < 29.9):
    print("Overweight")
elif (compute_bmi >= 30):
    print("Obese")
