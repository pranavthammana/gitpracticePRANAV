#Partner1: Pranav Thammana
#Partner2: Vivek Mittal-Henkle
##############
#Assignment name: github practice - 20 points - 3/3/2020
import random as rand

def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
	ints = []
	for i in range(int(n)):
		ints.append(rand.randint(0, 10))
	return ints
print(getNRandom(2))

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
	pass

def main():
	#print(multiplyRandom(getNRandom(10)))
	pass

if __name__ == "__main__":
	main()
