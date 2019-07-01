import math

print("\nStarting calculator...")

print("\n-------------Operations Math---------------")

print("\n-Sum ------------------> S")
print("-Substraction ---------> R")
print("-Multiplication -------> M")
print("-Division -------------> D")

operation = input("\nType key of the Operation: ").lower()


if operation != "s" and operation != "r" and operation != "m" and operation != "d":
	print("\nERROR the Key.")
else:
	numOne = float(input("Type a number: "))
	numTwo = float(input("Type other number: "))

	if operation == "s":
		resultado = numOne + numTwo
		print(f"the result of operation Sum is: {resultado}")

	elif operation == "r":
		resultado = numOne - numTwo
		print(f"the result of operation Substraction is: {resultado}")

	elif operation == "m":
		resultado = numOne * numTwo
		print(f"the result of operation Multiplication is: {resultado}")

	elif operation == "d":
		if numOne == 0 and numTwo == 0:
			print("\nResult is undefined")
		elif numOne == 0 and numTwo != 0 or numOne != 0 and numTwo == 0:
			print("\nCANNOT DIVIDE BY ZERO")
		else:
			resultado = numOne / numTwo
			print(f"the result of operation Division is: {resultado}")

print("\nFinishid Operation...")