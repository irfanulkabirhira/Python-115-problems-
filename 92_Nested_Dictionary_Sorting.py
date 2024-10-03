# 90. Nested Dictionary Sorting: Given a nested dictionary containing product details (product name, price, and quantity), write a Python program to sort the products based on their prices in ascending order.

# Sample nested dictionary containing product details
products = {
    'product1': {
        'name': 'Laptop',
        'price': 1200,
        'quantity': 10
    },
    'product2': {
        'name': 'Smartphone',
        'price': 800,
        'quantity': 25
    },
    'product3': {
        'name': 'Tablet',
        'price': 300,
        'quantity': 15
    },
    'product4': {
        'name': 'Headphones',
        'price': 150,
        'quantity': 40
    }
}

# Function to sort products by price in ascending order
def sort_products_by_price(product_dict):
    # Extract items and sort them based on the price
    sorted_items = sorted(product_dict.items(), key=lambda item: item[1]['price'])
    # Convert sorted items back into a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict

# Sorting the products and printing the result
sorted_products = sort_products_by_price(products)
print("Products sorted by price in ascending order:")
for product_id, details in sorted_products.items():
    print(f"Product ID: {product_id}")
    print(f"  Name: {details['name']}")
    print(f"  Price: ${details['price']}")
    print(f"  Quantity: {details['quantity']}")
    print()
