with open("input.txt", "r") as f:
	reportValues = f.readlines()
	reportValues = list(map(int, reportValues))

def twoNumbers(values):
	# If 2020 minus a number of the input equals to other number of the input, it means that the both add up 2020
	for x in values:
		y = 2020 - x
		if y in values:
			return x * y

def threeNumbers(values):
	for x in values:
		for y in values:
			z = 2020 - y - x
			if z in values:
				return x * y * z

#print(twoNumbers(reportValues))
#print(threeNumbers(reportValues))