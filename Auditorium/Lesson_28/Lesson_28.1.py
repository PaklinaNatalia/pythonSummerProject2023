class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
a = Node(1)
b = Node(22)
a.next_node = b
c = Node(333)
b.next_node = c
d = Node(4444)
c.next_node = d
e = Node(55555)

x = a
while x.next_node != None:
    print(x.value)
    x = x.next_node
else:
    x.next_node = e
    print(x.value)
    print(x.next_node.value)