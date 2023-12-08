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

list_1 = [4,2,2,56,7]
i = 0 
print(f"Min value:{recursion.computeMin(list_1, 0, list_1[i])}")

list_1 = [4,2,2,56,7]
i = 0 
print(f"Min value: {recursion.computeMin(list_1, 0, list_1[0])}")

str = 'Hello Dog'
print(f'Reverse String: {recursion.reverse(str, len(str))}')



print('Enter 7 numbers seperated by a space: ')
list_of_numbers = list(map(int, input("Enter two numbers separated by space: ").split()))
index = int(input('Enter the index at which the search will begin: '))
size = int(input('Enter the size of the list that will be searched: '))
target = int(input('Enter the target value to search for: '))
i = 0

print(f'Target found at: {recursion.search(list_of_numbers, index, size, target, i, False)}')