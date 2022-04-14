import math

print("\nARJUN'S CALCULATOR\n"
      "Enter the expression you want the answer of\n"
      "\n"
      "BEWARE\n"
      "\n"
      "Errors will completely stop the code and if you use to many digits, it will result in an error")
while True:
    expression = input("> ")
    before_symbol = ""
    after_symbol = ""
    symbol = ""
    symbol_seen = False
    if expression.upper() == 'Q':
        break
        
    for a in expression:
        if a == "+" or a == "-" or a == "*" or a == "x" or a == "/" or a == "÷" or a == "^":
            symbol = a
            symbol_seen = True
        
        elif symbol_seen == False:
            before_symbol = before_symbol + a
            
        elif symbol_seen == True:
            after_symbol = after_symbol + a
            
    if symbol == "+":
        print(float(before_symbol) + float(after_symbol))
            
    if symbol == "-":
        print(float(before_symbol) - float(after_symbol))
            
    if symbol == "*" or symbol == "x":
        print(float(before_symbol) * float(after_symbol))
            
    if symbol == "÷" or symbol == "/":
        print(float(before_symbol) / float(after_symbol))
            
    if symbol == "^":
        print(math.pow(float(before_symbol) + float(after_symbol)))
