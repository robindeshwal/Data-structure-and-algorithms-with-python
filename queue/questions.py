from collections import deque
from queue.queue import MyQueueUsingStack, MyStackUsingQueue, NQueuesInArray


class Questions:

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
    # arr = [-8, 2, 3, -6, 10]
    size = len(arr)

    k = 3
    # k = 2

    result = solve(arr, size, k)
    print(result)

  def non_repeated_char_in_stream(self):
    """
    GFG: first non-repeating char in a stream
    """
    # Code here
    A = "aabc"
    count = [0] * 26
    q = deque()

    ans = ""

    for i in range(len(A)):
      ch = A[i]
      count[ord(ch) - ord('a')] += 1
      q.append(ch)
      while q:
        if count[ord(q[0]) - ord('a')] > 1:
          q.popleft()
        else:
          ans += q[0]
          break
      if not q:
        ans += '#'
    return ans

  def gas_station(self):
    """
    V. IMP
    134 : Gas Station
    """
    gas = [4, 6, 3, 4, 8]
    cost = [3, 6, 7, 1, 3]

    deficit = 0  # kitna petrol kaam pad gya.
    balance = 0  # kitna petrol extra hai.
    start = 0  # circle start

    for i in range(len(gas)):
      balance += gas[i] - cost[i]

      if balance < 0:
        deficit += balance  # yaha pe galti hui hai
        start = i + 1
        balance = 0

    if deficit + balance >= 0:
      return start
    return -1

  def sliding_window_maximum(self):
    """
    239: Leetcode -> sliding window maximum.
    """
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    # code here
    q = deque()
    ans = []

    # First window.
    for i in range(k):
      while q and nums[i] >= nums[q[-1]]:
        q.pop()

      q.append(i)  # inserting index, we can checkout of window element.

    # store answer for first window.
    ans.append(nums[q[0]])

    # process remaining process.
    for i in range(k, len(nums)):
      # out of window element ko remove.
      if q and i - q[0] >= k:
        q.popleft()

      # remove small elements.
      while q and nums[i] >= nums[q[-1]]:
        q.pop()

      q.append(i)

      # current window store.
      ans.append(nums[q[0]])

    return ans

  def queue_using_stack(self):
    """
    232: Leetcode -> Implement queue using stack.
    """
    queue = MyQueueUsingStack()

  def stack_using_queue(self):
    """
    225: Leetcode -> Implement stack using queue.
    """
    stack = MyStackUsingQueue()

  def sum_min_max_subarray(self):
    """
    GFG : Sum of min and max element of all subarray of size k.
    """
    nums = [2, 5, -1, 7, -3, -1, -2]
    k = 4

    q = deque()
    q2 = deque()
    ans = 0

    # First window.
    for i in range(k):
      while q and nums[i] >= nums[q[-1]]:
        q.pop()

      # remove big element
      while q2 and nums[i] <= nums[q2[-1]]:
        q2.pop()

      q.append(i)  # inserting index, we can checkout of window element.
      q2.append(i)

    # store answer for first window.
    ans += nums[q[0]] + nums[q2[0]]

    # process remaining process.
    for i in range(k, len(nums)):
      # out of window element ko remove.
      if q and i - q[0] >= k:
        q.popleft()

      if q2 and i - q2[0] >= k:
        q2.popleft()

      # remove small elements.
      while q and nums[i] >= nums[q[-1]]:
        q.pop()

      while q2 and nums[i] <= nums[q2[-1]]:
        q2.pop()

      q.append(i)
      q2.append(i)

      # current window store.
      ans += nums[q[0]] + nums[q2[0]]

    print(ans)
    return ans

  def k_queues(self):
    ""
    nQueues = NQueuesInArray(6, 2)

    print(nQueues.push(5, 1))
    print(nQueues.push(6, 2))
    print(nQueues.push(7, 1))
    print(nQueues.push(8, 1))
    print(nQueues.push(9, 2))
    print(nQueues.push(10, 1))
    print(nQueues.push(11, 1))

    print(nQueues.pop(1))
    print(nQueues.pop(2))
