# algebra-calculator

This program currently has the capability to
* solve simple algebraic expressions
* find the factors of quadratic equations

In the future I plan to add the ability to solve for different variables given an equation.

## Examples:
<img width="1233" height="587" alt="Screenshot 2025-12-26 184859" src="https://github.com/user-attachments/assets/f9603b42-3377-44e0-b3c0-29a9ff13dfa9" />

The calculator follows the correct order of operations (PEMDAS) before outputting the result. Parentheses are currently not supported, but I plan to add functionality for them in a future version.

\
<img width="1020" height="766" alt="Screenshot 2025-12-26 185758" src="https://github.com/user-attachments/assets/9d6ca9d8-e820-4ed4-9239-208224689340" />

The user will be asked to input the values for any variables in their expression. If a variable appears multiple times, the user will still only be prompted once. The calculator will then plug in these user values and follow PEMDAS, taking care of any exponents before multiplying the coefficients. 

\
<img width="846" height="456" alt="Screenshot 2025-12-26 195319" src="https://github.com/user-attachments/assets/7e834ea6-b885-44ac-907c-01ce8b5fe187" />

If a quadratic expression entered by the user is factorable, the calculator will set the expression equal to 0 and use the quadratic formula to find the solutions. These solutions will be printed in the form (x - {s1}) (x - {s2}).
