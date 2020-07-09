import definitions
from math import *
def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom    # Returns the slope to the third decimal
    return int(float("%.3f" % slope))
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
print("The program is running")
print("Welcome to the Python Derivative Calculator\n\nTo Begin, Enter an expression (format: n * x ^ p + n * x ^ p): ")
expression = input()
args = expression.split()
# print(expression)
# formattedExpression = 0
# print(type(int('string')))
#for char in expression:
def f(n):
    newExp = 0
    counter = 0
    while counter < len(args):
        if args[counter].isdigit():
            if (counter != len(args) - 1) and "^" in args[counter+1]:
                newExp += int(args[counter])**args[counter+2]
                counter += 2
            else:
                newExp += int(args[counter])
        if args[counter] == 'x':
            if (counter != len(args) - 1) and "^" in args[counter+1]:
                newExp += n**args[counter+2]
            else:
                newExp += int(n)
        if args[counter] == '+':
            if args[counter+1] == 'x':
                newExp += n
            else:
                newExp += int(args[counter+1])
            counter+=1
        if args[counter] == '-':
            if args[counter+1] == 'x':
                newExp -= n
            else:
                newExp -= int(args[counter+1])
            counter += 1
        if args[counter] == '*':
            if args[counter+1] == 'x':
                newExp *= n
            else:
                newExp *= int(args[counter+1])
            ++counter
        if args[counter] == '/':
            if args[counter+1] == 'x':
                newExp = newExp / n
            else:
                newExp = newExp / int(args[counter+1])
            counter+=1
        counter += 1
    print(newExp)
    return newExp
value = int(input("Enter an x value of the derivative: "))
print(derive(f, value))