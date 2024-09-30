# 80. Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.

# Function to search for an item by price in the dictionary
def search_item_by_price(price_dict, search_price):
    # Find the item with the given price
    items = [item for item, price in price_dict.items() if price == search_price]
    
    if items:
        print(f"Item(s) with price {search_price}:")
        for item in items:
            print(item)
    else:
        print(f"No item found with price {search_price}.")

# Taking a dictionary and search price as input from the user
print("Enter a dictionary of items and their prices (e.g., {'apple': 1.2, 'banana': 0.5}):")
input_str = input()
price_dict = eval(input_str)

print("Enter the price to search for:")
search_price = float(input())

# Searching for the item(s) by price
search_item_by_price(price_dict, search_price)
