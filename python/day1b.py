with open ('./day1_input.txt') as f:
	inputData = f.read ()

frequencies = inputData.splitlines ()

prevFrequencies = {0: True}

delta = 0

hitPrevious = False

while hitPrevious == False:
	for frequency in frequencies:
		delta += int (frequency)
		if (delta in prevFrequencies):
			hitPrevious = delta
			break
		prevFrequencies [delta] = True

print (hitPrevious)		# 413