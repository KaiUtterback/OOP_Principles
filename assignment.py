'''1. Encapsulation in Personal Budget Management
Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. 
Students will apply these concepts to create a Personal Budget Management system.

Problem Statement: You are required to build a Personal Budget Management application. 
The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class
 Create a class BudgetCategory with private attributes for category name and allocated budget.
 Initialize these attributes in the constructor.

 Expected Outcome: A BudgetCategory class capable of storing category details securely.

Task 2: Implement Getters and Setters
 Write getter and setter methods for both the category name and the allocated budget.
 Ensure that the setter methods include validation (e.g., budget should be a positive number).
 
 Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

Task 3: Add Budget Functionality
 Implement a method to add expenses to a category and adjust the budget accordingly.
 Validate the expense amount before making deductions from the budget.
 
 Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

Task 4: Display Budget Details
 Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
 Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
'''

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = 0

    # Getters
    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def get_expense(self):
        return self.__expense

    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expense

    # Setters
    def set_category_name(self, name):
        if isinstance(name, str):
            self.__category_name = name

    def set_allocated_budget(self, budget):
        if isinstance(budget, (int, float)) and budget >= 0:
            self.__allocated_budget = budget

    # Methods
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.get_remaining_budget():
                self.__expense += amount
            else:
                raise ValueError("Expense exceeds remaining budget.")
        else:
            raise ValueError("Invalid expense amount.")

    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocated_budget()}")
        print(f"Total Expenses: ${self.get_expense()}")
        print(f"Remaining Budget: ${self.get_remaining_budget()}")


print("\nBudget Management:")
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

'''
2. E-commerce Product Catalog System
Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. 
Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. 
Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

Task 1: Create Base Product Class
Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
Expected Outcome: A Product class that can hold general information about a product and display it.

Task 2: Implement Subclasses for Specific Products
Create subclasses Book, Electronic, and Clothing that inherit from Product.
Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

Task 3: Override Display Method in Subclasses
Override the method to display product information in each subclass to include specific attributes.
For example, the Book class should display the author, Electronic should display specs, etc.
Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

Task 4: Test Product Catalog Functionality
Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.

'''

class Product:
    def __init__(self, product_ID, name, price):
        self.__product_ID = product_ID
        self.name = name
        self.price = price

    def get_product_ID(self):
        return self.__product_ID

    def set_product_ID(self, product_ID):
        if isinstance(product_ID, str):
            self.__product_ID = product_ID

    def display_info(self):
        print(f"Product ID: {self.get_product_ID()}, Name: {self.name}, Price: ${self.price}")



class Book(Product):
    def __init__(self, product_ID, name, price, author):
        super().__init__(product_ID, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")



class Electronic(Product):
    def __init__(self, product_ID, name, price, specs):
        super().__init__(product_ID, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specs: {self.specs}")



class Clothing(Product):
    def __init__(self, product_ID, name, price, size):
        super().__init__(product_ID, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


print("\nE Commerce Product Catalog System")
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_electronic = Electronic("456", "Smartphone", 999.99, "256GB, 8GB RAM")
my_clothing = Clothing("789", "T-Shirt", 19.99, "Medium")

my_book.display_info()
my_electronic.display_info()
my_clothing.display_info()