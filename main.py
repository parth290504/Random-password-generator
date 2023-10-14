import string
import random

def generate():


    length = int(input("Enter password length: "))

    print('''kindly Choose character set for password from the below options : 
    		press 1 for- Digits
    		press 2 for- Letters
    		press 3 for- Special characters
    		press 4 to - Exit''')

    characterList = ""


    while (True):
        choice = int(input("Enter the character set number: "))
        if (choice == 1):


            characterList += string.digits        
        elif (choice == 2):


            characterList += string.ascii_letters
        elif (choice == 3):



            characterList += string.punctuation
        elif (choice == 4):
            break
        else:
            print("Please pick a valid option!")

    password = []

    for i in range(length):


        randomchar = random.choice(characterList)


        password.append(randomchar)

    print("\nYour random password generated is:  " + "".join(password))
    x = (input("\nDo you want to generate another password? \n Press y if yes \n Press n if no\n"))
    if x == "y":
        generate()

    else:
        print("Thank you for using this random password generator")

generate()

