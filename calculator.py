import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
print("The program is running")
print("Welcome to the Python Calculator\n\nEnter an operator: ")
operator = input()

args = input("Enter args separated by commas (ex: 3, 4, 5): ")
newArgs = args.split(',')
#print(newArgs)
x = 0
for arg in newArgs:
    newArgs[x] = arg.replace(" ", "")
    x+=1
#print(newArgs)
