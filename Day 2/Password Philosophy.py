with open("input.txt", "r") as f:
	passwords = f.readlines()


def checkPassword(line):
		splitted = line.split()

		policyRange = splitted[0].split("-") 
		minRange = int(policyRange[0])
		maxRange = int(policyRange[1])
		
		policyLetter = splitted[1].replace(":","")
		password = splitted[2]

		if password.count(policyLetter) in range(minRange, maxRange+1):
			return True
		else:
			return False

correctPasswords = 0
for lines in passwords:
	if checkPassword(lines):
		correctPasswords += 1
print(correctPasswords)