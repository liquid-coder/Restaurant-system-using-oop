class Restaurant:
    def __init__(self,name,rent,menu =[]):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.order = []
        self.menu = menu
        self.rent = rent
        self.revenue = 0
        self.balance = 0
        self.expense = 0
        self.profit = 0
    
    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server  = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def add_order(self,order):
        self.orders.append(order)
      
    def receive_payment(self,order,amount,customer):
        if amount>= order.bill:
            self.revenue += amount
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money')
        
    def pay_expense(self,amount,description):
        if amount<self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')
    
    def pay_salary(self,employee):
        if employee.salary<self.balance:
            employee.receive_salary()
            
    def show_employees(self):
        print(f'Showing Employees')
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Chef: {self.server.name} with salary: {self.server.salary}')
        if self.manager is not None:
            print(f'Chef: {self.manager.name} with salary: {self.manager.salary}')