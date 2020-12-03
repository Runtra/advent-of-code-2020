with open("input.txt", "r") as f:
	terrain = f.readlines()


def countTrees(terrainList, stepRight, stepDown = 1):
	trees = 0
	pos = 0

	for line in terrainList[::stepDown]:
		if line[pos] == '#':
			trees += 1
			line = line[:pos] + 'X' +line[pos + 1:]
		else:
			line = line[:pos] + 'O' +line[pos + 1:]

		#print(line)
		pos += stepRight

		if pos > 30:
			pos -= 31
	return trees

R1D1 = countTrees(terrain, 1)
R3D1 = countTrees(terrain, 3)
R5D1 = countTrees(terrain, 5)
R7D1 = countTrees(terrain, 7)
R1D2 = countTrees(terrain, 1, 2)

print(R1D1)
print(R3D1)
print(R5D1)
print(R7D1)
print(R1D2)

print(R1D1 * R3D1 * R5D1 * R7D1 * R1D2)
