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

# -------------------------------------------------------------------------------#
# Using single & double quotation together
print("What's up....?")

# --------------------------------------------------------------------------------#

# Mostly data are mostly existed in the form of numeric and string
# Boolean operators and Binary data

# Boolean Operators----!
# Boolean Operators are words (like AND, OR, NOT) and symbols used to refine searches in databases and search engines, allowing us to narrow or broaden our search results

# Binary Data----!
# A data which has two possible occurances (i.e. 0 and 1)
# It's raining.
# You are not working.






print("--------------------------------|")
print("----------------------------------------------------------------->>>\n")
print("------------------------ KAGGLE PRACTICE ------------------------>>>\n")
print("----------------------------------------------------------------->>>\n")


# Random Activities - To familier you with new upcoming topics and concepts
planet = "Pluto is a planet"
print("--------------------")
print('My Name is \'MUHAMMAD IDREES\'')         # Here a single quote is used separatly

# String Methods
print("-----------------------------------------\n")
# 1. Indexing
print("1. string Indexing")
print("------------------")
print(planet[0])
print("-----------------------------------------\n")


# String Slicing                # Separate a part of a string
print("2. strring slicing")
print("------------------")
print(planet[-3:])
print("-----------------------------------------\n")


# String length                 # determining length of a string
print("3. String length")
print("------------------")
print(len(planet))
print("-----------------------------------------\n")


# Loop over String
print("4. Looping over String")
print("----------------------")
print([char + '!' for char in planet])
print("-----------------------------------------\n")


# String UPPER CASE
print("5. str.upper()")
print("-----------")
print(planet)

print(planet.upper())           # No return value
print("-----------------------------------------\n")


# String lower case
print("6. str.lower()")
print("--------------")
print(planet)
print(planet.lower())           # No return value
print("-----------------------------------------\n")


# String Searching for the first index of a substring
print("7. Searching for the first index of a substring")
print("----------------")
print(planet)
print(planet.index('plan'))
print("-----------------------------------------\n")




# String are immutable              # Their elemnt can't be changed once declared
print("8. String are immutable")
print("-----------------------")
print("Before: \n", planet)

# Here we are using try and except (with 'TypeError' attribute) block to handle an error
try:
    planet[0] = 'B'                     # We are trying to replace the 'P' with 'B'
except TypeError as e:
    print(f"String are immutable in Python!\nError Message: {e}")
    print("------------")

print("After: \n", planet)
# planet.append doesn't work either on string
print("--------------------------------------------")


# String startswith()
print("9. string startswith()")
print("-----------------")
print(planet)
print(planet.startswith("planet"))
print("-----------------------------------------\n")


# String endswith()
print("10. string endswith()")
print("---------------------")
print(planet)
print(planet.endswith("planet!"))           # False
print(planet.endswith("planet"))            # True
print("----------------------------------------------------------------->>>\n")


# Goint between strings and lists: .split() and .join()

# str.split() turns a string into a list of smaller strings, breaking on whitespace by default.
words = planet.split()
print(words)
print(type(words))


# Occasionally we will want to split on something other than whitespace:
date_str = '14-08-2002'
day, month, year = date_str.split('-')
print("------------------")
print(f"My Date of Birth\n{day}/{month}/{year}")
print("-----------------------------------------")
print("----------------------------------------------------------------->>>\n")

# Can we do split() on current string?
new_string = "Hello Python! This is 'MUHAMMAD IDREES', currently learning python computer language from KAGGLE online"
print(new_string)
print(type(new_string))

new_string = new_string.split()
print(new_string)
print(type(new_string))
print("----------------------------------------------------------------->>>\n")


# str.join()    takes us in the other direction, sewing a list of strings up into one long string, using the string it was called on as a separator.
my_dob_list = [day, month, year]
print(my_dob_list)

# Now converting it into a string using str.join()
my_dob_str = '🤔'.join(my_dob_list)                     # Litrally, we can use emojies here
print(my_dob_str)
print("----------------------------------------------------------------->>>\n")


# strings with multiple other string methods
print(words)        # This is a list right now...

# convert it into a string and in UPPERCASE
words = ' '.join([word.upper() for word in words])

print(words)
print(type(words))
print("----------------------------------------------------------------->>>\n")


# Building string with .format()
# Python lets us concatenate string with a '+' operator.
planet = words
print(planet.capitalize())

# Concatenation...
new_concatnt_str = planet + f'. I Love You, {"Pluto"}!'

print(new_concatnt_str)

# If we want to throw in any non-string objects, we have to be careful to call str() on them first
position = 9

try:
    concat_str = planet + ", you'll always be the " + position + "th planet to me."
    print(concat_str)
except TypeError as e:
    print(f"In 'Python', String can't be concatenate with integer!\nError: {e}")
print("------------------->>\n")

# To resolve the above problem, we performing the below step...
new_concatnt_str = planet + ", you'll always be the " + str(position) + "th planet to me."
print(new_concatnt_str)
print("------------------->>\n")

# The above statement is getting hard to read and annoying to type. str.format() to the rescue. So, we are performing the below statement:
new_concatnt_str = "{}, you'll always be the {}th planet to me.".format(planet, position)
print(new_concatnt_str)
print("----------------------------------------------------------------->>>\n")


# So much cleaner! We call .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.
# Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us.

# If that was all that format() did, it would still be incredibly useful. But as it turns out, it can do a lot more. Here's just a taste:
# Small Activity:
planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

#   2 decimal points    3 decimal points,   format as percent   separate with commas
new_compact_concat_of_str = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

print(new_compact_concat_of_str)
print("---------------------->\n")

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')

print(s)

# Another Example
my_str_10 = """This is {0}.
No, It's {1}.
No, It's neigther {0}, and nor {1}, but It's {2}""".format('MUHAMMAD IDREES', 'FAIZAN', 'HAMZA')

print(my_str_10)

# You could probably write a short book just on str.format, so I'll stop here, and point you to pyformat.info {https://pyformat.info/} and the official docs {https://docs.python.org/3/library/string.html#formatstrings} for further reading.