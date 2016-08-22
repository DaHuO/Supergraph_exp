import collections
import math
# debug=False
# with open('B-small-attempt1.in') as f:
# debug=True
with open('B-large.in') as f:
	content = f.readlines()

def GetMaxPositiveIndex(N):
	maxCounter,counter,index=0,0,0
	for x in range(len(N)):
		if(N[x]=='+'):
			counter+=1
		else:
			counter-=1
		if(counter>=maxCounter):
			maxCounter=counter
			index=x
	return index

def ReverseN(N):
	newList=['+' if v=='-' else '-' for v in N]
	newList.reverse()
	return newList

def GetManeuverOfListOfSizeN(N):
	currentIndex=len(N)-1
	minManeuverCounter=0
	while (currentIndex>=0):
		# print("N: "+str(N))
		# input()
		if(N[currentIndex]=="+"):
			currentIndex-=1
		else:
			minManeuverCounter+=1
			if(N[0]=="-"):
				newList=ReverseN(N[:currentIndex+1])
				# print("newList: "+str(newList))
				for i in range(len(newList)):
					N[i]=newList[i]
			else:
				index=GetMaxPositiveIndex(N[:currentIndex+1])
				newList=ReverseN(N[:index+1])
				# print("index: "+str(index))
				# print("newList: "+str(newList))
				for i in range(len(newList)):
					N[i]=newList[i]
	return minManeuverCounter

numOfTestCase=int(content.pop(0))
for x in range(numOfTestCase):
	N=list(content.pop(0).strip()	)
	# print("N: "+str(N))
	print("Case #%d: %s"%(x+1,GetManeuverOfListOfSizeN(N)))


# # def findMaxOccouranceIndex(N):
# # 	indexMaxOccouranceList=[]
# # 	print("N: findMaxOccouranceIndex "+str(N))			
# # 	counter=0
# # 	for x in  range(len(N)):
# # 		if(N[x]=='+'):
# # 			counter+=1
# # 		else:
# # 			counter-=1
# # 		indexMaxOccouranceList.append(abs(counter))
# # 	maxValue=max(indexMaxOccouranceList)
# # 	minValue=min(indexMaxOccouranceList)
# # 	lst= [i for i, x in enumerate(indexMaxOccouranceList) if x == maxValue]	
# # 	if('+' in N and '-' in N and len(N)>2):
# # 		lst+=	[i for i, x in enumerate(indexMaxOccouranceList) if x == minValue]	
# # 	lst=list(set(lst))
# # 	print("lst: "+str(lst))			
# # 	return lst


# def findMaxOccouranceIndex(N):
# 	indexMaxOccouranceList=[]
# 	print("N: findMaxOccouranceIndex "+str(N))			
# 	counter=0
# 	for x in  range(len(N)):
# 		if(N[x]=='+'):
# 			counter+=1
# 		else:
# 			counter-=1
# 		indexMaxOccouranceList.append(counter)
# 	maxValue=max(indexMaxOccouranceList)
# 	minValue=min(indexMaxOccouranceList)
# 	if(N[0]=="+"):
# 		lst= [i for i, x in enumerate(indexMaxOccouranceList) if x == maxValue]	
# 	else:
# 		lst= [i for i, x in enumerate(indexMaxOccouranceList) if x == minValue]	


# 	# if('+' in N and '-' in N and len(N)>2):
# 	# 	lst+=	[i for i, x in enumerate(indexMaxOccouranceList) if x == minValue]	
# 	lst=list(set(lst))
# 	print("lst: "+str(lst))			
# 	return lst


# def GetPopedListAfterMaeuver(N):
# 	print("N: popedUpList "+str(N))			
# 	popedUpList=['+' if v=='-' else '-' for v in N]
# 	popedUpList.reverse()
# 	print("popedUpList "+str(popedUpList))			
# 	return popedUpList

# def GetManeuverOfListOfSizeN(N):
# 	listLength=len(N)
# 	print("N: "+str(N))
# 	input()
# 	if(listLength==0):
# 		return 0
# 	elif(N[listLength-1]=="+"):
# 		return GetManeuverOfListOfSizeN(N[:listLength-1])
# 	else:
# 		indexsMaxOccourance=findMaxOccouranceIndex(N[:listLength])
# 		tempMin=[]
# 		for item in indexsMaxOccourance:
# 			tempN=list(N)
# 			popedUPListAfterManeuver=GetPopedListAfterMaeuver(N[:item+1])
# 			for x in range(len(popedUPListAfterManeuver)):
# 				tempN[x]=popedUPListAfterManeuver[x]
# 			print("tempN after maneuver: "+str(tempN))
			
# 			tempMin.append(GetManeuverOfListOfSizeN(tempN))
# 		print("tempMin: "+str(tempMin))
# 		return min(tempMin)+1

# # def MinManeuverToGetAllHappySide(N):	
# # 	currentIndex,maneuverCounter=len(N)-1,0	
# # 	while currentIndex>=0:
# # 		if(N[currentIndex]=='+'):
# # 			currentIndex-=1
# # 		else:
# # 			# print("N: "+str(N))			
# # 			indexMaxOccourance=findMaxOccouranceIndex(N[:currentIndex+1])
# # 			# print("indexMaxOccourance: "+str(indexMaxOccourance))			
# # 			popedUPListAfterManeuver=GetPopedListAfterMaeuver(N[:indexMaxOccourance+1])
# # 			# print("popedUPListAfterManeuver: "+str(popedUPListAfterManeuver))			
# # 			for x in range(len(popedUPListAfterManeuver)):
# # 				N[x]=popedUPListAfterManeuver[x]
# # 			maneuverCounter+=1
# # 	return maneuverCounter
					


# numOfTestCase=int(content.pop(0))
# for x in range(numOfTestCase):
# 	N=list(content.pop(0).strip()	)
# 	# print("N: "+str(N))
# 	print("Case #%d: %s"%(x+1,GetManeuverOfListOfSizeN(N)))
