with open("input.txt", "r") as f:
	reportValues = f.readlines()
	reportValues = list(map(int, reportValues))

# If 2020 minus a number of the input equals to other number of the input, it means that the both add up 2020
for x in reportValues:
	y = 2020 - x
	if y in reportValues:
		print(x*y)
		break