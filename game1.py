import random
class project:
	def first(self,player):
		computer = random.randint(1,3)
		stone1 = computer == 1
		papper1 = computer == 2
		siser1 = computer == 3
		stone = 1
		papper = 2
		siser = 3
        	if stone==siser1 or siser==papper1 or papper==stone1:
		    	print("player win!..")
	 		elif stone==stone1 or siser==siser1 or papper==papper1:
		    	print("match die!..")

			else:
		    	print("computer win!..")

obj = project()
obj.first(1)
