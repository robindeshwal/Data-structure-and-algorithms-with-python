import heapq
import sys
import math


class ListNode:

  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


class Questions:

  def k_smallest(self, arr=[7, 10, 4, 20, 15], k=10):
    """
    GFG: kth smallest number.
    """
    max_heap = []
    for i in range(k):
      heapq.heappush(max_heap, -arr[i])

    for i in range(k, len(arr)):
      heapTop = -max_heap[0]
      if heapTop > arr[i]:
        heapq.heappop(max_heap)
        heapq.heappush(max_heap, -arr[i])
        # heapreplace(max_heap, -arr[i]) also doing the same thing pop and push.

    print(-max_heap[0])
    return -max_heap[0]

  def k_largest(self, nums=[3, 2, 1, 5, 6, 4], k=2):
    """
    215: Leetcode -> Kth Largest Element in an Array
    """
    min_heap = []

    for i in range(k):
      heapq.heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
      heapTop = min_heap[0]
      if heapTop < nums[i]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, nums[i])

    print(min_heap[0])
    return min_heap[0]

  def merge_two_heaps(self):
    """
    HW
    """

  def is_bst_heap(self, root):
    """
    GFG: Is Binary Tree Heap. => Is Complete binary tree is heap or not.
    """

    def solve(root):
      # base case
      if not root:
        return (True, None)

      if not root.left and not root.right:
        return (True, root.data)

      left = solve(root.left)
      right = solve(root.right)

      if (left[0] and right[0] and root.data > left[1]
          and root.data > right[1]):
        return (True, root.data)
      return (False, None)

    ans = solve(root)
    return ans[0]

  def convert_bst_max_heap(self):
    """
    GFG: BST to max heap

    use inorder to store and put into postorder to create heap.
    """

  def is_tree_cbt(self):
    """
    GFG: Is tree complete binary tree or not.
    """

  def merge_k_sorted_array(self, arr, n, K):
    """
    GFG: merge k sorted arrays.
    """

    def solve(arr, n, k):
      # (value, row, col)
      heap = []

      for i in range(k):
        temp = (arr[i][0], i, 0)
        heapq.heappush(heap, temp)

      ans = []

      while heap:
        temp = heapq.heappop(heap)
        topElement = temp[0]
        topRow = temp[1]
        topCol = temp[2]

        ans.append(topElement)

        if topCol + 1 < n:
          newTemp = (arr[topRow][topCol + 1], topRow, topCol + 1)
          heapq.heappush(heap, newTemp)

      return ans

    n = len(arr[0])
    return solve(arr, n, K)

  def merge_k_sorted_linkedList(self, lists):
    """
    23: Leetcode -> Merge k Sorted Lists
    """
    minHeap = []

    k = len(lists)
    if k == 0:
      return None

    for i in range(k):
      if lists[i]:
        heapq.heappush(minHeap, (lists[i].val, i, lists[i]))

    head = ListNode(None)
    tail = head

    while minHeap:
      _, idx, node = heapq.heappop(minHeap)

      tail.next = node
      tail = node

      if node.next:
        heapq.heappush(minHeap, (node.next.val, idx, node.next))

    return head.next

  def smallest_range_in_k_lists(self, nums):
    """
    632: Leetcode -> Smallest Range Covering Elements from K Lists
    """
    mini = sys.maxsize
    maxi = -sys.maxsize - 1

    heap = []
    # data, maxi, mini.

    k = len(nums)

    for i in range(k):
      ele = nums[i][0]
      maxi = max(maxi, ele)
      mini = min(mini, ele)

      temp = (ele, i, 0)
      heapq.heappush(heap, temp)

    ans = [mini, maxi]

    while heap:
      top = heapq.heappop(heap)
      topEle = top[0]
      topRow = top[1]
      topCol = top[2]

      # update mini
      mini = topEle

      if (maxi - mini) < (ans[1] - ans[0]):
        ans = [mini, maxi]

      # check element exist in the list.
      if topCol + 1 < len(nums[topRow]):
        # TODO: don't forget to update the maxi.
        maxi = max(maxi, nums[topRow][topCol + 1])
        newTemp = (nums[topRow][topCol + 1], topRow, topCol + 1)
        heapq.heappush(heap, newTemp)
      else:
        break

    return ans

  def remove_stones(self, piles=[5, 7, 9], k=2):
    """
    1962: Leetcode -> Remove Stones to Minimize the Total
    """
    max_heap = []

    for i in range(len(piles)):
      heapq.heappush(max_heap, -piles[i])

    while k:
      k -= 1
      maxEle = -heapq.heappop(max_heap)
      maxEle = maxEle - math.floor(maxEle // 2)
      heapq.heappush(max_heap, -maxEle)

    # ans = 0
    # while max_heap:
    #     temp = -heapq.heappop(max_heap)
    #     ans += temp

    return -sum(max_heap)

  def reorganize_string(self, s):
    """
    767: Leetcode -> Reorganize String
    """
    dic = {}

    for i in range(len(s)):
      ch = s[i]
      if ch not in dic:
        dic[ch] = 0
      dic[ch] += 1

    max_heap = []

    for key, value in dic.items():
      temp = [-value, key]
      heapq.heappush(max_heap, temp)

    ans = ""

    while len(max_heap) > 1:
      first = heapq.heappop(max_heap)
      second = heapq.heappop(max_heap)

      ans += first[1]
      ans += second[1]

      first[0] += 1
      second[0] += 1

      if first[0] != 0:
        heapq.heappush(max_heap, first)

      if second[0] != 0:
        heapq.heappush(max_heap, second)

    if max_heap:
      temp = heapq.heappop(max_heap)
      if temp[0] == -1:
        ans += temp[1]
      else:
        return ""

    return ans

  def longest_happy_string(self, a, b, c):
    """
    1405: Leetcode -> Longest Happy String.
    """
    max_heap = []

    if a > 0:
      temp = [-a, 'a']
      heapq.heappush(max_heap, temp)
    if b > 0:
      temp = [-b, 'b']
      heapq.heappush(max_heap, temp)
    if c > 0:
      temp = [-c, 'c']
      heapq.heappush(max_heap, temp)

    ans = ""

    while len(max_heap) > 1:
      first = heapq.heappop(max_heap)
      second = heapq.heappop(max_heap)

      if -first[0] >= 2:
        ans += first[1]
        ans += first[1]
        first[0] += 2
      else:
        ans += first[1]
        first[0] += 1

      # NOTE: this is a catch here, second will be used 2 times only when its count greater then first. otherwise some of ch from first will not be used to create string.
      if -second[0] >= 2 and -second[0] >= -first[0]:  # IMPORTANT condition.
        ans += second[1]
        ans += second[1]
        second[0] += 2
      else:
        ans += second[1]
        second[0] += 1

      if -first[0] > 0:
        heapq.heappush(max_heap, first)

      if -second[0] > 0:
        heapq.heappush(max_heap, second)

    if len(max_heap) == 1:
      temp = heapq.heappop(max_heap)

      if -temp[0] >= 2:
        ans += temp[1]
        ans += temp[1]
        temp[0] += 2
      else:
        ans += temp[1]
        temp[0] += 1

    return ans

  def median_in_stream(self):
    """
    295: Leetcode -> Find Median from Data Stream
    """
