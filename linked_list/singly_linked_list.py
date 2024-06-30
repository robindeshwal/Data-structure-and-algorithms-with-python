class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  """
  """

  def __init__(self):
    self.head = None
    self.tail = None

  def is_ll_empty(self):
    if self.head is None:
      return True
    else:
      return False

  def print_ll(self):
    while self.head is not None:
      print(self.head.data, end=" -> " if self.head.next else "")
      self.head = self.head.next

  def ll_length(self):
    currNode = self.head
    length = 0
    while currNode:
      length += 1
      currNode = currNode.next
    return length

  def insert(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      return

    currNode = self.head
    while currNode.next:
      currNode = currNode.next

    currNode.next = newNode
    self.tail = newNode

  def insertAtHead(self, data):
    """
    add a new node at head, pre insert head.
    """
    newNode = Node(data)
    if not self.head:
      self.tail = newNode
    newNode.next = self.head
    self.head = newNode

  def insertAtTail(self, data):
    """
    insert at the right most end in ll.
    """
    newNode = Node(data)
    if not self.tail:
      self.tail = newNode
      self.head = newNode
    self.tail.next = newNode
    self.tail = newNode

  def insertAtPosition(self, position, data):
    """
    """
    if position < 0 or position > self.ll_length():
      print("Invalid position.")
      return

    if position == 0:
      self.insertAtHead(data)
      return

    if position == self.ll_length():
      self.insertAtTail(data)
      return

    i = 1
    currNode = self.head
    while True:
      if i == position:
        break
      currNode = currNode.next
      i += 1

    newNode = Node(data)
    newNode.next = currNode.next
    currNode.next = newNode

  def insertAfterValue(self):
    """
    """

  def deleteHead(self):
    """
    """
    if self.is_ll_empty():
      print("List is Empty")
      return

    previousHead = self.head
    self.head = self.head.next
    previousHead.next = None

  def deleteAt(self, position):
    """
    """
    if position < 0 or position > self.ll_length():
      print("Invalid position")
      return

    if position == 0:
      self.deleteHead()
      return

    if position == self.ll_length():
      self.deleteLast()
      return

    i = 0
    currNode = self.head
    previousNode = None
    while True:
      if i == position:
        previousNode.next = currNode.next
        currNode.next = None
        break
      previousNode = currNode
      currNode = currNode.next
      i += 1

  def deleteLast(self):
    """
    """
    if self.is_ll_empty():
      print("List is Empty")
      return

    currNode = self.head
    while True:
      if currNode.next == self.tail:
        break
      currNode = currNode.next

    self.tail = currNode
    currNode.next = None
