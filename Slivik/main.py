class Slivik:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.first_element = None
        self.last_element = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):
        new_Node = self.Node(value)
        if self.first_element is None:
            self.first_element = new_Node
            self.last_element = new_Node
        else:
            self.last_element.next = new_Node
            self.last_element = new_Node
        self.size += 1

    def recursive_str(self, node):
        if node is None:
            return ""
        next_str = self.recursive_str(node.next)
        return str(node.value) + " " + next_str

    def __str__(self):
        return "[" + self.recursive_str(self.first_element)[:-1] + "]"

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.first_element
        for _ in range(index):
            current = current.next
        return current.value

    def __getitem__(self, index):
        return self.get(index)

    def __adding_elements__(self, other):
        new_array = Slivik()
        current1 = self.first_element
        current2 = other.first_element
        
        while current1 and current2:
            new_array.append(current1.value + current2.value)
            current1 = current1.next
            current2 = current2.next
            
        return new_array

    def addition(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        new_Node = self.Node(value)
        if index == 0:
            new_Node.next = self.first_element
            self.first_element = new_Node

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.first_element = self.first_element.next
        else:
            current = self.first_element
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def sort(self):
        current = self.first_element
        while current:
            next_node = current.next
            while next_node:
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                next_node = next_node.next
            current = current.next
    
myarray = Slivik()
myarray.append(1)
myarray.append(3)
myarray.append(2)
print(myarray)  # [1, 3, 2]
print(myarray.get(1))  # 3
myarray.remove(1)
print(myarray)  # [1, 2]
myarray.sort()
print(myarray)  # [1, 2]
myarray.__adding_elements__(myarray)
myarray.addition(1, 10)
