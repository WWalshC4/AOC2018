import re

with open ('./day3_input.txt') as f:
	inputData = f.read ()

claims = inputData.splitlines ()

fabric = {}

re_claim = re.compile (r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

all_claims = set ()
overlap_claims = set ()

for claim in claims:
	match = re_claim.match (claim)
	if match:
		claimId, startX, startY, sizeX, sizeY = match.groups ()

		startX = int (startX)
		startY = int (startY)
		sizeX = int (sizeX)
		sizeY = int (sizeY)

		all_claims.add (claimId)

		for y in range (startY, startY + sizeY):
			for x in range (startX, startX + sizeX):
				if (y in fabric):
					if (x in fabric [y]):
						overlap_claims.add (claimId)
						overlap_claims.add (fabric [y][x])
					else:
						fabric [y] [x] = claimId

				else:
					fabric [y] = {}
					fabric [y] [x] = claimId

print (all_claims - overlap_claims) # 560