import random 

class Employee(object):
	def __init__(self, firstName , lastName):
		self.firstName = firstName
		self.lastName = lastName

	def eat(self, food = None , companions = None):
		resturants = random.choice(["Bucca" , "Olive Garden" , "McDonalds" , "Taco Bell"])

		if food != None and companions != None:
			print("{} ate at  {}  and had {} to eat ".format(self.firstName , resturants, food))
			return resturants

		

drew = Employee("Drew" , "Martin")
jack = Employee("Jack", "Pinkston")
steven = Employee("Steven" , "Wally")
joey = Employee("Joey" , "Kirby")
drew.eat(food="pizza" , companions="Jack , Alex")
