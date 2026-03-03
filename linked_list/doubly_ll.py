class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # insert at head
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print(f'Position out of bound')
            return

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def display(self):
        if self.head is None:
            return None
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('None')


dll = DLL()
dll.append_node(10)
dll.append_node(20)
dll.append_node(30)
dll.append_node(40)
dll.append_node(50)
dll.insert_at(10, 14)
dll.display()
