class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
    def __getattribute__(self, attr_name):
        if attr_name == "name":
            return object.__getattribute__(self, attr_name).title()
        elif attr_name == "price":
            return 2 * object.__getattribute__(self, attr_name)
        else:
            return object.__getattribute__(self, attr_name)
    def __getattr__(self, attr_name):
        if attr_name == "total":
            return self.price * self.amount
        else:
            raise AttributeError
i = Item("apple", 4, 5)
print(f"{i.name}: {i.total}")