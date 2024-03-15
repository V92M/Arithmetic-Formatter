##Arithmetic Arranger

This Python script arranges simple arithmetic problems for easy visual comparison.

Functionality
The main function, arithmetic_arranger(problems, show_answers=False), takes in a list of arithmetic problems and an optional boolean to indicate whether the answers should be displayed.

The function performs the following checks:

It checks the size of the problem list. If there are more than 5 problems, it raises a ValueError.
It checks the operators within a problem. The operator must be ‘+’ or ‘-’.
It checks if the problem contains only digits.
It checks if the problem contains a number larger than 4 digits.
The function then processes up to 5 problems. For each problem, it checks the operator, checks if the problem contains only digits, and checks the size of the digits.

The function then arranges the problems for display. It creates four lines of output: the first two lines are the operands, the third line is the line of dashes, and the fourth line (which is optional) is the answers.

If the show_answers parameter is set to True, the function also calculates and displays the answers.

Here is a sample usage of the function:

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))

This will output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
