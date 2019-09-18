
def getCount(array, total,start):
	if 0 > total: return 0
	if 0 == total: return 1
	if 0 == len(array): return 0
	
	if True == start:
		count = getCount(array[1:], total-array[0], False)\
			+ getCount(array[1:], total, True)
	else:
		count = getCount(array[1:], total-array[0], False)
			
	return count
	

def getCount2(array, total):
	if 0 == total: return 1
	if 0 == len(array): return 0
	
	tail = 0
	head = 0
	tempTot = array[0]
	count = 0
	
	while True:
		if tempTot == total:
			count+=1
		
		if tempTot >= total:
			tempTot -= array[tail]
			tail+=1
			if len(array) == tail: break
		else:
			head+=1
			if len(array) == head: break
			tempTot += array[head]
	
	return count
		
		
		
		
		
		
		
		

if __name__ == '__main__':
	array = (2,4,2,5,3,2,2,1,1,4, 8 ,90,2,5,3,1,2,8)
	total = 6
	print str(getCount(array, total, True))
	print str(getCount2(array, total))
