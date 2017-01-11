from bangazon import *

class Sales(Department):

	def __init__(self, name, supervisor, employee_count):
		super(Sales, self).__init__(name, supervisor , employee_count)
		self.policies = {}


	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

drewSales = Sales("Sales" , "Jack Pinkston" , 6)

print(drewSales.name)