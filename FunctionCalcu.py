import math

def banner(message, border = '-'):
	line = border * len(message)
	print(line)
	print(message)
	print(line)

def suma(num1, num2):
	result =  num1 + num2
	print(f"\nThe result of operation Sum is: {result}")

def resta(num1, num2):
	result = num1 - num2
	print(f"\nThe result of operation Substraction is: {result}")

def multiplication(num1, num2):
	result = num1 * num2
	print(f"\nThe result of operation Multiplication is: {result}")

def division(num1, num2):

	try:
		result = num1 / num2
		print(f"\nThe result of operation Division is: {result}")

	except ZeroDivisionError:
		print("\nCANNOT DIVIDE BY ZERO")
		return "Error Operation"
