"""
In this section we will see about salary incentive , how the system work for that.
___________________________________________________________________________________
Question : In giving salary you have to increment the bonus of employees
__________________________________________________________________________
Approach : first we take input from user in the form of salary then we calculate 10percent
           of salary we add calculated salary to the main salary and then print the final result
"""
a = int(input("enter amount of salary : "))
b = a * 10 / 100
print( "final amount of salary is :", a + b)
# Made by khushi