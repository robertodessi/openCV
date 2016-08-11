def mergeSort(listOrd):

	# merge method to merge two sorted list into one
	def merge(l1, l2):

		result = []
		item = None 

		while l1 and l2:
			if l1[0] < l2[0]:
				item = l1[0]
				result.append(l1[0])
				l1.remove(l1[0])

			else:
				item = l2[0]
				result.append(l2[0])
				l2.remove(l2[0])

		while (l1):
			item = l1[0]
			result.append(l1[0])
			l1.remove(item)


		while (l2):
			item = l2[0]
			result.append(l2[0])
			l2.remove(l2[0])

		return result
	# end of merge method

	assert len(listOrd) is not 0

	if len(listOrd) == 1:
		return listOrd
	else:
		p = len(listOrd)/ 2
		end = len(listOrd)
		l1 = mergeSort(listOrd[0:p])
		l2 = mergeSort(listOrd[p:end])
		return merge(l1,l2)

def insertionSort(listOrd):
	leng = len(listOrd)
	for x in xrange(1,leng):
		index = x - 1
		while index >= 0 and listOrd[index] > listOrd[index+1]:
			temp = listOrd[index+1]
			listOrd[index+1] = listOrd[index]
			listOrd[index] = temp
			index-=1
	return listOrd

def selectionSort(listOrd):
	def swap(x, xx, listOrd):
		temp = listOrd[x]
		listOrd[x] = listOrd[xx]
		listOrd[xx] = temp

	for x in xrange(len(listOrd)):
		temp = listOrd[x]
		for xx in xrange(x+1, len(listOrd)):
			if(listOrd[x] > listOrd[xx]): 
				swap(x, xx, listOrd)

	return listOrd

def quickSort(listOrd):
	if len(listOrd) == 1:
		return listOrd
	else:
		pivot = listOrd[len(listOrd)-1]
		l1 = [for x in listOrd if x <= pivot]
		l2 = [for x in listOrd if x > pivot]
		

def partition(l, low, high):


l = [3, 1, 4, 2, 9, 2]




#print mergeSort(l)
#print insertionSort(l)
#print selectionSort(l)

#print quicksort(l)
#print heapsort(l)