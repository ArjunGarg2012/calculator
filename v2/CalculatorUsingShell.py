import math

print("\nARJUN'S CALCULATOR\n"
      "Enter the expression you want the answer of\n"
      "Seperate the numbers and the symbol by spaces\n"
      "Press (Q) to quit once your done\n"
      "\n"
      "BEWARE\n"
      "\n"
      "Errors will completely stop the code and if you use to many digits, it will result in an error")
while True:
    calculation_input = input("> ")
    calculation = calculation_input.split()
    
    if calculation[1] == "+":
        answer = float(calculation[0]) + float(calculation[2])
        print("The sum is", answer)
    
    elif calculation[1] == "-":
        difference = float(calculation[0]) - float(calculation[2])
        print("The difference is", difference)
        
    elif calculation[1] == "*" or calculation[1] == "x":
        product = float(calculation[0]) * float(calculation[2])
        print("The product is", product)
        
    elif calculation[1] == "/" or calculation[1] == "÷":
        quotient = float(calculation[0]) / float(calculation[2])
        print("The quotient is", quotient)
        
    elif calculation[1] == "^":
        answer = math.pow(float(calculation[0]), float(calculation[2]))
        print("The answer is", answer)
        
    elif calculation[0] == "Q" or calculation[0] == "q":
        print("Thank you for using my calculator!")
        break