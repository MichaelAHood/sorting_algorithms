def insertionsort(arr):

	window = 0

	while window < len(arr) - 1:
		for ix, el in enumerate(arr[:window + 1]):
			if arr[window + 1] < el:
				arr[ix], arr[window + 1] = arr[window + 1], el
		window += 1

	return arr

if __name__ == '__main__':
	
	import numpy as np

	arr = np.random.choice(xrange(-100, 100), size=20).tolist()

	print "The unsorted array is: ", arr
	print "The sorted array is: ", insertionsort(arr)
	assert insertionsort(arr) == sorted(arr), "Sorted incorrectly!"
