with open ('./day5_input.txt') as f:
	inputData = f.read ()

polymers = inputData

# polymers = 'dabAcCaCBAcCcaDA' # 10, dabCBAcaDA

# polymers = 'abBA' # 0

remainingPolymers = []

polymers = polymers
index = 0

madeRemoval = True

while (madeRemoval):
	madeRemoval = False
	index = 0

	while index < len (polymers) - 1:
		thisElement = polymers [index]
		nextElement = polymers [index + 1]

		if (thisElement != nextElement and thisElement.upper() == nextElement.upper()):
			index = index + 2
			madeRemoval = True
		else:
			remainingPolymers.append (thisElement)
			index = index + 1

			if (index == len (polymers) - 1):
				remainingPolymers.append (nextElement)

	polymers = ''.join (remainingPolymers)
	remainingPolymers = []

print (len (polymers)) #10132