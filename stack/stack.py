class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    return "Stack is empty."

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    return "Stack is empty."

  def size(self):
    return len(self.items)

  # Alias for peek
  top = peek


class TwoStackInArray:

  def __init__(self, n):
    self.size = n
    self.arr = [None] * n
    self.top1 = -1
    self.top2 = n

  # Function to push an integer into stack 1
  def push1(self, x):
    if self.top2 - self.top1 > 1:
      self.top1 += 1
      self.arr[self.top1] = x
    else:
      print("Stack Overflow")

  # Function to push an integer into stack 2
  def push2(self, x):
    if self.top2 - self.top1 > 1:
      self.top2 -= 1
      self.arr[self.top2] = x
    else:
      print("Stack Overflow")

  # Function to remove an element from top of stack 1
  def pop1(self):
    if self.top1 >= 0:
      x = self.arr[self.top1]
      self.arr[self.top1] = None
      self.top1 -= 1
      return x
    else:
      print("Stack Underflow")
      return -1

  # Function to remove an element from top of stack 2
  def pop2(self):
    if self.top2 < self.size:
      x = self.arr[self.top2]
      self.arr[self.top2] = None
      self.top2 += 1
      return x
    else:
      print("Stack Underflow")
      return -1

  def printS(self):
    print(self.arr)


class MinStack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, val: int) -> None:
    if self.is_empty():
      tup = (val, val)
      self.items.append(tup)
    else:
      tup = (val, min(val, self.getMin()))
      self.items.append(tup)

  def pop(self) -> None:
    if not self.is_empty():
      temp = self.items.pop()
      return temp[0]
    else:
      return None

  def top(self) -> int:
    if not self.is_empty():
      return self.items[-1][0]
    else:
      return 0

  def getMin(self) -> int:
    if not self.is_empty():
      return self.items[-1][1]
    else:
      return -1

  # Alias for top
  peek = top