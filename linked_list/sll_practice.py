from .singly_linked_list import Node, LinkedList

# brute force creating and attaching nodes.
# first = Node('A')
# second = Node('B')
# third = Node('C')
# fourth = Node('D')
# fifth = Node('E')

# first.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth

# def print_ll(currNode):
#   while currNode is not None:
#     print(currNode.data, end=" -> " if currNode.next else "")
#     currNode = currNode.next

# head = None

# def insertAtHead(head, data):
#   newNode = Node(data)
#   newNode.next = head
#   head = newNode
#   return head

# print_ll(head)

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.insertAtHead(20)
ll.insertAtHead(30)

ll.insertAtTail(10)

length = ll.ll_length()
ll.insertAtPosition(3, 900)

ll.deleteHead()
ll.deleteLast()
ll.deleteAt(length)
ll.print_ll()
