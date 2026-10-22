# BMI Calculator

A command-line Python program that calculates a user's Body Mass Index (BMI) and tells them which health category it falls in.

Task 2 of the Python Programming track, Oasis Infobyte Internship (OIBSIP).

## Features
- Asks for weight in kilograms and height in metres
- Calculates BMI using `BMI = weight / (height²)`
- Shows the BMI rounded to 2 decimal places
- Shows the category:
  - Underweight: below 18.5
  - Normal: 18.5 to 24.9
  - Overweight: 25 to 29.9
  - Obese: 30 and above
- Input validation:
  - Rejects text such as `abc`
  - Rejects zero and negative values
  - Asks again until a valid number is entered

## Technologies Used
- Python 3
- `input()`, `try/except`, `while` loops and `if/elif/else`

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:
   ```
   python bmi_calculator.py
   ```

## Sample Output
```
======BMI CALCULATOR======
Enter your weight in kg: 70
Enter your height in m: 1.75
Your BMI is: 22.86
You are normal weight
```

## Author
Suhana
GitHub: github.com/suhanasheikh572