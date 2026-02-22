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
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end='->')
                temp = temp.next
            print('None')

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            prev = None
            while temp is not None and count < index:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = new_node
            new_node.next = temp

    def delete_node(self, data):
        if self.head is None:
            return

        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return

        prev = None
        while temp is not None:
            if temp.data == data:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def find_middle(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        temp = self.head
        for i in range(0, count // 2):
            temp = temp.next
        print(f'Middle element is {temp.data}')

    def find_middle_slow_fast(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(f'Middle element using slow and fast pointers : {slow.data}')


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
# ll.insert_at_index(5, 3)
# ll.delete_node(40)
# ll.find_middle()
ll.find_middle_slow_fast()
ll.display()
