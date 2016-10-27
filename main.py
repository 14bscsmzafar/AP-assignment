from wordLadder import *
from stats import *
from multiprocessing import Pool
import json

def jsonParser(path):
	with open(path, 'r', encoding='utf-8') as json_data:
		#json_data=decode(json_data)
		d=json.load(json_data)
		print("Load complete!")
		return d.keys()
if __name__=='__main__':
	print("Loading dictionary from file!")
	dict=jsonParser('dictionary.json')
	smartDict=smartDictator(dict)
	print("Indexing complete!")
	#for key in smartDict[4]:
	#	print(key)

	inp=input("Enter the size to solve: ")
	#len=input("Please enter the word length to calculate stats: ")
	#del d[:] #we dont need this, free up some memory
	statList=[]
	count=0
	scount=0
	save=shelve.open('three')
	pool = Pool()
	for source in smartDict[inp]:
		count=0
		while(count < (len(smartDict[inp])-1)):
		#for dest in smartDict[inp]:
			if (source==smartDict[inp][count]):
				break
			temp=[]
			result1 = pool.apply_async(aStar, [source, smartDict[inp][count], smartDict])    # evaluate "solve1(A)" asynchronously
			temp.append(smartDict[inp][count])
			count+=1
			result2 = pool.apply_async(aStar, [source, smartDict[inp][count], smartDict])    # evaluate "solve1(A)" asynchronously
			temp.append(smartDict[inp][count])
			
			answer1 = result1.get(timeout=10)
			if (answer1[-1]=="0"):
				statList.append(source, -1, temp[0])

			else:
				statList.append([source, len(answer1)-2, temp[0]])
			
			#statList.append(source, len(answer1)-2, answer1[-1]])

			answer2 = result2.get(timeout=10)
			if (answer2[-1]=="0"):
				statList.append([source, -1, temp[1]])
			else:
				statList.append([source, len(answer2)-2, temp[1]])
			print(count)

			# if len(ans) > 0:
				# for word in ans:
					# print("->" + word)
				# print()
			count+=1

	# l=[]

	freqDist(statList)
	save.close()
	
# w1=input("1st: ")
# w2=input("2nd: ")
# l.append(w1)
# ans=solve(w1, w2, l, smartDict)
# print(ans[2])