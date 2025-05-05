print("--------------------------------|")
print("--------------------------------|\nHello String Chapter....")
print("--------------------------------|")

# What is string.......?
# Strings are written in single 'string', double "string" or tripple """string""" quotation mark. It (string - collection of words) are printed as it is (Like Someone has said in English language) کسی کی بات کو نقل کرنا


print("Hellow World (Error)")       # This is an error in string, and this is cannot be detect and fix by python interpreter by itself but we have to remove manually.... like the below:
print("Hello World (Correct)")

print('We are learning python with Dr Aammar on Codanics')  # Single Quotation mark....

# Why multi representation used in string?
print("Hello Learner.......! This is 'MUHAMMAD IDREES'")
print('''
--------------------------------
This is multiline string
Hey! This is TDF - TechDevFamily Leader!
I hope this message find you well.
Take Care
''')

# As a Professional use We have to use double quotation in most cases
# `` called bactics and use to show code separately from other text in markdown language. And we will see this in upcoming chapters
# 
# ------------------------------------------!
print('''
This is a
Tripple single (Multiline)
Quotation mark
''')

print("""
And This is a Tripple Double
(Multiline) Quotation mark
""")

# Numbering in string
print(2 + 3)
print("2+3+5-4")

# What is Type Casting in programming
# Converting one data type into another, is called type casting
# Example:
stringNum = "29"
print(type(stringNum))      # This will probably print <class 'str'> means, variable belongs to 'string class'
print("----------------------")

# Now, we are trying to convert it into integer to perform arithmatic operation (that we can't do on string type)
# Example:
myAge = 25
try:
    print(myAge + stringNum)        # Error: Unsupported operand type(s) for +: 'int' and 'str'
    print("----------------------")
except TypeError as e:
    print(f"Something went wrong\nError Message: '{e}'\n-------------------")

# Solution:
stringNum = int(stringNum)
try:
    answer = myAge + stringNum            # the method 'int()' will convert 'string' into 'int' type
    print(f"The Problem is resolved and the answer is\n{answer}")

except TypeError as e:
    print(f"Something went wrong...\nError Message: {e}")


print("----------------------")
# -------------------------------------------------------------------------------

# Another Type Casting Example:-    from 'int' to 'String'
myIntVar = 100
# The below statement  will print <class 'int'>, which means it's belongs to int data type
print(f"Type of myIntVar = {type(myIntVar)}")

# Conversion 'int' to 'String':-
myStringVar = str(myIntVar)

# Result Printing...
print(f"Type of New variable 'myStringVar' = {type(myStringVar)}")
# Now this will print <class 'str'> which means string data type

# -------------------------------------------------------------------------------





print("--------------------------------|")
