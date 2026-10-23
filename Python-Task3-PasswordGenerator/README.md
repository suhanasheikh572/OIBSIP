# Random Password Generator

A command-line Python program that generates random passwords based on the length and character types chosen by the user.

Task 3 of the Python Programming track, Oasis Infobyte Internship (OIBSIP).

## Features
- Asks for the password length (minimum 8 characters)
- Lets the user choose character types:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- At least 2 types must be selected
- Generates a password using only the selected types
- Input validation:
  - Rejects text instead of a number
  - Rejects lengths below 8
  - Asks again if fewer than 2 types are chosen
- Option to generate another password without restarting the program

## Technologies Used
- Python 3
- `random` and `string` modules
- `while` loops, `try/except` and `if` statements

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:
   ```
   python PasswordGenerator.py
   ```

## Sample Output
```
![Output] (screenshot.png)

```

## Author
Suhana

GitHub: github.com/suhanasheikh572