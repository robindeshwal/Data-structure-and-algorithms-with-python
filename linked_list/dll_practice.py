from .doubly_linked_list import Node, LinkedList

# first = Node(10)
# second = Node(20)
# third = Node(30)

# first.next = second
# second.prev = first

# second.next = third
# third.prev = second

# print("printing doubly linked list.")

# def print_ll(head):
#   temp = head
#   while temp:
#     print(temp.data, end=" -> " if temp.next else "")
#     temp = temp.next

# def ll_length(head):
#   len = 0
#   currNode = head
#   while currNode:
#     len += 1
#     currNode = currNode.next

#   return len

# def insertAtHead(head, data):
#   newNode = Node(data)
#   if head is None:
#     head = newNode
#     tail = newNode
#     return

#   head.prev = newNode
#   newNode.next = head
#   head = newNode
#   return head

# def insertAtTail(self, head, data):
#   newNode = Node(data)
#   if head is None:
#     head = newNode
#     tail = newNode
#     return

#   tail.next = newNode
#   newNode.prev = tail
#   tail = newNode

ll = LinkedList()

ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.insert(40)
# ll.insert(50)
# ll.insert(60)

ll.print_ll()
length = ll.ll_length()
print("\nLength :", length)

# ll.insertAtHead(1000)
# ll.insertAtTail(500)
# ll.insertAtPosition(5, 300)

# ll.deleteHead()
# ll.deleteTail()
ll.deleteAtPosition(2)

ll.print_ll()
length = ll.ll_length()
print("\nAfter length :", length)
