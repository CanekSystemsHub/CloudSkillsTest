# This code is for a simple calculator of to values + - x /

# First value
val1 = int(input('Input the first value '))
val2 = int(input('Input the second value  '))
operation = str(input('Input the operation type, you can only type +, -, x or /  '))

print(val1) 
print(operation)
print(val1)

if operation == '+':
  print('You selected a Sum  so the result is: ' + str(val1) + str(operation) + str(val2) + " = " + str(val1 + val2))
elif operation == '-':
  print('You selected a Sub  so the result is: ' + str(val1) + str(operation) + str(val2) + " = " + str(val1 - val2))
elif operation == 'x':
 print('You selected a Mul  so the result is: ' + str(val1) + str(operation) + str(val2) + " = " + str(val1 * val2))
elif operation == '/':
  print('You selected a Div so the result is: ' + str(val1) + str(operation) + str(val2) + " = " + str(val1 / val2))
else:
    print('You did not selecte a valid operation ... Bye!')

# print(str(val1) + str(operation + str(val2) + " = " ))
