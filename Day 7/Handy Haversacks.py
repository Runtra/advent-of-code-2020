with open('input.txt', 'r') as f:
	bagsRules = f.readlines()
	bagsRules = list(map(lambda s : s.strip('\n.'), bagsRules))

bagsDict = dict()
for line in bagsRules:

	line = line.replace('bags', '')
	line = line.replace('bags', '')
	line = ''.join([i for i in line if not i.isdigit()]) 
	line = line.split('contain')

	for item in line:
		indexItem = line.index(item)
		item = item.split(',')
		
		#print(item)
		for itemcito in item:
			indexItemcito = item.index(itemcito)
			itemcito = itemcito.strip()
			item[indexItemcito] = itemcito
		#print(item)
		line[indexItem] = item
	line[0] = line[0][0]
	
	bagsDict.update({line[0]:line[1]})

print(bagsDict)

#dictKeys = bagsDict.keys() 
shinyGoldCount = 0
for keys in bagsDict:
	if 'shiny gold' in bagsDict[keys]:
		#print(bagsDict[keys])
		shinyGoldCount += 1
print(len(bagsDict))
print(shinyGoldCount)