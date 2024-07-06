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

  def interleave_first_and_second_half(self):
    """
    Interleave first and second half of a Queue.
    """
    # take first half of Q into a new Queue.
    q = [3, 7, 5, 6, 8, 9]
    N = 6

    if not q:
      return

    mid = N // 2 + 1 if N & 1 else N // 2

    count = 0
    q2 = list()

    while len(q) != 0 and count != mid:
      q2.append(q.pop(0))
      count += 1

    # interleaving
    while len(q) != 0 and len(q2) != 0:
      first = q2.pop(0)
      q.append(first)

      second = q.pop(0)
      q.append(second)

    return q

  def first_neg_integer(self):
    """
    first -ve interger in every window of size k.
    i/p: [12, -1, -7, 8, -15, 30, 16, 28]
    """

    def solve(arr, n, k):
      q = deque()

      result = []
      #  process first window of size k.
      for i in range(k):
        if arr[i] < 0:
          q.append(i)

      # remaining windows to process.
      for i in range(k, n):
        #  previous window ans.
        if len(q) != 0:
          result.append(arr[q[0]])
        else:
          result.append(0)

        # remove out of window elements.
        while len(q) != 0 and i - q[0] >= k:
          q.popleft()

        # check curr element for insertion.
        if arr[i] < 0:
          q.append(i)

      # append result for the last window.
      result.append(arr[q[0]]) if q else result.append(0)

      return result

    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    arr = [-8, 2, 3, -6, 10]
    size = len(arr)

    k = 3
    k = 2

    result = solve(arr, size, k)
    print(result)

  def non_repeated_char_in_stream(self):
    """
    """
