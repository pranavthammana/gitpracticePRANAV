#Partner1: Pranav Thammana
#Partner2: Vivek Mittal-Henkle
##############
#Assignment name: github practice - 20 points - 3/3/2020
import random as rand

def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
	ints = []
	for i in range(int(n)):
		ints.append(rand.randint(1, 10))
	return ints

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
	product = 1
	for num in numbers:
		product *= num
	return product

def main():
	print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
	main()
