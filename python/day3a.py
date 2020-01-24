import re

with open ('./day3_input.txt') as f:
	inputData = f.read ()

claims = inputData.splitlines ()

fabric = {}

re_claim = re.compile (r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

overlaps = 0

for claim in claims:
	match = re_claim.match (claim)
	if match:
		claimId, startX, startY, sizeX, sizeY = match.groups ()

		startX = int (startX)
		startY = int (startY)
		sizeX = int (sizeX)
		sizeY = int (sizeY)

		for y in range (startY, startY + sizeY):
			for x in range (startX, startX + sizeX):
				if (y in fabric):
					if (x in fabric [y]):
						fabric [y] [x] += 1
						if (fabric [y][x] == 2):
							overlaps += 1
					else:
						fabric [y] [x] = 1
				else:
					fabric [y] = {}
					fabric [y] [x] = 1

print (overlaps) #	112418