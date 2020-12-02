with open("input.txt", "r") as f:
	passwords = f.readlines()


def oldCheckPassword(line):

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

def newCheckPassword(line):

	splitted = line.split()

	toCheckValues = splitted[0].split("-") 
	value1 = int(toCheckValues[0])-1
	value2 = int(toCheckValues[1])-1
		
	policyLetter = splitted[1].replace(":","")
	password = splitted[2]

	if bool(password[value1] == policyLetter) != bool(password[value2] == policyLetter):
		return True
	else:
		return False




correctPasswords = 0

for lines in passwords:
	if newCheckPassword(lines):
		correctPasswords += 1
print(correctPasswords)