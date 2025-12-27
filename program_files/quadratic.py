import math

# Note: There are still some corner cases to check for
def factor_quadratic(vars, constants, operators) :

    digit_counter = 0
    a = 1
    b = 1
    c = 0
    
    # Check to see what a is
    for i in vars[0] :
        if (i.isdigit()) :
            digit_counter += 1
        else :
            if (digit_counter > 0) :
                a = float(vars[0][0 : digit_counter])
                
    digit_counter = 0

    # b = 0 in the form (ax^2 + c)
    if (len(vars) == 1) :
        b = 0

    # find b in the form (ax^2 + bx + c)
    elif (len(vars) == 2) :
                
        # Check to see what b is
        for i in vars[1] :
            if (i.isdigit()) :
                digit_counter += 1
            else :
                if (digit_counter > 0) :
                    b = float(vars[1][0 : digit_counter])
                    digit_counter = 0
        
    else :
        print("Please use the expression form: ax^2 + bx + c ")
    
    # c is either a positive or negative constant
    try: 
        if (operators[len(vars) - 1] == "+") :
            c = constants[0]
        elif (operators[len(vars) - 1] == "-") :
            c = constants[0] * -1
        else :
            print("Please only use '+' or '-' in your quadratic expression! ")
    except :
        pass

    try:
        answer1 = round((-b + math.sqrt(b * b - (4 * a * c))) / (2 * a), 4)
        answer2 = round((-b - math.sqrt(b * b - (4 * a * c))) / (2 * a), 4)

        print(f"{a}x^2 + {b}x + {c} = {a}(x + {answer1 * -1})(x + {answer2 * -1})")
    
    except:
        print("This quadratic expression is not factorable ")

    return 
