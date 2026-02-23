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

    def check_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def cycle_count(self):
        my_dict = dict()
        temp = self.head
        count = 0
        while temp is not None:
            if temp in my_dict:
                return count - my_dict[temp]
            else:
                my_dict[temp] = count
                count += 1
                temp = temp.next
        return 0

    def cycle_count_slow_fast(self):
        slow = self.head
        fast = self.head
        count = 0
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count += 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.head.next.next.next.next = ll.head.next

print(ll.check_cycle())
print(ll.cycle_count())
print(ll.cycle_count_slow_fast())
# ll.display()
