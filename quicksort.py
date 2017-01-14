import random

def quicksort(arr):
	"""	
	Input:  An unsorted array of integers or floats
	Output: A sorted array of integers or floats
	Desc:   Quicksort algorithm. 

	"""

	if len(arr) < 2:
		return arr

	# Select the pivot at random
	pivot = random.choice(arr)

	lesser  = []
	equal   = []
	greater = []

	for el in arr:
		if el < pivot:    lesser.append(el)
		elif el == pivot: equal.append(el)
		else:             greater.append(el)

	return quicksort(lesser) + equal + quicksort(greater)


if __name__ == '__main__':
	
	import numpy as np

	arr = np.random.choice(xrange(-100, 100), size=20).tolist()

	print "The unsorted array is: ", arr
	print "The sorted array is: ", quicksort(arr)
	assert quicksort(arr) == sorted(arr), "Sorted incorrectly!"


# The unsorted array is:  [-97, -18, 28, -14, 42, 40, -42, -74, -75, -3, -62, -86, -100, 48, -36, -95, 12, 68, -100, -20]
# The sorted array is:  [-100, -100, -97, -95, -86, -75, -74, -62, -42, -36, -20, -18, -14, -3, 12, 28, 40, 42, 48, 68]