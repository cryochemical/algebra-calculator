
# Simplify takes a list 'equation' and simplifies it using a given operator. This means it is copying values 
# from a long list to indexes on a new, shorter list, with lots of added rules.
def simplify(equation, operator1 : str, operator2 : str) :

    simplified_equation = []
    
    for i in range(len(equation)) :

        # Check for the operators I want. If found, simplify and pass the new value to the right.
        if (equation[i] == operator1) :
            equation[i + 1] = eval(f"{equation[i - 1]} {operator1} {equation[i + 1]}")
        elif (equation[i] == operator2) :
            equation[i + 1] = eval(f"{equation[i - 1]} {operator2} {equation[i + 1]}")

        # Check for other operators. If found, store the values at the previous and current index of equation.
        elif (isinstance(equation[i], float) == False) :
            simplified_equation.append(equation[i - 1])
            simplified_equation.append(equation[i])
            
        # Check to see if the end of the equation has been reached. If true, store the value at the final index.
        if (i == len(equation) - 1) :
            simplified_equation.append(equation[i])

    return(simplified_equation)

def solve(equation) :

    final_equation = []

    final_equation = simplify(equation, "*", "/")
    #print(f"Final equation after * and / : {final_equation}")
    
    print("After multiplication and division:")
    print(final_equation)

    final_equation = simplify(final_equation, "+", "-")
    #print(f"Final equation after + and - : {final_equation}")

    print("After addition and subtraction:")
    print(final_equation)

    if not final_equation :
        return equation
    return final_equation