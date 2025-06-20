
from item import Item
from phone import Phone

item1 = Item('Phone', 750, 20)

item1.name = 'Samsung'

item1.apply_increment(0.2)

print(item1.price)