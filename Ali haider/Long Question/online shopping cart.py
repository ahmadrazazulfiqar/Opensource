# Base class for all products
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Abstract method to calculate the price
    def calculate_price(self):
        pass

# Subclass for physical products
class PhysicalProduct(Product):
    def calculate_price(self):
        return self.price

# Subclass for digital products
class DigitalProduct(Product):
    def calculate_price(self):
        return self.price

# Class representing the shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart = []

    # Add a product to the cart
    def add_to_cart(self, product):
        self.cart.append(product)

    # Remove a product from the cart
    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print(f"{product.name} is not in the cart.")

    # Calculate the total price of the items in the cart
    def calculate_total_price(self):
        total_price = sum(product.calculate_price() for product in self.cart)
        return total_price

    # Checkout
    def checkout(self):
        total_price = self.calculate_total_price()
        print(f"Total price: ${total_price}")
        print("Checkout successful. Thank you for your purchase!")

# Example usage:

# Create products
physical_product = PhysicalProduct("Laptop", 1000)
digital_product = DigitalProduct("Ebook", 20)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_to_cart(physical_product)
cart.add_to_cart(digital_product)

# Calculate the total price
total_price = cart.calculate_total_price()
print(f"Total price in the cart: ${total_price}")

# Remove a product from the cart
cart.remove_from_cart(physical_product)

# Calculate the total price again
total_price = cart.calculate_total_price()
print(f"Total price in the cart after removal: ${total_price}")

# Checkout
cart.checkout()
