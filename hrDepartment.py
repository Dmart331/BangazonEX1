from bangazon import *

class HumanResources(Department):

	def __init__(self, name, supervisor, employee_count):
		super(HumanResources, self).__init__(name, supervisor , employee_count)
		self.policies = {}


	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

drewHR = HumanResources("Human Resources" , "Paul Andrew Martin" , 6)

print(drewHR.name)