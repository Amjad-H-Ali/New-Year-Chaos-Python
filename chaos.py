print("New Year Chaos!")

def min_bribes(array):

	for i in range(0, len(array)):
		if (array[i] - (i + 1) >= 3):
			return "Too Chaotic!"
print(min_bribes([1, 2, 3, 4, 8, 5, 7, 6]))		
