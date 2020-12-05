with open("input.txt", "r") as f:
	passports = f.readlines()
	passports = list(map(lambda s: s.strip(), passports)) # Removes the \n at the end of every sentence


splitIndexes = []


for lines in passports:
	if lines == '':
		indexOfSplit = passports.index(lines)
		splitIndexes.append(indexOfSplit)
		passports.pop(indexOfSplit)

splittedPassports = [passports[i : j] for i, j in zip([0] + 
          splitIndexes, splitIndexes + [None])] 
#print(splittedPassports)

validPassports = 0
isValid = False
possibleHairColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for lines in splittedPassports:

	for item in lines:
		if item.find(' ') != -1:
			itemIndx = lines.index(item)
			
			item = item.split()

			lines = lines[:itemIndx] + item + lines [itemIndx + 1:]
	
	for item in lines:
		itemIndx = lines.index(item)
		item = item.split(':')
		lines = lines[:itemIndx] + item + lines [itemIndx + 1:]
	#print(lines)
	
	passportDict = {}
	# De aca para abajo chequeamos la validez del pasaporte
	for i in range(0, len(lines), 2):
		passportDict.update({lines[i]:lines[i+1]})
	print(passportDict)

	checkParametersValidity = False

	if len(passportDict) == 8:
		checkParametersValidity = True
	elif len(passportDict) == 7:
		cidFound = False
		for item in lines:
			if 'cid' in item:
				cidFound = True
				break
		if not cidFound:
			checkParametersValidity = True

	if checkParametersValidity: # Ya se que esta no es la manera correcta de hacerlo pero no me rompas la pija son las 6 de la mañana y hace tanto tiempo que no duermo
		isValid = True
		if 1920 <= int(passportDict['byr']) <= 2002:
			print(passportDict['byr'])
		else:
			isValid = False
			print('byr: False -> ' + passportDict['byr'])
		if 2010 <= int(passportDict['iyr']) <= 2020:
			print(passportDict['iyr'])
		else:
			isValid = False
			print('iyr: False -> ' + passportDict['iyr'])
		if 2020 <= int(passportDict['eyr']) <= 2030:
			print(passportDict['eyr'])
		else:
			isValid = False
			print('eyr: False -> ' + passportDict['eyr'])
		if passportDict['hcl'] in possibleHairColors:
			print(passportDict['hcl'])
		else:
			isValid = False
			print('hcl: False -> ' + passportDict['hcl'])
		if passportDict['pid'].isdigit() and len(passportDict['pid']) == 9:
			print(passportDict['pid'])
		else:
			isValid = False
			print('pid: False')
		# encima no anfa esto la concha de la lora


	if isValid:
		validPassports += 1
		
	
print(validPassports)
				
# por favor no me pidas que entienda este codigo en media hora porque no tengo ni la mas puta idea