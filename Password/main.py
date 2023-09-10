correct = False
counter = 0
Upper = False
Lower = False
Symbol = False
Length = False

print("Rules:\nPlease enter a password containg 1 number, 1 capital letter, 1 small letter and a '%' symbol")
pass1 = str(input("Enter a password:"))

while (counter <= 3) or correct == True:
    if len(pass1) >= 7:
        Length = True
        for i in range(len(pass1)):
            if pass1[i] == pass1[i].upper():
                Upper = True
                if pass1[i] == pass1[i].lower():
                    Lower = True
                    if pass1[i] == "%":
                        Symbol = True
                        correct == True
    if correct == False:
        if Length == False:
            print("Your password must contain a minimum of 8 characters!!")
            if Upper == False:
                print("Your password must contain a capital letter!")
                if Lower == False:
                    print("Your password must contain a lower letter!")
                    if Symbol == False:
                        print("Your password must contain a '%' symbol")
        elif Upper == False:
            print("Your password must contain a capital letter!")
        elif Lower == False:
            print("Your password must contain a lower letter!")
        elif Symbol == False:
            print("Your password must contain a '%' symbol")
            
    print("Incorrect password!!!\nEnter password again:\n")
    pass1 = str(input("Enter a password:"))
    counter = counter + 1

print("Correct password, make sure to remember it cuz i aint going through all that shit to change it again!")