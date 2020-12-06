with open("input.txt", "r") as f:
	passportsInput = f.readlines()
	passportsInput = list(map(lambda s: s.strip(), passportsInput)) # Removes the \n at the end of every line


splitIndexes = []
# Removes the empty line between each group and saves the index
for lines in passportsInput:
	if lines == '':
		indexOfSplit = passportsInput.index(lines)
		splitIndexes.append(indexOfSplit)
		passportsInput.pop(indexOfSplit)
# Divides the groups into lists inside the list, each group marked by the saved indexes
splittedPassports = [passportsInput[i : j] for i, j in zip([0] + 
          splitIndexes, splitIndexes + [None])] 

validPassports = 0
for lines in splittedPassports:

	for item in lines:

		if ' ' in item:

			#lines.remove(item)
			#item = item.split()
			#lines.extend(item)

			itemIndx = lines.index(item)
			item = item.split()
			lines = lines[:itemIndx] + item + lines [itemIndx + 1:]
	
	for item in lines:
		itemIndx = lines.index(item)
		item = item.split(':')
		lines = lines[:itemIndx] + item + lines [itemIndx + 1:]

	
	passportDict = {}
	for i in range(0, len(lines), 2):
		passportDict.update({lines[i]:lines[i+1]})


	flag = False
	if len(passportDict) == 8:
		flag = True
	elif len(passportDict) == 7 and 'cid' not in passportDict:
		flag = True


	if flag:
		if not (1920 <= int(passportDict['byr']) <= 2002):
			flag = False
		if not (2010 <= int(passportDict['iyr']) <= 2020):
			flag = False
		if not (2020 <= int(passportDict['eyr']) <= 2030):
			flag = False
		# This conditional is taken from the solution megathread because i couldn't make it work and i've already looked that answer so my logic was "corrupt" anyways
		if not (((passportDict['hgt'][-2:] == 'cm') and (150 <= int(passportDict['hgt'][:-2]) <= 193)) or ((passportDict['hgt'][-2:] == 'in') and (59 <= int(passportDict['hgt'][:-2]) <= 76))):
			flag = False
		if not (passportDict['hcl'][0] == '#' and int(passportDict['hcl'][1:],16) > 0):
			flag = False
		if passportDict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			flag = False
		if not (passportDict['pid'].isdigit() and len(passportDict['pid']) == 9):
			flag = False

	if flag:
		validPassports += 1

	

print(validPassports)


'''
This is one of the attemps i did after day 4, if you want to look...
#splittedPassports = [['byr:1935 eyr:2025 iyr:2018 hgt:65in pid:396444938 cid:293', 'ecl:grn', 'hcl:#efcc98'], ['byr:1926 pid:954310029 cid:64', 'hcl:#fffffd', 'ecl:grn', 'iyr:2012', 'hgt:150cm', 'eyr:2024']]
valid = 0
for passport in splittedPassports:
	#print(passport)
	for line in passport:
		#print(line)
		if ' ' in line:
			passport.remove(line)
			line = line.split()
			passport.extend(line)

		#print(line)
	print(passport)

	if len(passport) == 8:
		valid += 1
	elif len(passport) ==  and 'cid' not in passport:
		valid += 1
print(valid)
'''