class Category:
    balance = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []
        
       
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    def withdraw(self, amount, description=''):    
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False
       
    def get_balance(self):
        self.balance = 0
        for item in self.ledger:
            self.balance += item['amount']
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, description=f'Transfer to {category.name}')
            category.deposit(amount, description = f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
    
        if ((30 - len(self.name)) % 2) != 0:
            left = (30 - len(self.name)) // 2
            right = (30 - len(self.name)) - left
            star_format = (str('*' * left + self.name + '*' * right))
               
        else:
            stars = (30 - len(self.name)) // 2
            star_format = (str('*' * stars + self.name + '*' * stars))
            
        list_format = []  
        total_format = 'Total: ' + str(self.balance)   
        for item in self.ledger:
            if len(str(item['amount'])) > 7:
                formatted_amount = f"{(str(item['amount'])[:8])}"
            else:
                formatted_amount = f"{(item['amount']):.2f}"
                
            if len(item['description']) > 23:
                formatted_description = item['description'][:23]
            else:
                formatted_description = item['description']
            space = 30 - (len(formatted_description) + len(formatted_amount))

            list_format.append(formatted_description + ' ' * space + formatted_amount)
            '\n'.join(list_format)


        return star_format + '\n' + '\n'.join(list_format) + '\n' + total_format

        
        



   
        
        
        
        
'''
Calling the transfer method on a category object 
should create a specific ledger item in that category object.

The transfer method should create a specific ledger item 
in the category object passed as its argument.

category object? is an instance of the category class. so far we have food and clothing
a specific ledger item? is a specific item in the ledger list

so its saying when you call the transfer method on an instance of the class like food
or clothing, it should create a specific item in the ledger list in that class(food/clothing)

then its saying within the transfer method, it should create a specific item in the ledger list
that belongs to the class object (food or clothing) that was passed as one of the arguments
'''
        
        
'''
food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
food.get_balance()
clothing = Category('Clothing')
food.transfer(50, clothing)
food.transfer(100, clothing)
clothing.get_balance()
clothing.check_funds(100)
'''

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.deposit(1000, 'initial deposit')
clothing.get_balance()
#tests = Category('tests')
#tests.deposit(1000, 'initial deposit')
print(food)
#print(food)




    
#def create_spend_chart(categories):
    #pass


'''
#Instance attribute: a specific trait that exists for every instance created from the class template
#So if you create an instance of a class, that means youre using the template(class) and making a specific thing.
#That thing you create will have an attribute, which is defined in the class.
'''



'''
def __str__(self):
    
        if ((30 - len(self.name)) % 2) != 0:
            left = (30 - len(self.name)) // 2
            right = (30 - len(self.name)) - left
            print(str('*' * left + self.name + '*' * right))
            
        else:
            stars = (30 - len(self.name)) // 2
            print(str('*' * stars + self.name + '*' * stars))
            
        for item in self.ledger:
            if len(str(item['amount'])) > 7:
                formatted_amount = f"{(str(item['amount'])[:8])}"
            else:
                formatted_amount = f"{(item['amount']):.2f}"
            
            
            if len(item['description']) > 23:
                formatted_description = item['description'][:23]
            else:
                formatted_description = item['description']
            
            space = 30 - (len(formatted_description) + len(formatted_amount))
        
            print(formatted_description + ' ' * space + formatted_amount)

        return 'Total: ' + str(self.balance)

'''