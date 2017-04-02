import time

def tinker():

	max_num = int(input("Give me a range: "))
	step = int(input("Give me a step: "))
	
	start = time.clock()
	counter = 0
	numbers = []

	[numbers.append(True) for i in range(max_num)]

	# print("NUMBERS: {}".format(numbers))
	while numbers.count(True) != 1:
		for i in range(0, len(numbers)):
			if numbers[i] == True:
				counter += 1
			if counter == step:
				numbers[i] = False
				counter = 0

		# print(numbers)

	print("RESULT: {}".format(numbers.index(True)+1))
	print("TIME ELAPSED: {}".format(time.clock() - start))

tinker()

