# 19. Collections.OrderedDict() - HackerRank
from collections import OrderedDict

n = int(input("Enter number of items: "))
items = OrderedDict()

for _ in range(n):
    item_data = input("Enter item name and price: ").split()
    name = " ".join(item_data[:-1])
    price = int(item_data[-1])
    
    if name in items:
        items[name] += price
    else:
        items[name] = price

print("Item list:")
for name, price in items.items():
    print(f"{name} {price}")