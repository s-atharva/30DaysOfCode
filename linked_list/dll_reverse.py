class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
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
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('None')

    def reverse(self):
        if self.head is None:
            return self.head
        current = self.head
        prev = None
        while current:
            front = current.next
            current.next = prev
            current.prev = front
            prev = current
            current = front

        self.head = prev


dll = DoublyLinkedList()
dll.append_node(10)
dll.append_node(20)
dll.append_node(30)
dll.append_node(40)
dll.append_node(50)
dll.append_node(60)
dll.display()
dll.reverse()
dll.display()
