class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            print('Empty Linked List')
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current = current.next
            print('None')

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        if self.head is None:
            return

        temp = self.head
        # delete head
        if temp.data == val:
            self.head = temp.next
            return

        # search node
        prev_node = None
        found = False

        while temp is not None:
            if temp.data == val:
                found = True
                break
            prev_node = temp
            temp = temp.next

        if found:
            prev_node.next = temp.next
            print('Node deleted')
            return
        else:
            print('Node not found')


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
# sll.insert_at(123, 2)
# sll.traverse()
sll.delete(30)
sll.traverse()
