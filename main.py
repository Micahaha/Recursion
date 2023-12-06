from loops import *
from recursion import *


print("Factorial of 6 using a loop is", loops.factorial(6))
print("Factorial of 5 using a loop is", loops.factorial(5))
print("Factorial of 1 using a loop is", loops.factorial(1))

print('')

print("Factorial of 6 using a loop is", recursion.factorial(6))
print("Factorial of 1 using a loop is", recursion.factorial(5))
print("Factorial of 1 using a loop is", recursion.factorial(1))

print("2 to the 5th power using a loop is:", loops.power(2, 5))
print("2 to the 4th power using a loop is:", loops.power(2, 4))
print("2 to the 0 power using a loop is:", loops.power(2, 0))

print("2 to the 5th power using a loop is:", recursion.power(2, 5))
print("2 to the 4th power using a loop is:", recursion.power(2, 4))
print("2 to the 0 power using a loop is:", recursion.power(2, 0))

list = [4,2,2,56,7]
i = 0 
print(f"Min value:{recursion.computeMin(list, 0, list[i])}")

list = [4,2,2,56,7]
i = 0 
print(f"Min value: {recursion.computeMin(list, 0, list[0])}")

str = 'Hello Dog'
print(f'Reverse String: {recursion.reverse(str, len(str))}')

