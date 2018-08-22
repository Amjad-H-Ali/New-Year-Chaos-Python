print("New Year Chaos!")

def min_bribes(array):
	bribes = 0
	for i in range(len(array) - 1, -1, -1):
		# If integer is 3 indexes or more away from original position in array
		if (array[i] - (i + 1) >= 3):
			return "Too Chaotic!"
		# From 1 index left of the ORIGINAl place of the integer, to where the integer is now in the array
		# Check if any number is greater than it
		# If it is, increment bribes
		for j in range(max(0, array[i] - 2), i):
			if (array[j] > array[i]):
				bribes += 1
	return bribes			



			
print(min_bribes([2, 5, 1, 3, 4])) # Too Chaotic

print(min_bribes([1, 2, 5, 3, 7, 8, 6, 4])) # 7

print(min_bribes([5, 1, 2, 3, 7, 8, 6, 4])) # Too Chaotic

print(min_bribes([1, 2, 5, 3, 4, 7, 8, 6])) # 4