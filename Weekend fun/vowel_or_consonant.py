letter = str(input("Enter a letter:  "))
length = len(letter)
if (length == 1):
    word = letter.lower()
    vowel = ["a" , "e" , "i" , "o" , "u"]

    for count in range(5):
        if word in vowel[count]:
            print("Vowel")
            break
    else:
        print("Consonant")
else:
    print("Invalid input")
