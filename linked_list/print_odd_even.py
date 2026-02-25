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

    def print_even_odds(self):
        if self.head is None or self.head.next is None:
            return

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

ll.display()
ll.print_even_odds()
ll.display()
