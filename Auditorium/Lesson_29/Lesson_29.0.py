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
cur_max = a.value
x = a
while True:
    if x.value > cur_max:
        cur_max = x.value
    if x.next_node == None:
        break
    x = x.next_node
print(cur_max)