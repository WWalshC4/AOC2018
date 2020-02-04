with open ('./day5_input.txt') as f:
	inputData = f.read ()

polymersToReact = inputData

# polymersToReact = 'aA' # 0
# polymersToReact = 'abBA' # 0
# polymersToReact = 'abAB'
# polymersToReact = 'aabAAB'
# polymersToReact = 'dabAcCaCBAcCcaDA' # 10, dabCBAcaDA


def reactPolymers (polymers):
	index = 0

	while index < len (polymers) - 1:
		thisElement = polymers [index]
		nextElement = polymers [index + 1]

		if (thisElement != nextElement and thisElement.upper() == nextElement.upper()):
			polymers = polymers.replace (thisElement + nextElement, '')
			index = index - 1
		else:
			index = index + 1

	return polymers

reactedPolymers = reactPolymers (polymersToReact)

print (len (reactedPolymers)) # 10132