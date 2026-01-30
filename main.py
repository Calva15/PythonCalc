# This is a simple calculator program, it takes input and outputs an answer
# Carlos Alvarez 1/30/2026
#This is not a safe program to run because eval can be used to run code, but for something simple like this
#It gets the job done.
allowed_chars = "0123456789+-*/.()" #Allowed characters for safety
query = input("Enter a Math Expression: ").replace(" ","") #Input
is_safe = all(char in allowed_chars for char in query) # Logic Check
if is_safe and "**" not in query: #Extra check to prevent power operator
    try:
        answer = eval(query) #Safely evaluate the expression with some caveats
        print(answer) #Output
    except (SyntaxError, ZeroDivisionError, OverflowError): #Catches common errors
        print("Error Invalid Input!")
else:
    print("Error Invalid Input!") #If not safe, output error