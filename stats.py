def freqDist(data, name):
	dist={}
	noChain=[]
	maxChainRow=['', 0, '']
	
	for row in data:
		print(row[1])
		if row[0]==row[2]:
			continue
		if row[1]==-1:
			noChain.append(row)
		else:
			if row[1] not in dist.keys():
				dist[row[1]]=1
			else:
				dist[row[1]]+=1
			
			if row[1] > maxChainRow[1]:
				maxChainRow=row
	
	f=open(name+".txt", 'w')
	f.write("Stats for " + name+ "\n\n")
	print("Stats for " + name+ "\n")
	f.write("Words with no chain:\n")
	print("Words with no chain:")
	for row in noChain:
		f.write(row[0] + "-->" + row[2] + "\n")
		print(row[0] + "-->" + row[2])
	
	f.write("Word with longest chain:\n")
	print("Word with longest chain:")

	f.write(row[0])
	print(row[0])

	for row in maxChainRow[2]:
		f.write("-->" + row)
		print("-->" + row)

	
	f.write("\n\n")
	print("\n")
	
	
	distKey=list(dist)
	distKey.sort()
	f.write("\t\tFrequency Distribution\n")
	print("\t\tFrequency Distribution\n")
	f.write("Frequency\t\tValue\n")
	print("Frequency\t\tValue")
	for key in distKey:
		f.write(str(key) + "\t\t" + str(dist[key]) + '\n')
		print(str(key) + "\t\t" + str(dist[key]) + '\n')
	
	f.close()

	