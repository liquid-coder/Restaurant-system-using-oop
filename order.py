class Order:
    def __init__(self,customer,items):
        self.customer = customer
        self.items = items
        total = 0
        for i in items:
            total += i.price
        self.bill = total