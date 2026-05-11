age = int(input("Enter age:  "))

price = ""
if (age == 5):
    price = "Free"
elif (12 > age >= 5):
    price = "$5"
elif (64 > age >= 13):
    price = "$12"
elif (age >= 65):
    price = "$8"

print(price)
