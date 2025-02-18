class Restautant:
    def __init__(self,name):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = []
        self.revenue = 0
        self.profit = 0
    
    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server  = employee
        elif employee_type == 'manager':
            self.manager = employee
             