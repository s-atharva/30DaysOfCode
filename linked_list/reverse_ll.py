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

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print('None')

    def reverse(self):
        my_stack = []
        temp = self.head
        while temp is not None:
            my_stack.append(temp.data)
            temp = temp.next

        temp = self.head
        while temp is not None:
            stack_data = my_stack.pop()
            temp.data = stack_data
            temp = temp.next

        return self.head

    def reverse_one_loop(self):
        if self.head is None:
            print('No nodes in linked list')
            return

        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev


ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.append(40)
# ll.append(50)
ll.traverse()
# ll.reverse()
ll.reverse_one_loop()
ll.traverse()
