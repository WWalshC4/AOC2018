from string import ascii_lowercase

with open ('./day5_input.txt') as f:
	inputData = f.read ()

polymersToReact = inputData

# polymersToReact = 'aA' # 0
# polymersToReact = 'abBA' # 0
# polymersToReact = 'abAB'
# polymersToReact = 'aabAAB'
# polymersToReact = 'dabAcCaCBAcCcaDA' # 10, dabCBAcaDA

bestReactionCount = 100000000000
bestReactionLetter = ''

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

for c in ascii_lowercase:
	missingPolymer = polymersToReact
	missingPolymer = missingPolymer.replace (c, '')
	missingPolymer = missingPolymer.replace (c.upper (), '')

	reactedPolymers = reactPolymers (missingPolymer)

	if (len (reactedPolymers) < bestReactionCount):
		bestReactionLetter = c
		bestReactionCount = len (reactedPolymers)

print (bestReactionCount, bestReactionLetter) #4572, m