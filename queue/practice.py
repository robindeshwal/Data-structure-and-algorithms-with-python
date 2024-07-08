from queue.queue import Queue
from collections import deque


class Practice:

  def __init__(self):
    self.queue = Queue()

  def reverse_queue(self):
    """
    i/p : [3,6,9,2,8]
    o/p: [8,2,9,6,3]

    Approch1: using stack
    Approch2: using recursion.
    """

    def using_stack(queue):
      stack = list()

      while not queue.is_empty():
        element = queue.pop()
        stack.append(element)

      while len(stack) != 0:
        element = stack.pop()
        queue.push(element)

    def using_recursion(queue):
      if queue.is_empty():
        return

      temp = queue.pop()
      using_recursion(queue)

      queue.push(temp)

    self.queue.push(3)
    self.queue.push(6)
    self.queue.push(9)
    self.queue.push(2)
    self.queue.push(8)

    print(self.queue.items)
    # using_stack(self.queue)
    using_recursion(self.queue)
    print(self.queue.items)

  def reverse_first_k_elements(self):
    """
    Reverse first of elements of queue.
    i/p : [3, 6, 9, 12, 15]
    o/p : [9, 6, 3, 12, 15]
    """

    def solve(queue, k):
      #  queue k elements -> stack
      stack = list()
      count = 0
      n = queue.length()

      if k == 0 or k > n:
        return

      while not queue.is_empty():
        temp = queue.pop()
        stack.append(temp)
        count += 1
        if count == k:
          break

      while len(stack) != 0:
        temp = stack.pop()
        queue.push(temp)

      count = 0
      while not queue.is_empty() and n - k != 0:
        temp = queue.pop()
        queue.push(temp)
        count += 1

        if count == n - k:
          break

    self.queue.push(3)
    self.queue.push(6)
    self.queue.push(9)
    self.queue.push(12)
    self.queue.push(15)

    k = 5
    print(self.queue.items)
    solve(self.queue, k)
    print(self.queue.items)