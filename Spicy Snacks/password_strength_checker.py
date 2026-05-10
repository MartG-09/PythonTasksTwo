pass_word = str(input("Create your password:  "))

if (len(pass_word) < 1):
    print(" Invalid")
elif (len(pass_word) < 6):
    print(" Weak")
elif (10 >= len(pass_word) > 6):
    print(" Medium")
elif (len(pass_word) > 10):
    print(" Strong")

