class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        if self.head is None:
            return f'No node is present in Linked List'

        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('None')

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            temp.prev = front
            prev = temp
            temp = front
        return prev


dll = DLL()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.display()
dll.head = dll.reverse()
dll.display()
