# This is a simple calculator program, it takes input and outputs an answer
# Carlos Alvarez 1/30/2026
#This is 99% a safe program to run but be cautious with eval usage
import math
safe_dict = {"sqrt": math.sqrt,} #Dictionary of safe functions
allowed_chars = "0123456789+-*/.()sqrt" #Allowed characters for safety
while True:
    query = input("Enter a Math Expression: ").replace(" ","").lower() #Input
    if len(query) > 100: #Length check
        print("Error: Input too long!")
        continue
    if len(query) == 0: #Empty input check
        print("Error: No Input!")
        continue
    if query.lower() == "exit": #Exit condition
        break
    is_safe = all(char in allowed_chars for char in query) # Logic Check
    if is_safe and "**" not in query: #Extra check to prevent power operator
        try:
            answer = eval(query,{"__builtins__": {}}, safe_dict) #Safely evaluate the expression with some caveats
            print(answer) #Output
        except (SyntaxError, ZeroDivisionError, OverflowError): #Catches common errors
            print("Error Invalid Input!")
    else:
        print("Error Invalid Input!") #If not safe, output error   