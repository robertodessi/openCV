def mergesort(listOrd):

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
		l1 = mergesort(listOrd[0:p])
		l2 = mergesort(listOrd[p:end])
		return merge(l1,l2)



l = [3, 1, 4, 4, 9, 2]

print mergesort(l)

