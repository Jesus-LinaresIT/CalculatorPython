import math
from FunctionCalcu import suma, resta, multiplication, division, banner


print("\nStarting calculator...\n")

banner('Operations Math')

print("\n-Sum ------------------> S")
print("-Substraction ---------> R")
print("-Multiplication -------> M")
print("-Division -------------> D")

operation = input("\nType key of the Operation: ").lower()


if operation != "s" and operation != "r" and operation != "m" and operation != "d":
	print("\nERROR the Key.")	
else:
	numOne = float(input("\nType a number: "))
	numTwo = float(input("Type other number: "))

	if operation == "s":
	 	suma(numOne, numTwo)

	elif operation == "r":
		resta(numOne, numTwo)
		
	elif operation == "m":
		multiplication(numOne, numTwo)
		
	elif operation == "d":		
		if numOne == 0 and numTwo == 0:
			print("\nResult is undefined")

		elif numOne == 0 and numTwo != 0 or numOne != 0 and numTwo == 0:
			print("\nCANNOT DIVIDE BY ZERO")
		else:
			division(numOne, numTwo)
			


print("\nFinishid Operation...")