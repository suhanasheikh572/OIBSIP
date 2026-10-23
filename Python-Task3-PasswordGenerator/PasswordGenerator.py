import random
import string

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()[]{};:'.?<>/|"

print("\n========Welcome to the PASSWORD GENERATOR!========= \n")

while True :

    while True :
        try :
            length = int(input("Enter the length of password:"))
            if length >= 8 :
                break
            else :
                print("Password must have atleast 8 characters.")
        except ValueError :
            print("Error : Please enter a whole number.")
    

# User should select at least two options to generate a strong password...
# as it will not generate a strong password if user select only one option.
 
    print("\nPlease select at least two options from the following to generate a strong password:\n")
    while True :

        a = input("Do you want to include Uppercase letters in your password? [y/n]:").lower()
        b = input("Do you want to include Lowercase letters in your password? [y/n]:").lower()
        c = input("Do you want to include numbers in your password? [y/n]:").lower()
        d = input("Do you want to include symbols in your password? [y/n]:").lower()

        if [a, b, c, d].count("y") >= 2 :
            break
        print("Error: Please select at least 2 types")

    check = ""

    if a == "y" :

        check = check + string.ascii_uppercase
        
    if b == "y" :
        check = check + string.ascii_lowercase

    if c == "y" :
        check = check + numbers

    if d == "y" :
        check = check + symbols

    count = 0
    password = ""


    while count < length :

        password = password + random.choice(check)

        count = count + 1

    print("\nYour password is generated successfully! Your password is :", password)

    again = input("Generate another password? (y/n) : ").lower()

    if again != "y" :
        break



