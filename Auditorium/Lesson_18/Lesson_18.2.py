class Tree:
    def __init__(self, kind, height):
        self.kind = kind
        self.height = height
        self.age = 0

    def grow(self):
        self.age += 1

class Fruit_Tree(Tree):
    def __init__(self, kind, height):
        super().__init__(kind, height)

    def give_fruits(self, harvest):
        print(f"{harvest} kg of {self.kind}")

apple_tree = Fruit_Tree("Apple", 0.7)
apple_tree.give_fruits(20)
orange_tree = Fruit_Tree("Orange", 1)
orange_tree.give_fruits(30)