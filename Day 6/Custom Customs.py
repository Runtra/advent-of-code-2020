with open("input.txt", "r") as f:
	answersInput = f.readlines()
	answersInput = list(map(lambda s : s.strip(), answersInput)) # Removes the \n at the end of every line


splitIndexes = []
# Removes the empty line between each group and saves the index
for lines in answersInput:
	if lines == '':
		indexOfSplit = answersInput.index(lines)
		splitIndexes.append(indexOfSplit)
		answersInput.pop(indexOfSplit)

# Divides the groups into lists inside the list, each group marked by the saved indexes
splittedAnswers = [answersInput[i : j] for i, j in zip([0] + 
          splitIndexes, splitIndexes + [None])] 



#####################
# Part 1 (original) #
#####################
def union_byHand():
	groupConfirmed = []
	for group in splittedAnswers:

		confirmed = []
		for answer in group:
			for char in answer:
				if char not in confirmed:
					confirmed.append(char)
		groupConfirmed.append(len(confirmed))
	return groupConfirmed



#####################
#  Part 1 (better)	#
#####################
def union():
	groupConfirmed = []
	for group in splittedAnswers:
		answers = []
		for answer in group:
			answers.append(set(answer))
		commonChars = set.union(*answers)
		groupConfirmed.append(len(commonChars))
	return groupConfirmed


#####################
#  		Part 2		#
#####################
def intersection():
	groupConfirmed = []
	for group in splittedAnswers:
		answers = []
		for answer in group:
			answers.append(set(answer))
		commonChars = set.intersection(*answers)
		groupConfirmed.append(len(commonChars))
	return groupConfirmed

unionConfirmed = union()
unionConfirmed_byHand = union_byHand()
intersectionConfirmed = intersection()

print(sum(unionConfirmed))
#print(sum(unionConfirmed_byHand))
print(sum(intersectionConfirmed))

# Correct part one: 6680
# Correct part two: 3117