import heapq


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

  def k_largest(self, nums=[3,2,1,5,6,4], k=2):
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

  def is_bst_heap(self):
    """
    GFG: Is Complete binary tree is heap or not.
    """