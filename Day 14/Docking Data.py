with open('input.txt', 'r') as f:
	data = f.readlines()
	data = list(map(lambda s : s.strip(), data)) # Removes the \n at the end
	data = list(map(lambda s : s.replace(' ',''), data)) # Removes the spaces in between

# Function from https://stackoverflow.com/a/12174051 to replace an specific bit of a value
def setBit(v, index, x):
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v |= mask         # If x was True, set the bit indicated by the mask.
  return v            # Return the result, we're done.

dataDict = {}
a = 0
for line in data:
	
	line = line.split('=')

	if line[0] == 'mask':
		mask = line[1]
		continue

	line[0] = int(line[0].translate({ord(c): None for c in '[]mem'})) # Removes the characters of the string from line
	dataDict.update({line[0]:int(line[1])})


	index = len(mask)-1
	for char in mask:
		if char == '1':
			dataDict[line[0]] = setBit(dataDict[line[0]], index, True)

		elif char == '0':
			dataDict[line[0]] = setBit(dataDict[line[0]], index, False)

		index -= 1


print(sum(dataDict.values()))

#
#	Part 1: 13556564111697
#
#