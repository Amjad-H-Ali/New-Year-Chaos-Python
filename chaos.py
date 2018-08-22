print("New Year Chaos!")

def min_bribes(array):
	for i in range(len(array) - 1, -1, -1):
		print(i)
		# If integer is 3 indexes or more off from original position in array
		# if (e - (i + 1) >= 3):
		# 	return "Too Chaotic!"
min_bribes([1, 2, 3, 4, 8, 5, 7, 6])
