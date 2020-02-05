import re

with open ('./day6_input.txt') as f:
	inputData = f.read ()

coords = inputData.splitlines ()

coords = [
	'1, 1',
	'1, 6',
	'8, 3',
	'3, 4',
	'5, 5',
	'8, 9',
]

map = {}

re_coord = re.compile (r"\(\d+)\,(\d+)")

for coord in coords:

	match = re_coord.match (coord)

	if (match):
		x, y = match.groups ()
