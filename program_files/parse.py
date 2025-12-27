from evaluate_terms import evaluate_const_to_pow

# Checks if a string contains at least one alphabetic character
def contains_alpha(input_string):
  return any(c.isalpha() for c in input_string)

def parse(equation : str) :
    
    # Parse the user's equation for constants, variables and operators, 
    # appending them to three lists
    constants = []
    variables : str = []
    operators = []
    all_parts = []

    for part in equation.split() :
        try:
            # This part is a constant if it can be casted to a float
            constants.append(float(part))
            all_parts.append(float(part))

            # Append operators to operator list
        except ValueError:
            if (part == "+"):
                operators.append(part)
                all_parts.append(part)
            elif (part == "-") :
                operators.append(part)
                all_parts.append(part)
            elif (part == "*") :
                operators.append(part)
                all_parts.append(part)
            elif (part == "/") :
                operators.append(part)
                all_parts.append(part)
            # Append variables to variable list
            elif (contains_alpha(part)) :
                variables.append(part)  
                all_parts.append("V")
            # Check for terms like "2^2" which are constants but can't be casted to a float
            elif ("^" in part) :
                this_const = evaluate_const_to_pow(part)
                constants.append(this_const)
                all_parts.append(this_const)
    
    return constants, variables, operators, all_parts
    