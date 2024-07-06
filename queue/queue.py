from collections import deque


class Queue:

  def __init__(self):
    self.items = deque()

  def is_empty(self):
    return len(self.items) == 0

  def length(self):
    return len(self.items)

  def front(self):
    if not self.is_empty():
      return self.items[0]
    return None

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if not self.is_empty():
      return self.items.popleft()
    else:
      return -1


class QueueUsingFrontRear:
  """
  TODO
  """


class CicularQueue:

  def __init__(self, max_size):
    self.size = max_size
    self.items = [None] * max_size
    self.front = -1
    self.rear = -1

  def is_full(self):
    return (self.rear + 1) % self.size == self.front

  def is_empty(self):
    return self.front == self.rear == -1

  def length(self):
    ""

  def push(self, data):
    # if queue full.
    # first element f = r = 0
    #  circular nature. (rear == n-1 and front != 0) -> rear = 0
    # default: rear ++ -> arr[rear] = data

    if self.is_full():
      print("Queue is full.")
      return
    elif self.front == -1:
      self.front += 1
      self.rear += 1
      self.items[self.front] = data
    elif self.rear == self.size - 1 and self.front != 0:
      self.rear = 0
      self.items[self.rear] = data
    else:
      self.rear += 1
      self.items = data

  def pop(self):
    # check empty
    # single element -> front and rear = -1
    # circular nature
    # normal flow

    if self.is_empty():
      print("Queue is empty")
      return
    elif self.front == self.rear:
      self.items[self.front] = -1
      self.front = -1
      self.rear = -1
    elif self.front == self.size - 1:
      self.front = 0
    else:
      self.front += 1


class DoublyEndedQueue:

  def __init__(self):
    self.deque = deque()

  def is_empty(self):
    return len(self.deque) == 0

  def add_front(self, item):
    self.deque.appendleft(item)

  def add_rear(self, item):
    self.deque.append(item)

  def remove_front(self):
    if not self.is_empty():
      return self.deque.popleft()
    else:
      return None

  def remove_rear(self):
    if not self.is_empty():
      return self.deque.pop()
    else:
      return None

  def peek_front(self):
    if not self.is_empty():
      return self.deque[0]
    else:
      return None

  def peek_rear(self):
    if not self.is_empty():
      return self.deque[-1]
    else:
      return None

  def size(self):
    return len(self.deque)
