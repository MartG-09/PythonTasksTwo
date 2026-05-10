numberOne = int(input("Enter number:  "))
numberTwo = int(input("Enter number:  "))

choose = (input("Enter operator '+' , ' - ' , ' * ' , ' / ' :  "))
choosen = choose.strip()

total = 0
if (choosen == '+'):
    total = numberOne + numberTwo
elif (choosen == '-'):
    total = numberOne - numberTwo
elif (choosen == '*'):
    total = numberOne * numberTwo
elif (choosen == '/'):
    total = numberOne / numberTwo

print(total)
