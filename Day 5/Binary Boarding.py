with open("input.txt", "r") as f:
	seatsList = f.readlines()
	seatsList = list(map(lambda s: s.strip(), seatsList))
	#print(seats)

maxID = 0
IDs = []
for seat in seatsList:


	row = [0, 127]
	column = [0, 7]
	#print(seat)
	#print(row)

	for char in seat:
		
		if char == 'B':
			row[0] = (row[1]+row[0])//2+1

		if char == 'F':
			row[1] = (row[1]+row[0])//2

		if char == 'R':
			column[0] = (column[1]+column[0])//2+1
		if char == 'L':
			column[1] = (column[1]+column[0])//2

	seatID = row[0] * 8 + column[0]
	IDs.append(seatID)
	if seatID > maxID:
		maxID = seatID
	#print(seatID)


IDs.sort()


mySeat = -1
for i in range(len(IDs)):
	if IDs[i+1]-IDs[i] == 2:
		mySeat = IDs[i]+1
		break

print('My seat  ID: ' + str(mySeat))
print('Max seat ID: ' + str(maxID))