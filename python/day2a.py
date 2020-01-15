with open ('./day2_input.txt') as f:
	inputData = f.read ()

boxIds = inputData.splitlines ()

twos = 0
threes = 0

for boxId in boxIds:
	l = list (boxId)
	s = {}

	two = False
	three = False

	for i in l:
		if (i in s):
			s [i] += 1
		else:
			s [i] = 1

	for i in s:
		if (s [i] == 2):
			two = True
		if (s [i] == 3):
			three = True

	if (two):
		twos += 1
	if (three):
		threes += 1

print (twos * threes)		# 6696
