total_bill = int(input("Enter bill:  "))
is_member = str(input("Enter 'Yes' or 'No' :  "))

normal = is_member.lower()

amount = 0
if (total_bill >= 1000 and normal == 'yes'):
    discount = total_bill * 0.1
    amount = total_bill - discount
    print(amount)
elif (total_bill >= 1000 and normal == 'no'):
    discount = total_bill * 0.05
    amount = total_bill - discount
    print(amount)
else:
    print("No discount, amount is" , total_bill)
