import math
from FunctionCalcu import suma, resta, multiplication, division, banner


print("\nStarting calculator...\n")

banner('Operations Math')

print("\n-Sum ------------------> S")
print("-Substraction ---------> R")
print("-Multiplication -------> M")
print("-Division -------------> D")

ope = input("\nType key of the Operation: ").lower()


if ope != "s" and ope != "r" and ope != "m" and ope != "d":
	print("\nERROR the Key.")

else:	

	while True:

		try:
			numOne = float(input("\nType a number: "))
			numTwo = float(input("Type other number: "))
			break

		except ValueError:
			print("\nThe values entered are not correct. Try again")

	if ope == "s":
	 	suma(numOne, numTwo)

	elif ope == "r":
		resta(numOne, numTwo)
		
	elif ope == "m":
		multiplication(numOne, numTwo)
		
	elif ope == "d":		
		if numOne == 0 and numTwo == 0:
			print("\nResult is undefined")			
		else:
			division(numOne, numTwo)
			

print("\nFinishid Operation...")

print("\ncontinuation of program execution...")
