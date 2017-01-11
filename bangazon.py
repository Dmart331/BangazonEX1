class Department(object):
 

    def __init__(self, name, supervisor, employee_count, budget):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count
        self.budget = 10000

    def meet():
        print("Everyone meet in {}'s office".format(self.supervisor))


    def get_name(self):
      """Returns the name of the department"""

      return self.name

    def get_supervisor(self):
      """Returns the name of the supervisor"""

      return self.supervisor

    def get_budget(self, number):
      self.budget = number
      return self.budget

