from bangazon import *

class Development(Department):

	def __init__(self, name, supervisor, employee_count, budget):
		super(Development, self).__init__(name, supervisor , employee_count, budget)
		self.policies = set()

	def meet(Development):
		print("Everyone meet in the server room")	

	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

	def get_budget(self, budget):
		super(Development, self).get_budget(budget)
		return self.budget

drewsDev = Development("development" , "drew martin" , 12, 10000)

drewsDev.add_policy("Don't Do this" , "Punch the Supervisor")
print(drewsDev.get_budget(45000))
print(drewsDev.budget) 