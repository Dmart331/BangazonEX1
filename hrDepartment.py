from bangazon import *

class HumanResources(Department):

	def __init__(self, name, supervisor, employee_count, budget):
		super(HumanResources, self).__init__(name, supervisor , employee_count, budget)
		self.policies = {}


	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

	def get_budget(self, number):
            self.budget = number
            return self.budget

drewHR = HumanResources("Human Resources" , "Paul Andrew Martin" , 6 , 10000)
drewHR.get_budget(4000)
print(drewHR.budget)