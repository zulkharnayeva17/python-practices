#1 task
a=input('Your last name, first name\n ')
b= input ('How old are you?\n')
c=input('Your phone number?\n')
print ('Your name', a)
print ('Your age', b)
print('Your phone number', c)

 #4
import math
A=int(input('enter the number'))
Y= (A**2/3 )+ ((A**2 + 4)/6 )+ (math.sqrt(A**2 + 4))/(4) + math.sqrt(math.pow((A**2+ 4),3))/4
print(Y)
#5
import math
x= int(input(   'guess the number'))
y=((x/5) + 8)/2
print(y)


#tasks for variables, cycles
#2.1
import math

def calculate(a, b, operation):
   result = None 

   if operation == '+':
       result = sum(a, b)
   elif operation == '-':
       result = subtract(a, b)
   elif operation == '/':
       result = divide(a, b)
   elif operation == '*':
       result = multiply(a, b)
   else:
       print('unknown operation')  
    
   return result
# 2.2
