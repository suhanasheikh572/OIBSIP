# BMI Calculator

print("======BMI CALCULATOR======")

while True :
    try:
        wgt = float(input("Enter your weight in kg:"))   
        if wgt > 0 :
            break
        else:
            print("Weight must be greater than 0")
    except ValueError:
        print("Error : Please enter numeric value (e.g.,45.5 etc.)")

while True :
    try:
        hgt = float(input("Enter your height in m:"))
        if hgt > 0:
            break
        else:
            print("Height must be greater than 0")
    except ValueError:
        print("Error : Please enter a numeric value for height (e.g., 1.75)")
        
bmi = wgt / (hgt ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:

    print("You are underweight")

elif bmi < 25:

    print("You are normal weight")

elif bmi < 30:

    print("You are overweight")

else:

    print("You are obese")

