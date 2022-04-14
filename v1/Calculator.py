import math
import numpy

print("\nARJUN'S CALCULATOR\n"
      "Enter (A) to Add\n"
      "Enter (S) to Subtract\n"
      "Enter (M) to Multiply\n"
      "Enter (D) to Divide\n"
      "Enter (SQ) to Calculate Square\n"
      "Enter (C) to Calculate Cube\n"
      "Enter (SQRT) to Calculate Square Root\n"
      "Enter (CBRT) to Calculate Cube Root\n"
      "Enter (EX) for Exponents\n"
      "Enter (Q) to Quit\n")
while True:
    choice = input("> ")

    if choice.upper() == 'A':
        num_1 = float(input("Enter first value: "))
        num_2 = float(input("Enter second value: "))
        add = num_1 + num_2
        print("The sum is", add)

    elif choice.upper() == 'S':
        num_1 = float(input("Enter first value: "))
        num_2 = float(input("Enter second value: "))
        subtract = num_1 - num_2
        print("The difference is", subtract)

    elif choice.upper() == 'M':
        num_1 = float(input("Enter first value: "))
        num_2 = float(input("Enter second value: "))
        multiplication = num_1 * num_2
        print("The product is", multiplication)

    elif choice.upper() == 'D':
        num_1 = float(input("Enter first value: "))
        num_2 = float(input("Enter second value: "))
        division = num_1 / num_2
        print("The quotient is", division)

    elif choice.upper() == 'SQ':
        num_1 = float(input("Enter the number: "))
        square = num_1 * num_1
        print("The square is", square)

    elif choice.upper() == 'C':
        num_1 = float(input("Enter the number: "))
        cube = num_1 * num_1 * num_1
        print("The cube is", cube)

    elif choice.upper() == 'SQRT':
        num_1 = float(input("Enter the number: "))
        square_root = math.sqrt(num_1)
        print("The square root is", square_root)

    elif choice.upper() == 'CBRT':
        num_1 = float(input("Enter the number: "))
        cube_root = numpy.cbrt(num_1)
        print("The cube root is", cube_root)

    elif choice.upper() == 'EX':
        num_1 = float(input("Enter base(lower and bigger number): "))
        num_2 = float(input("Enter exponent(higher and smaller number): "))
        value = math.pow(num_1, num_2)
        print("The value is", value)

    elif choice.upper() == 'Q':
        print("Thanks for using my calculator\n"
              "Bye...")
        break

    else:
        print("Wrong Value Entered\n"
              "Try Again")