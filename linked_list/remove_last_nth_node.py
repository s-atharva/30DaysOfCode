class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print('None')

    def remove_nth_node(self):
        temp = self.head
        prev = None
        while temp.next.next is not None:
            prev = temp
            temp = temp.next
        prev.next = temp.next


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.display()
ll.remove_nth_node()
ll.display()
