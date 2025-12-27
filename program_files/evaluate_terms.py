# evaluate terms like 2^2
def evaluate_const_to_pow (term) :
    parts = term.split("^")
    try :
        result = pow(float(parts[0]), float(parts[1]))
        return result
    except :
        print(f"Error! The result of {term} is too large!")
        return 1

# Evaluates terms like "10xy", editing the original equation with the new constant values.
def evaluate_terms(variables, equation) :

    pass_counter = 0
    digit_counter = 0
    known_vars = []
    var_values = []
    terms : float = []

    for var in variables :
        temp_value = None
        for i in range(len(var)) :
            
            # Pass over this index if it has already been evaluated
            if (pass_counter > 0) :
                pass_counter -= 1
                continue

            # If this index is a variable such as "x"
            if (var[i].isalpha()) :

                # Handle evaluation for newly initialized variables
                if var[i] not in known_vars:
                    this_var = float(input(f"What is {var[i]} equal to? \n"))
                    known_vars.append(var[i])
                    var_values.append(this_var)

                # Handle evaluation for known variables
                else :
                    this_var = var_values[known_vars.index(var[i])]
                    
                # Check if this variable should be raised to a power
                try :
                    if (var[i+1] == "^") :
                        
                        # Check to see how many digits the exponent has
                        j = 2
                        exponent_length = 0
                        while (i + j < len(var) and var[i + j].isdigit()) :
                            exponent_length += 1
                            j += 1
                           
                        # Handle power evaluation (x^2) or no exponent error (x^_)
                        if (exponent_length > 0) :

                            # Build a string of the form "const^const" or "2^2"
                            # We already have a method to evaluate this
                            exp_start = (i+2)
                            exp_end = (i+2+exponent_length)
                            exponent = var[exp_start : exp_end]
                            this_var = evaluate_const_to_pow(str(this_var)+"^"+exponent)
                            
                        else :
                            print("Error! Exponent expected but not found!")

                        # Set pass counter to exponent length + 1 to pass over 
                        # that many indexes of var. Used to pass over "^2"
                        pass_counter = exponent_length + 1

                except :
                    pass

                # If there is a value from before, multiply x and that value
                if (digit_counter > 0) :
                    temp_value = this_var * float(var[0 : digit_counter])
                    digit_counter = 0

                # If there is a variable from before, multiply x and that variable
                elif (temp_value != None) :
                    temp_value = this_var * temp_value

                # If there is no value from before, just store x.
                elif (temp_value == None) :
                    temp_value = this_var
                
            # If this index is a number, increment digit counter
            elif (var[i].isdigit()) :
                digit_counter += 1

        # If this index is the last index in the variable, store the final result in the terms list
        terms.append(temp_value)

            
    # Find all the variables in the main equation and replace them with known values
    j = 0
    for i in range(len(equation)) :
            if (equation[i] == "V") :
                    
                equation[i] = terms[j]
                j += 1

    return