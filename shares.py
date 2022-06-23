#!/usr/bin/python
import sys

global sharePrice
realisedGain = 45000
sharesSold = 137
extraShares = 30
exercisedOptions = 500
totalBy2023 = 1068
optionsWithGrowth = 32
cgt = 0.2
eit = 0.5459

def growthSharesValue():
	if sharePrice <= 551:
		return sharePrice * optionsWithGrowth * (1 - eit)
	else:
		return 551 * optionsWithGrowth * (1 - eit) + (sharePrice - 551) * optionsWithGrowth * (1 - cgt)

def unexercisedOptionsValue():
	return sharePrice * (totalBy2023 - exercisedOptions) * (1 - eit)

def sharesValue():
	return sharePrice * (exercisedOptions + extraShares - sharesSold) * (1 - cgt)

def totalValue():
	return realisedGain + growthSharesValue() + unexercisedOptionsValue() + sharesValue()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		sharePrice = int(sys.argv[1])
	else:
		sharePrice = 440
	print(totalValue())
