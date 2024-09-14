#  explain the key feature of python that makes it famous among the coders
'''ans: python is famous among the  coders due to several reasons some of them are
given below
Readable Syntax: Python uses indentation to define code blocks instead of braces or keywords.
                This enforces a clean and consistent coding style and helps reduce errors.
Concise Code: Python often allows you to accomplish tasks with fewer lines of code compared to other languages. This brevity can lead to faster development and easier maintenance.

Extensive Standard Library: Python comes with a comprehensive standard library that covers many common programming tasks, which reduces the need to write code from scratch.

'''


#  describe the role of pre defined keywords in python and provide examples of how they are used in a program
''' 
ans:
In Python, predefined keywords are reserved words that have specific meanings and roles within the language. They cannot be used for variable names or identifiers because they are part of Python's syntax and language rules. These keywords are essential for defining the structure and control flow of Python programs.

Here’s an overview of some common predefined keywords and their roles, along with examples of how they are used in a program:'''



def greet(name):
    return f"Hello, {name}!"

print(greet("mayank"))



#  discuss different type of operators in python and provide examples of how thet are used
'''
ans:
In Python, operators are special symbols that perform operations on values or variables. They are categorized into several types, each serving a different purpose. Here’s a breakdown of the various types of operators in Python, along with examples of how they are used:

1. Arithmetic Operators
These operators are used for basic arithmetic operations.

Addition (+)


a = 5
b = 3
result = a + b  # result is 8
Subtraction (-)


result = a - b  # result is 2
Multiplication (*)

result = a * b  # result is 15
Division (/)


result = a / b  # result is 1.6667
Floor Division (//)


result = a // b  # result is 1
Modulus (%)

python
Copy code
result = a % b  # result is 2
Exponentiation (**)


result = a ** b  # result is 125
2. Comparison Operators
These operators are used to compare two values.

Equal to (==)

result = (a == b)  # result is False
Not equal to (!=)


result = (a != b)  # result is True
Greater than (>)


result = (a > b)  # result is True
Less than (<)

result = (a < b)  # result is False
Greater than or equal to (>=)


result = (a >= b)  # result is True
Less than or equal to (<=)


result = (a <= b)  # result is False
3. Logical Operators
These operators are used to perform logical operations.

Logical AND (and)


x = True
y = False
result = x and y  # result is False
Logical OR (or)


result = x or y  # result is True
Logical NOT (not)


result = not x  # result is False
4. Assignment Operators
These operators are used to assign values to variables.

Assignment (=)


x = 10  # x is 10
Addition Assignment (+=)


x += 5  # x is now 15
Subtraction Assignment (-=)


x -= 3  # x is now 12
Multiplication Assignment (*=)


x *= 2  # x is now 24
Division Assignment (/=)


x /= 4  # x is now 6.0
Modulus Assignment (%=)


x %= 5  # x is now 1.0
Exponentiation Assignment (**=)


x **= 3  # x is now 1.0
Floor Division Assignment (//=)

x //= 2  # x is now 0.0
5. Bitwise Operators
These operators perform bit-level operations.

Bitwise AND (&)


a = 6  # binary: 110
b = 3  # binary: 011
result = a & b  # result is 2 (binary: 010)
Bitwise OR (|)


result = a | b  # result is 7 (binary: 111)
Bitwise XOR (^)


result = a ^ b  # result is 5 (binary: 101)
Bitwise NOT (~)


result = ~a  # result is -7 (binary: -111)
Bitwise Shift Left (<<)

result = a << 1  # result is 12 (binary: 1100)
Bitwise Shift Right (>>)

result = a >> 1  # result is 3 (binary: 011)
6. Membership Operators
These operators check for membership in sequences like lists, tuples, and strings.

In (in)


fruits = ['apple', 'banana', 'cherry']
result = 'banana' in fruits  # result is True
Not In (not in)



result = 'grape' not in fruits  # result is True
7. Identity Operators
These operators compare the memory locations of two objects.

Is (is)



x = [1, 2, 3]
y = x
result = x is y  # result is True
Is Not (is not)



z = [1, 2, 3]
result = x is not z  # result is True
Each type of operator has its specific use cases, and understanding them is crucial for writing effective Python code.'''



#  explain the concept of type casting in the python with example
'''
ans:
Type casting in Python refers to the conversion of a variable from one data type to another. This is a common operation when you need to perform operations that require different data types or when you need to ensure that values are in a specific format. Python provides several built-in functions for type casting, each designed to convert a value to a particular type.'''
#  there are two type of type casting
#  implicit and explicit
#  example:
float_value = 12.56
int_value = int(float_value)  # Converts 12.56 to 12
print(int_value)


#  how conditional statements work in python ? ilustrate woth example
'''
ans:
Conditional statements in Python allow you to execute certain blocks of code based on whether a condition is true or false. The primary conditional statements in Python are if, elif, and else.
if Statement: This is used to check a condition. If the condition is true, the block of code following the if statement is executed.

elif Statement: This stands for "else if" and is used to check additional conditions if the previous if or elif conditions were not true. You can have multiple elif statements.

else Statement: This is used to execute a block of code if none of the preceding conditions were true. It is optional and only used when you want to handle all remaining cases.'''


#  example:


score = int(input(" enter the score here "))


if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")





#  describe differetn type of loops in python and their use case with examples
'''
ans:
In Python, loops are used to execute a block of code repeatedly based on certain conditions. Python primarily supports two types of loops:

for Loop
while Loop
1. for Loop
The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range). It executes a block of code once for each item in the sequence. 

for variable in sequence:
    # code to execute for each item


Use Cases
Iterating through elements of a list or other iterable collections.
Executing a block of code a specific number of times using range
'''
# example

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

'''
2. while Loop
The while loop executes a block of code as long as a specified condition is true. The condition is evaluated before each iteration
syntax:
while condition:
    # code to execute while the condition is true
Use Cases
When the number of iterations is not known beforehand and depends on some condition.
Continuously checking and performing actions until a condition changes.'''

count = 0

while count < 5:
    print(count)
    count += 1







