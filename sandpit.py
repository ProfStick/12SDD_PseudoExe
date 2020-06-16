""" A sandpit to test code snippets.
"""

# test of logic for sarter.pse

currentNumber = 0

print(currentNumber)

lastNumber = currentNumber
currentNumber = lastNumber + 1

print(currentNumber)

for counter in range(1, 20, 1):
    tempNumber = currentNumber
    currentNumber = currentNumber + lastNumber
    lastNumber = tempNumber
    print(currentNumber)

