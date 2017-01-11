from bangazon import *

class Marketing(Department):

	def __init__(self, name, supervisor, employee_count):
		super(Marketing, self).__init__(name, supervisor , employee_count)
		self.policies = {}


	def add_policy(self, policy_name, policy_text):
		self.policies.add((policy_name, policy_text))

drewMarketing = Marketing("Marketing" , "Paul Andrew Martin" , 6)

print(drewMarketing.name)