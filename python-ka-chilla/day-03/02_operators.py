# Basic / Arithmatic Operators
# ------------------------------------------------------->
a = 5
b = 3

# 1. Addition
print(a + b)  # Output: 8


# 2. Subtraction
print(a - b)  # Output: 2


# 3. Multiplication
print(a * b)  # Output: 15


# 4. Division
print(a / b)  # Output: 1.6666666666666667


# 5. Modulus (Remainder)



# 6. Exponentiation



# 7. Floor Division


# -------------------------->
# PEMDAS Test before diving into advanced operators
print("PEMDAS Test...")
print(3 ** 2 / 2 * 3 / 3 + 6 - 4 / (2 * 6))
# Solution: 10.166666
# -------------------------->
# Explanation:
# ------------>
# The order of operations in Python follows the PEMDAS/BODMAS rules, which stands for:

# 1. Parentheses '()': Evaluate expressions inside parentheses first.
# 2. Exponents '**': Evaluate exponents (powers and roots).
# 3. Multiplication '*' and Division '/': Evaluate from left to right, whichever comes first.
# 4. Addition '+' and Subtraction '-': Evaluate from left to right, whichever comes first.

# So, in the expression '3 ** 2 / 2 * 3 / 3 + 6 - 4 / (2 * 6)', the operations are performed in the following order:

# 1. Parentheses: '4 / (2 * 6)' becomes '4 / 12' which is '0.3333333333333333'.
# 2. Exponents: '3 ** 2' becomes '9'.
# 3. Multiplication and Division (from left to right):
#    - '9 / 2' becomes '4.5'.
#    - '4.5 * 3' becomes '13.5'.
#    - '13.5 / 3' becomes '4.5'.
# 4. Addition and Subtraction (from left to right):
#    - '4.5 + 6' becomes '10.5'.
#    - '10.5 - 0.3333333333333333' becomes '10.166666666666666'.

# Here is the code snippet from your file with the PEMDAS test:

# python
# print("PEMDAS Test...")
# print(3 ** 2 / 2 * 3 / 3 + 6 - 4 / (2 * 6))

# This will output '10.166666666666666' as explained.
# ---------------------------------------------------------------------------------------------->




# ------------------------------------------------->
# Advanced Operators
# -------------------------->
# 8. Bitwise AND
# 9. Bitwise OR
# 10. Bitwise XOR
# 11. Bitwise NOT
# 12. Left Shift
# 13. Right Shift
# 14. Multiplication Assignment
# 15. Division Assignment
# 16. Modulus Assignment
# 17. Exponentiation Assignment
# 18. Bitwise AND Assignment
# 19. Bitwise OR Assignment
# 20. Bitwise XOR Assignment
# 21. Bitwise NOT Assignment
# 22. Left Shift Assignment
# 23. Right Shift Assignment
# 24. Bitwise Invert
# 25. Bitwise Invert Assignment