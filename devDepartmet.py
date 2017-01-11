from bangazon import *

class Development(Department):

	def __init__(self, name, supervisor, employee_count):
		super(Development, self).__init__(name, supervisor , employee_count)
		self.policies = {}


	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

drewsDev = Development("development" , "drew martin" , 12)

print(drewsDev.name)