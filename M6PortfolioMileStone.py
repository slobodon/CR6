class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    #define methods
    def add_items(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)


    def remove_item(self, item_name):
        pass

    def modify_item(self, item):
        pass

    def get_num_items_in_cart(self):

        totalItems = 0
        for item in self.cart_items:
            totalItems += item[1]
        return totalItems 
        

    def get_cost_of_cart(self):
        #calculate the total cost of the cart
        totalCost = 0
        for item in self.cart_items:
            totalCost += item[1]*item[2] 
        return totalCost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name , self.current_date).center(50))

        numberofitems = self.get_num_items_in_cart()
        print('Number of items: {}'.format(numberofitems).center(50) )
         #print a summary of each item   
        for Item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(Item[0], Item[1], Item[2], Item[1]*Item[2]).center(50))

        totalCost = self.get_cost_of_cart()    

        print('Total: ${}'.format(totalCost).center(50))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name , self.current_date).center(50))
        for Item in self.cart_items:
            print('{}: {} '.format(Item[0], Item[3]).center(50))


#Main body of code

    
def print_menu():
    #invalid = 1
    option = 'none'
    while option == 'none'or option != 'q':
        print('MENU'.center(50))
        print('a - Add item to cart'.center(50))
        print('r - Remove item from cart'.center(50))
        print('c - Change item quantity'.center(50))
        print('i - Output items\' descriptions'.center(50))
        print('o - Output shopping cart'.center(50))
        print('q - Quit'.center(50))
        option = input('Choose an option: '.center(50))
        if option in ['a', 'r', 'c', 'i', 'o']:
            if option == 'i':
                print('OUTPUT ITEM\'S DESCRIPTIONS'.center(50))
                my_cart.print_descriptions()
            elif option=='o':
                print('OUTPUT SHOPPING CART'.center(50))
                my_cart.print_total()
            else:
                print(option)
        elif option=='q':
            print()
        else:
            print('Invalid Choice. Please Choose a Valid Option.'.center(50))





#option = print_menu()

#print(option)7

CustomerName = 'John Doe'
Date = 'February 1,  2020'

testShoppingCart = [['Nike Romaleos', 2, 189, 'Volt color, Weightlifting shoe'],
                    ['Chocolate Chips', 5, 3, 'Semi-sweet'],
                    ['Powerbeats 2 Headphones', 1, 128, 'Bluetooth headphones']]

my_cart = ShoppingCart(CustomerName, Date)

for item in testShoppingCart:
    my_cart.add_items(item)

print_menu()




#my_cart.print_total()
#print()
#my_cart.print_descriptions()



















































