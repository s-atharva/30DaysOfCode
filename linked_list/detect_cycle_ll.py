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

    def detect_cycle(self):
        temp = self.head
        my_set = set()
        found = False

        while temp is not None:
            if temp in my_set:
                found = True
                break
            my_set.add(temp)
            temp = temp.next
        if found:
            print('Loop is present.')
        else:
            print('Loop is not present.')

    def detect_cycle_two_pointers(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detect_cycle_starting_point(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return None


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.head.next.next.next.next = ll.head.next

# ll.display()
# ll.detect_cycle()
# print(ll.detect_cycle_two_pointers())
print(ll.detect_cycle_starting_point())
