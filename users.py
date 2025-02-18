from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self,name,phone,email,address):
        self.name = name 
        self.phone = phone
        self.email = email
        self.address = address
        
class Customer(User):
    
    def __init__(self,name,phone,email,address,money):
        self.wallet = money
        self.__order = None
        super().__init__(name,phone,email,address)
    
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order = order 
    
    def place_order(self,order):
        self.order = order
        print(f'{self.name} ordered {order.items}')
        
    def eat_food(self,order):
        print(f'{self.name} is eating {order.items}') 
    
    def pay(self_for_order,amount):
        pass
    
    def give_tips(self,tips_amount):
        pass
    
    def write_review(self,stars):
        pass

class Employee(User):
    
    def __init__(self,name,phone,email,address,salary,starting_date,department):
        super().__init__(name,phone,email,address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department  
        
    def receive_salary(self):
        self.due = 0
class Chef(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department,cooking_item):
        super().__init__(name,phone,email,address,salary,starting_date,department)
        self.cooking_item = cooking_item 
        
class Server(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department):
        self.tips_earning = 0
        super().__init__(name,phone,email,address,salary,starting_date,department)
    def take_order(self,order):
        pass
    def transfer_order(self,order):
        pass
    def serve_food(self,order):
        pass
    def receive_tips(self,tips):
        self.tips_earning +=tips

class Manager(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department):
        super().__init__(name,phone,email,address,salary,starting_date,department)
        