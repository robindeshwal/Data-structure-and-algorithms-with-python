class Node:

  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def is_ll_empty(self):
    if self.head is None:
      print("List is empty.")
      return True
    return False

  def print_ll(self):
    temp = self.head
    while temp:
      print(temp.data, end=" -> " if temp.next else "")
      temp = temp.next

  def ll_length(self):
    len = 0
    currNode = self.head
    while currNode:
      len += 1
      currNode = currNode.next

    return len

  def insertAtHead(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      return

    self.head.prev = newNode
    newNode.next = self.head
    self.head = newNode

  def insertAtTail(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      return

    self.tail.next = newNode
    newNode.prev = self.tail
    self.tail = newNode

  def insert(self, data):
    self.insertAtTail(data)

  def insertAtPosition(self, position, data):
    if position < 0 or position > self.ll_length():
      print("Invalid Position.")
      return

    if position == 0:
      self.insertAtHead(data)
      return

    if position == self.ll_length():
      self.insertAtTail(data)
      return

    i = 1
    currNode = self.head
    prevNode = None
    newNode = Node(data)
    while True:
      if i == position + 1:
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = currNode
        currNode.prev = newNode
        break
      prevNode = currNode
      currNode = currNode.next
      i += 1

  def deleteHead(self):
    if self.is_ll_empty():
      return

    nextHead = self.head.next
    if nextHead:
      nextHead.prev = None
    self.head = nextHead

  def deleteTail(self):
    if self.is_ll_empty():
      return

    if self.ll_length() == 1:
      self.head = None
      self.tail = None
      return

    newTail = self.tail.prev
    newTail.next = None
    self.tail = newTail

  def deleteAtPosition(self, position):
    if position < 0 or position > self.ll_length():
      print("Invalid position.")
      return

    if position == 0:
      self.deleteHead()
      return

    if position == self.ll_length():
      self.deleteTail()
      return

    i = 1
    currNode = self.head
    prevNode = None
    while True:
      if i == position + 1:
        prevNode.next = currNode.next
        currNode.next.prev = prevNode
        currNode.next = None
        return
      prevNode = currNode
      currNode = currNode.next
      i += 1
