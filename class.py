import random
class sample:
	def __init__(self,a):
		s = random.randint(1,3)
		print(s)
		for i in range(0,a):
			if(i%2==0):
				continue
			print(i)
		print("Welcom to anjac college")
obj = sample(30)
obj1 = sample(10)



