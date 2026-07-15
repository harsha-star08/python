'''a=[8,9,4,2,3]
n=len(a)
for i in range(1,n):
    for j in range(1,n):
        if a[j]<a[j-1]:
            b=a[j]
            a[j]=a[j-1]
            a[j-1]=b
print(a)
Bubble sort'''
'''a=[8,9,4,2,3]
n=len(a)
for i in range(1,n):
    j=i-1
    k=a[i]
    while (j>=0 and a[j]>k):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=k
print(a) insertin sort'''
''''insert at last

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        nn = Node(val)
        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            self.tail = nn

    def displayHead(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")
    


l1 = LinkedList()

while True:
    val = int(input())
    if val != -1:
        l1.insert(val)
    else:
        break

l1.display()'''
'''
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_last(self, val):
        nn = Node(val)

        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            nn.prev = self.tail       
            self.tail = nn           

    def displayHead(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next

        print("None")

    def displayTail(self):
        temp = self.Tail
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.prev
        print("None")

    
l1 = DoublyLinkedList()

while True:
    val = int(input())
    if val == -1:
        break
    l1.insert_last(val)

l1.display()'''

'''class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_last(self, val):
        nn = Node(val)

        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            nn.prev = self.tail       
            self.tail = nn   
    def palindrome(self):
        left=self.head
        right=self.tail
        if left!=right:
            if left.data!=right.data:
               return False
            left=left.next
            right=right.prev
        return True


    def displayHead(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next

        print("None")

    def displayTail(self):
        temp = self.Tail
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.prev
        print("None")
l1 = DoublyLinkedList()
while True:
    val = int(input())
    if val == -1:
        break
    l1.insert_last(val)
l1.displayHead()
print(l1.palindrome())'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

    # Insert at Beginning
    def insert_begin(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn


    def insert_pos(self, pos, val):
        nn = Node(val)

        if pos == 0:
            nn.next = self.head
            self.head = nn
            return

        temp = self.head
        for i in range(pos - 2):
            temp = temp.next

        nn.next = temp.next
        temp.next = nn
l1=Linked()
l1.insert_begin(5)
l1.insert_begin(7)

l1.insert_pos( 1,15)
l1.display()'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at End
    def insert(self, val):
        nn = Node(val)

        if self.head is None:
            self.head = nn
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = nn

    # Display
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Insert at Beginning
    def insert_begin(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn

    # Insert at Position (0-based)
    def insert_pos(self, pos, val):
        nn = Node(val)

        if pos == 0:
            nn.next = self.head
            self.head = nn
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        nn.next = temp.next
        temp.next = nn

    # Delete Beginning
    def delete_begin(self):
        if self.head:
            self.head = self.head.next

    # Delete End
    def delete_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete at Position (0-based)
    def delete_pos(self, pos):

        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        temp.next = temp.next.next

    # Search
    def search(self, key):

        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                print("Found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Not Found")

    # Reverse
    def reverse(self):

        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # Find Middle
    def middle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle =", slow.data)

    # Detect Cycle
    def cycle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cycle Detected")
                return

        print("No Cycle")


# ---------------- Driver Code ----------------

l = LinkedList()

while True:
    x = int(input("Enter value (-1 to stop): "))
    if x == -1:
        break
    l.insert(x)

print("\nOriginal List")
l.display()

print("\nInsert at Beginning")
l.insert_begin(5)
l.display()

print("\nInsert at Position")
l.insert_pos(2, 15)
l.display()

print("\nDelete Beginning")
l.delete_begin()
l.display()

print("\nDelete End")
l.delete_end()
l.display()

print("\nDelete Position")
l.delete_pos(2)
l.display()

print("\nSearch")
l.search(30)

print("\nReverse")
l.reverse()
l.display()

print("\nMiddle")
l.middle()

print("\nCycle Check")
l.cycle()

