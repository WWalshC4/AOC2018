with open ('./day2_input.txt') as f:
	inputData = f.read ()

boxIds = inputData.splitlines ()

twos = 0
threes = 0

for id1 in range (len (boxIds)):
	for id2 in range (id1 + 1, len (boxIds)):
		l1 = list (boxIds [id1])
		l2 = list (boxIds [id2])

		diff = 0
		id = list (boxIds [id1])

		for i in range (len (l1)):
			if (l1 [i] != l2 [i]):
				diff += 1
				id [i] = ''

		if (diff == 1):
			print (''.join (id))		# bvnfawcnyoeyudzrpgslimtkj