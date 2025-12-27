# Stephen Harden Algebra Calculator

# next steps: 
# add functionality for ()
# add complex exponent evaluation like 2x^3y
# let the user input a full equation and solve for different variables

import math
from parse import parse
from evaluate_terms import evaluate_terms
import simplify
from simplify import solve
from quadratic import factor_quadratic

def main():

    user_equation = input("Please enter a mathematical expression: \n")
    total_data = parse(user_equation)

    # Take the total data and split it up between constants,
    # variables and operators.
    constants = total_data[0]
    print("Constants: " + str(constants))
    variables = total_data[1]
    print("Variables: " + str(variables))
    operators = total_data[2]
    print("Operators: " + str(operators))
    equation_parts = total_data[3]
    print("Full Equation:" + str(equation_parts))

    # What should be solved for?
    user_choice = input("1) plug in variables and solve \n2) factor quadratic \n")
    
    # Plug in variables
    if (user_choice == "1") :
        evaluate_terms(variables, equation_parts)
        solution = str(*simplify.solve(equation_parts))
        print(f"Your solution is {solution}")

    # Set quadratic = 0 and solve
    elif (user_choice == "2") :
        factor_quadratic(variables, constants, operators)

main()