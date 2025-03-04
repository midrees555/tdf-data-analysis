# print("MUHAMMAD IDREES")
# print(2 + 3)
# print("We are learning Python\n")

# Task By instructor - Write 10 to 15 lines of code as above mentioned
# Solution: - I'm going to build a small project - in which almost a lot of concepts used
# So, I've choosen to create a basic calculator that takes two numbers and an operation from the user, performs the calculation, and displays the result.

# def welcome_message():
#     print("-------------------------------------")
#     print("Welcome To Simple Calculator......!!!")
#     print("-------------------------------------")

# def taking_input():
#     num1 = float(input("Enter the First number\n"))
#     num2 = float(input("Enter the Second Number\n"))

#     print("Enter number for desire operation....")
#     print("1 for '+'")
#     print("2 for '—'")
#     print("3 for 'X'")
#     print("4 for '➗'")
#     operation = input("\n")

#     return num1, num2, operation

# def perform_operation(num1, num2, operation):
#     print("-------------------------")
#     result = 0
#     if operation == '1':
#         result = num1 + num2
#         return result
    
#     elif operation == '2':
#         result = num1 - num2
#         return result
    
#     elif operation == '3':
#         result = num1 * num2
#         return result

#     elif operation == '4' and num2 != 0:
#         result = num1 / num2
#         return result
#     elif operation == '➗' and num2 == 0:
#         print("Cannot divide by zero")
#         return

#     else:
#         print("Something went wrong....!\nPlease try again later.")


# def main():
#     welcome_message()

#     input_values = taking_input()

#     print(f"Result = {perform_operation(*input_values)}")


#     print("----------------------------------------------")
#     print("\n\nExiting Program...")
#     print("----------------------------------------------")
#     print("----------------------------------------------")



# main()


# -------------------------------------------------------------------------------
# BODMAS / PAMDAS rules in python
# In mathematics, the order of operations is a collection of rules that dictate the sequence in which operations should be performed in an expression. Two common acronyms used to remember these rules are BADMAS and PEMDAS.

# --------------!
# BADMAS:
# B - Brackets

# A - Addition and D - Division (left to right)

# M - Multiplication and A - Addition (left to right)

# Subtraction
# ----------------------------------------------------------


# PEMDAS
# P - Parentheses

# E - Exponents

# M - Multiplication and D - Division (left to right)

# A - Addition and S - Subtraction (left to right)

# Python's Default Order of Operations
# Python follows the 'PEMDAS' rule by default. This means:

# P - Parentheses are evaluated first.

# E - Exponents (or powers) are evaluated next.

# M - Multiplication and D - Division are evaluated from left to right.

# A - Addition and S - Subtraction are evaluated from left to right.

# Python Code Example
# Let's demonstrate Python's order of operations using the PEMDAS rule:

# Example expression
expression = 10 + 3 * 2 ** 2 / (4 - 2)

# Step-by-step evaluation:
# 1. Parentheses: (4 - 2) = 2
# 2. Exponents: 2 ** 2 = 4
# 3. Multiplication and Division: 3 * 4 = 12, then 12 / 2 = 6
# 4. Addition: 10 + 6 = 16

result = 10 + 3 * 2 ** 2 / (4 - 2)
print("Result:", result)  # Output: 16.0