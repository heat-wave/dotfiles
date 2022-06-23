#!/usr/bin/python
import sys

def stampDuty(price):
	if price < 500000:
		return (price - 300000) * 0.05
	else:
		return 125000 * 0.02 + (price - 250000) * 0.05

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Arguments: salary, property price, safety net")
		sys.exit(1)
	salary = int(sys.argv[1])
	propertyPrice = int(sys.argv[2])
	safetyNet = int(sys.argv[3])
	mortgage = 4.75 * salary
	cashRequired = (propertyPrice + stampDuty(propertyPrice) + safetyNet) - mortgage
	print("Cash required: " + str(cashRequired))
