import time
def hammingDistance(wordA, wordB):
	count=0
	dist=0
	while (count < len(wordA)):
		if (wordA[count]!=wordB[count]):
			dist+=1
		count+=1
	return dist
	
def smartDictator(dict):
	smartDict={}
	for word in dict:
		if len(word) not in smartDict:
			smartDict[len(word)]=[]
		smartDict[len(word)].append(word)
	return smartDict

def aStar(wordA, wordB, smartDict):
	queCost=[]
	queCost.append([['',wordA], 0])
	found=False
	seenList=[]
	while (len(queCost)!=0):
		currentPath, currentCost= queCost.pop(0)
		queCost=[]
		if currentPath[-1] == wordB:
			found=True
			return currentPath
		if currentPath[-1] in seenList:
			continue
		else:
			seenList.append(currentPath[-1])
			nextWords=[]
			for word in smartDict[len(wordA)]:
				if word not in seenList and hammingDistance(word, currentPath[-1])==1:
					nextWords.append(word)
			for word in nextWords:
				newPath=[]
				newPath=list(currentPath)
				newPath.append(word)
				newCost=hammingDistance(word, wordB)
				newCost=newCost+ currentCost
				queCost.append([newPath, newCost])
		queCost=sorted(queCost,key=lambda x: x[1])
	tempS=[wordB, 0]
	return tempS