from menu import *
from restaurant import *
from users import * 
def main():
    menu = Menu()
    pizza1 = Pizza('Overload Pizza',750,'large',['meat','onion','cheese'])
    menu.add_menu_item('pizza',pizza1)
    pizza2 = Pizza('Cheese Blast',500,'large',['meat','chedar cheese','mozarella'])
    menu.add_menu_item('pizza',pizza2)
    pizza3 = Pizza('Meat Machine',1100,'large',['chicken','beef','mutton'])
    menu.add_menu_item('pizza',pizza3)
    burger1 = Burger('Beef Cheese Blast', 350,'beef',['beef','cheese','onion','secret sauce'])
    menu.add_menu_item('burger',burger1)
    burger2 = Burger('Chicken Cheese Blast', 300,'chicken',['chicken','cheese','onion','secret sauce'])
    menu.add_menu_item('burger',burger2)
    burger3 = Burger('Naga Blast',400 ,'beef',['beef','cheese','onion','secret sauce'])
    menu.add_menu_item('burger',burger3)
    drinks1 = Drinks('Mojo',25,True)
    menu.add_menu_item('drinks',drinks1)
    drinks2 = Drinks('Drinko',20,True)
    menu.add_menu_item('drinks',drinks2)
    drinks3 = Drinks('Choco',100,True)
    menu.add_menu_item('drinks',drinks3)
    
    menu.show_menu()
    
    restaurant = Restaurant ('Dhom_Machale_Restaurant',3000, menu)
    
    manager = Manager('Fardeen',5,'mdfardeenislam28@gmail.com','dhaka',3000,'28/09/20023','finance')
    restaurant.add_employee('manager',manager)

    chef = Chef('Anik Baburchi',6,'fianik27@gmail.com','dhaka',3500,'22/5/2024','Chef','everything')   
    restaurant.add_employee('chef',chef)
    
    server = Server('Chotu',6,'fianik28@gmail.com','restaurant',200,'1/1/2025','server') 
    restaurant.add_employee('server',server)
    
    restaurant.show_employees()
if __name__ == '__main__':
    main()