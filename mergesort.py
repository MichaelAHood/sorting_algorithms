def mergesort(arr):
	"""	
	Input:  An unsorted array of integers or floats
	Output: A sorted array of integers or floats
	Desc:   My implementation of the merge sort algorithm. 

	"""

	if len(arr) < 2:
		return arr

	# choose a midpoint to be at the middle (more or less) of an array
	midPt = len(arr) / 2

	# split the arrays into a left and right half
	left  = arr[:midPt]
	right = arr[midPt:]

	# call the merge function tom sort the elements of each
	# half and merge them back into a -- newly sorted -- array
	return merge( mergesort(left), mergesort(right) ) 

def merge(left, right):

	# create a bucket to hold the sorted elements of left and right
	res = []

	# i and j are going to be point at the index of the left 
	# and right arrays as we iterate over the elements, sort
	# them and put them back into res
	i = 0
	j = 0

	# Since left and right are already sorted, we can loop
	# over them and pick out the smallest of the first two elements.
	# We can then increment i or j, and repeat.
	# Once either i or j is equal to the lenth of it's respective
	# array we can end the loop. 
	while i < len(left) and j < len(right):
		
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1

	# Merge the res array with the remaining elements of left and right		
	return res + left[i:] + right[j:]


if __name__ == '__main__':
	
	import numpy as np

	arr = np.random.choice(xrange(-100, 100), size=20).tolist()

	print "The unsorted array is: ", arr
	print "The sorted array is: ", mergesort(arr)
	assert mergesort(arr) == sorted(arr), "Sorted incorrectly!"


