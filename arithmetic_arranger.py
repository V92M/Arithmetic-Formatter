import sys

def arithmetic_arranger(problems, show_answers=False):
    

    #Checks Problem List Size
    def checkProblemListSize(problemSize):
            try:
                if problemSize > 5:
                    raise ValueError('Too many problems.')
            except ValueError as e:
                print(f'Error: {e}')
                sys.exit()
                

    
    #Checks the operators within a problem

    def checkProblemOperators(problem):
        operands = "+-"
        if not any(op in problem for op in operands):
            raise ValueError("Operator must be '+' or '-'")
            
            
            
    #Checks if the string only contains digits
    def checkProblemNumbers(problem):
        cleaned_problem = problem.replace("+", "").replace("-", "").replace(" ", "")
        return cleaned_problem.isdigit()
    
    #Checks if the problem contains a number larger than 4 digits
    def checkDigitSize(problem):
           
        cleaned_problem = problem.replace("+", "").replace("-", "")
        split_problem = cleaned_problem.split("  ")
           
        part1 = split_problem[0]
        part2 = split_problem[1]
            
        length_part1 = len(part1)
        length_part2 = len(part2)   
        
        if(length_part1 > 4 or length_part2 > 4):
            sys.exit("Numbers cannot be more than four digits.")
            
        
        
        

              

        
    

    #Variables
    strOne = ''
    strTwo = ''
    strThree = ''
    strFour = ''
    strFive = ''
    
    checkProblemListSize(len(problems))

    for i in range(len(problems)):
            if i == 0:
                strOne += problems[i]
                
                try:
                    checkProblemOperators(strOne)
                except ValueError as e:
                    print(f"Error: {e}")
                    sys.exit()
                    
                
                try:
                    if not checkProblemNumbers(strOne):
                        raise ValueError("Numbers must only contain digits.")
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    checkDigitSize(strOne)
                except IndexError:
                    print("Error: The problem must contain at least two parts separated by spaces.")
                except ValueError as e:
                    print(f"Error: {e}")
                # printResults(strOne,show_answers)
            elif i == 1:
                strTwo += problems[i]
                
                try:
                    checkProblemOperators(strTwo)
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    if not checkProblemNumbers(strTwo):
                        raise ValueError("Numbers must only contain digits.")
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    checkDigitSize(strTwo)
                except IndexError:
                    print("Error: The problem must contain at least two parts separated by spaces.")
                except ValueError as e:
                    print(f"Error: {e}")
                # printResults(strTwo,show_answers)
            elif i == 2:
                strThree += problems[i]
                
                try:
                    checkProblemOperators(strThree)
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    if not checkProblemNumbers(strThree):
                        raise ValueError("Numbers must only contain digits.")
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    checkDigitSize(strThree)
                except IndexError:
                    print("Error: The problem must contain at least two parts separated by spaces.")
                except ValueError as e:
                    print(f"Error: {e}")
               
            elif i == 3:
                strFour += problems[i]
                
                try:
                    checkProblemOperators(strFour)
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    if not checkProblemNumbers(strFour):
                        raise ValueError("Numbers must only contain digits.")
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    checkDigitSize(strFour)
                except IndexError:
                    print("Error: The problem must contain at least two parts separated by spaces.")
                except ValueError as e:
                    print(f"Error: {e}")
                
            elif i == 4:
                strFive += problems[i]
                
                try:
                    checkProblemOperators(strFive)
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    if not checkProblemNumbers(strFive):
                        raise ValueError("Numbers must only contain digits.")
                except ValueError as e:
                    print(f"Error: {e}")
                
                try:
                    checkDigitSize(strFive)
                except IndexError:
                    print("Error: The problem must contain at least two parts separated by spaces.")
                except ValueError as e:
                    print(f"Error: {e}")
        
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    for problem in problems:
        minusSign ='-'
        plusSign = '+'
        problemWidth = '-' 
        whiteSpace1 = ' ' 
        whiteSpace2 = ' ' 
        whiteSpace3 = ' '
        sum = 0
        
            
        if '+' in problem:
            cleaned_problem = problem.replace("+", "")
            split_problem = cleaned_problem.split("  ")
            
                
                
            part1 = split_problem[0]
            part2 = split_problem[1]

            if not part1.isdigit() or not part2.isdigit():
                raise ValueError("Numbers must only contain digits.")
            sum = int(part1) + int(part2)
            sumSize = len(str(sum))
                    # print(part1)
                    # print(part2)

                    

            if len(part1) > len(part2):
                problemWidth *= (len(part1) + 2)
                        # print(problemWidth)
            elif len(part2)  > len(part1):
                problemWidth *= (len(part2) + 2)
                        # print(problemWidth)
            elif len(part2) == len(part1):
                problemWidth *= (len(part2) + 2) 
                        # print(problemWidth)
                    
            if len(part2) == len(part1):
                whiteSpace1 *= 2
                whiteSpace2 *= 1
                    
            if len(part1) == 1:
                if len(part1) == 1 and len(part2) == 2:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                elif len(part1) == 1 and len(part2) == 3:
                    whiteSpace1 *= 4
                    whiteSpace2 *= 1    
                elif len(part1) == 1 and len(part2) == 4:
                    whiteSpace1 *= 5
                    whiteSpace2 *= 1
                    
                    
            elif len(part1) == 2:
                if len(part1) == 2 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                elif len(part1) == 2 and len(part2) == 3:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                elif len(part1) == 2 and len(part2) == 4:
                    whiteSpace1 *= 4
                    whiteSpace2 *= 1

            elif len(part1) == 3:
                if len(part1) == 3 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 3
                elif len(part1) == 3 and len(part2) == 2:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                elif len(part1) == 3 and len(part2) == 4:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                    
            elif len(part1) == 4:
                if len(part1) == 4 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 4
                elif len(part1) == 4 and len(part2) == 2:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 3
                elif len(part1) == 4 and len(part2) == 3:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                    
                    
            line1 += f'{whiteSpace1}{part1}    '
            line2 += f'{plusSign}{whiteSpace2}{part2}    '
            line3 += f'{problemWidth}    '
           
                          

            # print(f'{whiteSpace1}{part1}')
            # print(f'{plusSign}{whiteSpace2}{part2}')
            # print(f'{problemWidth}')
                    
                    

            if show_answers:
                if sumSize == 1:
                    whiteSpace3 *= 2
                elif sumSize == 2:
                    whiteSpace3 *= 2
                elif sumSize == 3:
                    whiteSpace3 *= 2
                elif sumSize == 4:
                    whiteSpace3 *= 1
                # print(f'{whiteSpace3}{sum}')
                line4 += f'{whiteSpace3}{sum}    '
      
               
    
    

                                
                        
                
        if '-' in problem:
            cleaned_problem = problem.replace("-", "")
            split_problem = cleaned_problem.split("  ")
            part1 = split_problem[0]
            part2 = split_problem[1]

            if not part1.isdigit() or not part2.isdigit():
                raise ValueError("Numbers must only contain digits.")

            sum = int(part1) - int(part2)
            if sum < 0:
                sumSize = len(str(sum * -1))
            else:
                sumSize = len(str(sum))
                    # print(sumSize)
                    
                    
            if len(part1) > len(part2):
                problemWidth *= (len(part1) + 2)
                        # print(problemWidth)
            elif len(part2)  > len(part1):
                problemWidth *= (len(part2) + 2)
                        # print(problemWidth)
            elif len(part2) == len(part1):
                problemWidth *= (len(part2) + 2) 
                        # print(problemWidth)
                    
            if len(part2) == len(part1):
                whiteSpace1 *= 2
                whiteSpace2 *= 1
                    
            if len(part1) == 1:
                if len(part1) == 1 and len(part2) == 2:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                elif len(part1) == 1 and len(part2) == 3:
                    whiteSpace1 *= 4
                    whiteSpace2 *= 1    
                elif len(part1) == 1 and len(part2) == 4:
                    whiteSpace1 *= 5
                    whiteSpace2 *= 1
                    
                    
            elif len(part1) == 2:
                if len(part1) == 2 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                elif len(part1) == 2 and len(part2) == 3:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                elif len(part1) == 2 and len(part2) == 4:
                    whiteSpace1 *= 4
                    whiteSpace2 *= 1

            elif len(part1) == 3:
                if len(part1) == 3 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 3
                elif len(part1) == 3 and len(part2) == 2:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                elif len(part1) == 3 and len(part2) == 4:
                    whiteSpace1 *= 3
                    whiteSpace2 *= 1
                    
            elif len(part1) == 4:
                if len(part1) == 4 and len(part2) == 1:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 4
                elif len(part1) == 4 and len(part2) == 2:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 3
                elif len(part1) == 4 and len(part2) == 3:
                    whiteSpace1 *= 2
                    whiteSpace2 *= 2
                        
                # print(f'{whiteSpace1}{part1}')
                # print(f'{minusSign}{whiteSpace2}{part2}')
                # print(f'{problemWidth}')
            line1 += f'{whiteSpace1}{part1}    '
            line2 += f'{minusSign}{whiteSpace2}{part2}    '
            line3 += f'{problemWidth}    '
    
          


            if show_answers:
                if sum < 0:
                    if sumSize == 1:
                        whiteSpace3 *= 1
                    elif sumSize == 2:
                        whiteSpace3 *= 1
                    elif sumSize == 3:
                        whiteSpace3 *= 1
                    elif sumSize == 4:
                        whiteSpace3 *= 1
                    line4 += f'{whiteSpace3}{sum}    '
                if sum > 0:
                    if sumSize == 1:
                        whiteSpace3 *= 2
                    elif sumSize == 2:
                        whiteSpace3 *= 2
                    elif sumSize == 3:
                        whiteSpace3 *= 2
                    elif sumSize == 4:
                        whiteSpace3 *= 2
                    line4 += f'{whiteSpace3}{sum}    '
                    
    print(line1.rstrip())
    print(line2.rstrip())
    print(line3.rstrip())
    if show_answers:
        print(line4.rstrip())
                
                
            
            

            
                
                
                
            

                

            
    
    # return problems
                    
#tests
#arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
#arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
#arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])     
#arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])    
#arithmetic_arranger(["3 + 855", "988 + 40"], True)  
#arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)                