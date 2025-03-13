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
print(a % b)  # Output: 2


# 6. Exponentiation
print(a ** b)  # Output: 125


# 7. Floor Division
print(a // b)  # Output: 1
# ------------------------------------------------------->


# -------------------------->
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

# Here is the code snippet from the file with the PEMDAS test:

# python
print("PEMDAS Test...")
print(3 ** 2 / 2 * 3 / 3 + 6 - 4 / (2 * 6))

# Step by step calculation:
# -------------------------->
print("Step by step calculation...")
print(2 * 6)
print(3 ** 2)
print(3 ** 2 / 2)
print(3 ** 2 / 2 * 3)
print(3 ** 2 / 2 * 3 / 3)
print(4 / 12)
print(3 ** 2 / 2 * 3 / 3 + 6)
print(3 ** 2 / 2 * 3 / 3 + 6 - 4 / (2 * 6))
# Output:
# 12
# 9
# 4.5
# 13.5
# 4.5
# 0.3333333333333333
# 10.5
# 10.166666666666666
# The output of the above code will be:

# '10.166666666666666' as explained.
# ---------------------------------------------------------------------------------------------->




# ------------------------------------------------->
# Advanced Operators
print("Advanced Operators...")
# ----------------------------------->
# 8. Bitwise AND
print("Bitwise AND...")
# ----------------------------------->
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print(x & y)  # Output: 0 (0000 in binary)
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise AND operator compares the binary representation of two numbers and returns a new number where each bit is set to 1 if both bits are 1 in the corresponding positions, otherwise, it sets the bit to 0.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise AND operation between these two numbers, we get '0000' which is equal to 0 in decimal.
# ----------------------------------->

# More Examples:
print("--------------------------------\nBitwise AND - More Examples:")
m = 12  # 01100 in binary
n = 20  # 10100 in binary
print(m & n)

m = 28  # 01100 in binary
n = 20  # 10100 in binary
print(m & n)
# ----------------------------------->


# 9. Bitwise OR
print("Bitwise OR...")
# ----------------------------------->
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print(x | y)  # Output: 14 (1110 in binary)
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise OR operator compares the binary representation of two numbers and returns a new number where each bit is set to 1 if at least one of the bits is 1 in the corresponding positions, otherwise, it sets the bit to 0.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise OR operation between these two numbers, we get '1110' which is equal to 14 in decimal.
# ----------------------------------->

# More Examples:
print("--------------------------------\nBitwise OR - More Examples:")
c = 14  # 1110
d = 9   # 1001
# ----------------------------------->

# 10. Bitwise XOR
print("Bitwise XOR...")
# ----------------------------------->
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print(x ^ y)  # Output: 14 (1110 in binary)
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise XOR operator compares the binary representation of two numbers and returns a new number where each bit is set to 1 if the bits are different in the corresponding positions, otherwise, it sets the bit to 0.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise XOR operation between these two numbers, we get '1110' which is equal to 14 in decimal.
# ----------------------------------->
# ----------------------------------->


# 11. Bitwise NOT
print("Bitwise NOT...")
# ----------------------------------->
x = 10  # 1010 in binary
print(~x)  # Output: -11
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise NOT operator inverts the bits of a number, changing 1s to 0s and 0s to 1s.
# In this case, the binary representation of 10 is '1010'. When we perform a bitwise NOT operation on 10, we get '-11' in decimal.
# ----------------------------------->
# ----------------------------------->


# 12. Left Shift
print("Left Shift...")
# ----------------------------------->
x = 10  # 1010 in binary
print(x << 1)  # Output: 20 (10100 in binary)
# ----------------------------------->
# Explanation:
# ------------>
# The left shift operator shifts the bits of a number to the left by a specified number of positions, adding zeros to the right.
# In this case, the binary representation of 10 is '1010'. When we perform a left shift operation on 10 by 1 position, we get '10100' which is equal to 20 in decimal.
# ----------------------------------->
# ----------------------------------->

# 13. Right Shift
print("Right Shift...")
# ----------------------------------->
x = 10  # 1010 in binary
print(x >> 1)  # Output: 5 (101 in binary)
# ----------------------------------->
# Explanation:
# ------------>
# The right shift operator shifts the bits of a number to the right by a specified number of positions, discarding the bits that are shifted off.
# In this case, the binary representation of 10 is '1010'. When we perform a right shift operation on 10 by 1 position, we get '101' which is equal to 5 in decimal.
# ----------------------------------->
# ----------------------------------->

# 14. Multiplication Assignment
print("Multiplication Assignment...")
# ----------------------------------->
x = 5
x *= 3
print(x)  # Output: 15
# ----------------------------------->


# 15. Division Assignment
print("Division Assignment...")
# ----------------------------------->
x = 15
x /= 3
print(x)  # Output: 5.0
# ----------------------------------->

# 16. Modulus Assignment
print("Modulus Assignment...")
# ----------------------------------->
x = 15
x %= 4
print(x)  # Output: 3
# ----------------------------------->

# 17. Exponentiation Assignment
print("Exponentiation Assignment...")
# ----------------------------------->
x = 2
x **= 3
print(x)  # Output: 8
# ----------------------------------->

# 18. Bitwise AND Assignment
print("Bitwise AND Assignment...")
# ----------------------------------->
x = 10
x &= 4
print(x)  # Output: 0
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise AND assignment operator performs a bitwise AND operation between two numbers and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise AND operation between these two numbers, we get '0000' which is equal to 0 in decimal.
# The result of the bitwise AND operation is then assigned to the variable x, so x becomes 0.
# ----------------------------------->

# 19. Bitwise OR Assignment
print("Bitwise OR Assignment...")
# ----------------------------------->
x = 10
x |= 4
print(x)  # Output: 14
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise OR assignment operator performs a bitwise OR operation between two numbers and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise OR operation between these two numbers, we get '1110' which is equal to 14 in decimal.
# The result of the bitwise OR operation is then assigned to the variable x, so x becomes 14.
# ----------------------------------->

# 20. Bitwise XOR Assignment
print("Bitwise XOR Assignment...")
# ----------------------------------->
x = 10
x ^= 4
print(x)  # Output: 14
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise XOR assignment operator performs a bitwise XOR operation between two numbers and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010' and the binary representation of 4 is '0100'. When we perform a bitwise XOR operation between these two numbers, we get '1110' which is equal to 14 in decimal.
# The result of the bitwise XOR operation is then assigned to the variable x, so x becomes 14.
# ----------------------------------->

# 21. Bitwise NOT Assignment
print("Bitwise NOT Assignment...")
# ----------------------------------->
x = 10
x = ~x
print(x)  # Output: -11
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise NOT assignment operator inverts the bits of a number and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010'. When we perform a bitwise NOT operation on 10, we get '-11' in decimal.
# The result of the bitwise NOT operation is then assigned to the variable x, so x becomes -11.
# ----------------------------------->

# 22. Left Shift Assignment
print("Left Shift Assignment...")
# ----------------------------------->
x = 10
x <<= 1
print(x)  # Output: 20
# ----------------------------------->
# Explanation:
# ------------>
# The left shift assignment operator shifts the bits of a number to the left by a specified number of positions and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010'. When we perform a left shift operation on 10 by 1 position, we get '10100' which is equal to 20 in decimal.
# The result of the left shift operation is then assigned to the variable x, so x becomes 20.
# ----------------------------------->


# 23. Right Shift Assignment
print("Right Shift Assignment...")
# ----------------------------------->
x = 10
x >>= 1
print(x)  # Output: 5
# ----------------------------------->
# Explanation:
# ------------>
# The right shift assignment operator shifts the bits of a number to the right by a specified number of positions and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010'. When we perform a right shift operation on 10 by 1 position, we get '101' which is equal to 5 in decimal.
# The result of the right shift operation is then assigned to the variable x, so x becomes 5.
# ----------------------------------->


# 24. Bitwise Invert
print("Bitwise Invert...")
# ----------------------------------->
x = 10
print(~x)  # Output: -11
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise invert operator inverts the bits of a number, changing 1s to 0s and 0s to 1s.
# In this case, the binary representation of 10 is '1010'. When we perform a bitwise invert operation on 10, we get '-11' in decimal.
# ----------------------------------->

# 25. Bitwise Invert Assignment
print("Bitwise Invert Assignment...")
# ----------------------------------->
x = 10
x = ~x
print(x)  # Output: -11
# ----------------------------------->
# Explanation:
# ------------>
# The bitwise invert assignment operator inverts the bits of a number and assigns the result to the left operand.
# In this case, the binary representation of 10 is '1010'. When we perform a bitwise invert operation on 10, we get '-11' in decimal.
# The result of the bitwise invert operation is then assigned to the variable x, so x becomes -11.
# ----------------------------------->
# ----------------------------------->
# ------------------------------------------------->
# ------------------------------------------------->