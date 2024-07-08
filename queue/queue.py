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


class MyQueueUsingStack:

  def __init__(self):
    self.s1 = list()
    self.s2 = list()

  def push(self, x: int) -> None:
    self.s1.append(x)

  def pop(self) -> int:
    pop = -1
    if self.s2:
      pop = self.s2.pop()
    else:
      while self.s1:
        self.s2.append(self.s1.pop())
      pop = self.s2.pop()
    return pop

  def peek(self) -> int:
    peek = -1
    if self.s2:
      peek = self.s2[-1]
    else:
      while self.s1:
        self.s2.append(self.s1.pop())
      peek = self.s2[-1]
    return peek

  def empty(self) -> bool:
    return len(self.s1) == 0 and len(self.s2) == 0


class MyStackUsingQueue:

  def __init__(self):
    self.q = deque()

  def push(self, x: int) -> None:
    self.q.append(x)
    for i in range(len(self.q) - 1):
      temp = self.q.popleft()
      self.q.append(temp)

  def pop(self) -> int:
    if self.q:
      return self.q.popleft()
    else:
      return -1

  def top(self) -> int:
    if self.q:
      return self.q[0]
    else:
      return -1

  def empty(self) -> bool:
    return len(self.q) == 0


class NQueuesInArray:

  def __init__(self, size, k):
    self.size = size
    self.k = k
    self.freespot = 0
    self.arr = [None] * size
    self.front = [-1] * k
    self.rear = [-1] * k
    self.next = [i + 1 if i != size - 1 else -1 for i in range(size)]
    self.count = 0

  def push(self, x, qi):
    """
    x = value
    qi = which queue (1-indexed)
    """
    # Convert 1-indexed qi to 0-indexed
    qi -= 1

    if qi < 0 or qi >= self.k:
      raise IndexError("Queue index out of range")

    # overflow
    if self.freespot == -1 or self.count == self.size:
      return False

    # find first free index.
    index = self.freespot

    # update freespot
    self.freespot = self.next[index]

    # if first element in qi
    if self.front[qi] == -1:
      self.front[qi] = index
    else:
      # link new element to that Q's rearest element.
      self.next[self.rear[qi]] = index

    # update next
    self.next[index] = -1

    # update rear
    self.rear[qi] = index
    self.arr[index] = x

    self.count += 1

    return True

  def pop(self, qi):
    """
    qi = pop from which queue. (1-indexed)
    """
    # Convert 1-indexed qi to 0-indexed
    qi -= 1

    if qi < 0 or qi >= self.k:
      raise IndexError("Queue index out of range")

    # underflow
    if self.front[qi] == -1:
      return -1

    # find index to pop
    index = self.front[qi]

    # update front
    self.front[qi] = self.next[index]

    # update freespots
    self.next[index] = self.freespot
    self.freespot = index

    self.count -= 1

    return self.arr[index]
