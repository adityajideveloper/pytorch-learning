import csv

class Item:
    pay_rate = 0.8  # <- Price after 20% discount
    all = []

    def __init__(self, name: str, price: int = 0, quantity=0):
        # This function will automatically called when Item() is used
        # print(f"An instance created: {name}")

        # Run Validatons to the recieved arguments
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >= 0, f"Price {price} is not >= 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')" # <- Best Practices acc to python documentation
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('./oop/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


item1 = Item("Phone", 100, 5)  # <- __init__ will be called automatically
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

item2 = Item("Laptop", 1000, 3)
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

item2.has_numpad = False

print(f"Name -> {item1.name}, Price -> $ {item1.price}, Quantity -> {item1.quantity}, Total -> $ {item1.calculate_total_price()}")
print(f"Name -> {item2.name}, Price -> $ {item2.price}, Quantity -> {item2.quantity}, Total -> $ {item2.calculate_total_price()}")

# item3 = Item(1, 100, -1)
# print(item3.name, type(item3.price))

print(item1.pay_rate)
print(Item.__dict__)  # All attributes for class level
print("------------------------------------------------")
print(item1.__dict__)  # All attribute for instance level

item1.apply_discount()
print(item1.price)

# Apply 30% discount for Laptop
item2.pay_rate = 0.7
item2.apply_discount()
print(f"Name -> {item2.name}, Price -> $ {item2.price}, Quantity -> {item2.quantity}, Total -> $ {item2.calculate_total_price()}")

item3 = Item("iMac", 700, 1)
item4 = Item("Mac Studio", 600, 5)
item5 = Item("Mouse", 10, 100)

print("-----------------------------------------------")
for instances in Item.all:
    print(instances.name)

print("-----------------------------------------------")
print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.5))