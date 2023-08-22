# calculator.py
# MAHEEN RAZA, ENDG 233 F21 UCID: 30137445
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#

num_one = int(input('Enter the first value: '))            ## this code asks the user for input for three integers and two operations
oper_one = str(input('Enter the first operator: '))
num_two = int(input('Enter the second value: '))
oper_two = str(input('Enter the second operator: '))
num_three = int(input('Enter a third value: '))
print('Entered expresion:', num_one, oper_one, num_two, oper_two, num_three)     ## this will display the final expression the suer wants to calculate


adding = '+'               ## this assigns a variable to the string that the user will enter depending on what operation that want the calculator to perform
subtracting = '-'
multiplying = '*'
dividing = '/'
        
if oper_one == adding and oper_two == adding:          ## the if and elif statements will decipher how to calculate the expression depending on what operations are entered, following BEDMAS
    answer = num_one + num_two + num_three
    
elif oper_one == adding and oper_two == subtracting:
    answer = num_one + num_two - num_three
    
elif oper_one == adding and oper_two == multiplying:
    answer = num_one + (num_two * num_three)
    
elif oper_one == adding and oper_two == dividing:
    answer = num_one + (num_two // num_three)
    
elif oper_one == subtracting and oper_two == adding:
    answer = num_one - num_two + num_three
    
elif oper_one == subtracting and oper_two == subtracting:
    answer = num_one - num_two - num_three
    
elif oper_one == subtracting and oper_two == multiplying:
    answer = num_one - (num_two * num_three)
    
elif oper_one == subtracting and oper_two == dividing:
    answer = num_one - (num_two // num_three)
    
elif oper_one == multiplying and oper_two == adding:
    answer = (num_one * num_two) + num_three
    
elif oper_one == multiplying and oper_two == subtracting:
    answer = (num_one * num_two) - num_three
    
elif oper_one == multiplying and oper_two == multiplying:
    answer = num_one * num_two * num_three
    
elif oper_one == multiplying and oper_two == dividing:
    answer = num_one * num_two // num_three
    
elif oper_one == dividing and oper_two == adding:
    answer = (num_one // num_two) + num_three

elif oper_one == dividing and oper_two == subtracting:
    answer = (num_one // num_two) - num_three

elif oper_one == dividing and oper_two == multiplying:
    answer = num_one // num_two * num_three

elif oper_one == dividing and oper_two == dividing:
    answer = num_one // num_two // num_three
else:                                             ## if anything else in inputed, it will display error
    print('Error!')

print('Your final answer =', answer)      ## this will output the final answer as an integer since floor division is used