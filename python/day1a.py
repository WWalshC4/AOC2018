with open ('./day1_input.txt') as f:
	inputData = f.read ()

frequencies = inputData.splitlines ()

delta = 0

for frequency in frequencies:
	delta += int (frequency)

print (delta)		# 493