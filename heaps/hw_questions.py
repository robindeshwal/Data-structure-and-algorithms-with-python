import heapq
import sys


class Questions:

  def merge_two_heaps(self, a, b, n, m):
    """
    GFG: Merge two binary Max heaps
    """

    def heapify(arr, i, n):
      while True:
        left = 2 * i + 1
        right = 2 * i + 2
        index = i
        if left < n and arr[left] > arr[i]:
          index = left

        if right < n and arr[right] > arr[index]:
          index = right

        if index == i:
          break
        arr[i], arr[index] = arr[index], arr[i]
        i = index

    # code here

    result = a + b
    combined_length = n + m

    # lets heapify result.
    for i in range(combined_length // 2 - 1, -1, -1):
      heapify(result, i, combined_length)

    return result

  def is_bst_heap(self, root):
    """
    GFG: Is Binary Tree Heap. => Is binary tree is heap or not.
    """

    def node_count(root):
      if not root:
        return 0

      l = node_count(root.left)
      r = node_count(root.right)

      return l + r + 1

    def isCBT(root, i, n):
      if not root:
        return True

      if i > n:
        return False

      return isCBT(root.left, 2 * i, n) and isCBT(root.right, 2 * i + 1, n)

    def isMaxOrder(root):
      if not root:
        return True

      left = isMaxOrder(root.left)
      right = isMaxOrder(root.right)
      ans = False
      if not root.left and not root.right:
        ans = True
      elif root.left and not root.right:
        ans = root.data > root.left.data
      else:
        ans = root.data > root.left.data and root.data > root.right.data
      return ans and left and right

    n = node_count(root)
    i = 1
    if not isCBT(root, 1, n):
      return False

    return isMaxOrder(root)

  def k_closest_points(self, points=[[1, 3], [-2, 2]], k=1):
    """
    973: Leetcode -> K Closest Points to Origin.
    """
    min_heap = []

    for i in range(len(points)):
      x = points[i][0]
      y = points[i][1]

      d = x**2 + y**2
      heapq.heappush(min_heap, (d, points[i]))

    ans = []
    for i in range(k):
      temp = heapq.heappop(min_heap)
      ans.append(temp[1])

    return ans

  def sliding_window_max(self, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3):
    """
    239: Leetcode -> Sliding Window Maximum
    """
    max_heap = []
    ans = []

    for i in range(k):
      # pair (val, index)
      pair = (-nums[i], i)
      heapq.heappush(max_heap, pair)

    ans.append(-max_heap[0][0])

    for i in range(k, len(nums)):
      pair = (-nums[i], i)
      heapq.heappush(max_heap, pair)

      #  remove if max are from previous window.
      while max_heap[0][1] <= i - k:
        heapq.heappop(max_heap)

      ans.append(-max_heap[0][0])

    return ans

  def biggest_three_rhombus(self, grid):
    """
    1878: Leetcode -> Get Biggest Three Rhombus Sums in a Grid.
    """

    def checkBounds(grid, temp):
      m = len(grid)
      n = len(grid[0])
      for i in range(len(temp)):
        if temp[i][0] < 0 or temp[i][0] >= m or temp[i][1] < 0 or temp[i][
            1] >= n:
          return False

      return True

    def getAllVertices(grid, temp, c, delta):
      aP = (c[0] - delta, c[1])
      bP = (c[0], c[1] + delta)
      cP = (c[0] + delta, c[1])
      dP = (c[0], c[1] - delta)

      temp.append(aP)
      temp.append(bP)
      temp.append(cP)
      temp.append(dP)

      if checkBounds(grid, temp):
        return True
      return False

    def getAllSum(grid, cx, cy, mh):
      # push rh sum of rh with area 0
      heapq.heappush(mh, -grid[cx][cy])
      delta = 1

      while getAllVertices(grid, [], (cx, cy), delta):
        a = (cx - delta, cy)
        b = (cx, cy + delta)
        c = (cx + delta, cy)
        d = (cx, cy - delta)

        cSum = grid[a[0]][a[1]] + grid[b[0]][b[1]] + grid[c[0]][c[1]] + grid[
            d[0]][d[1]]

        for i in range(1, delta):
          # all cells between a and b.
          cSum += grid[a[0] + i][a[1] + i]

          # all cells between b and c.
          cSum += grid[b[0] + i][b[1] - i]

          # all cells between c and d.
          cSum += grid[c[0] - i][c[1] - i]

          # all cells between d and a.
          cSum += grid[d[0] - i][d[1] + i]

        heapq.heappush(mh, -cSum)
        delta += 1

    ans = []
    max_heap = []
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
      for j in range(n):
        getAllSum(grid, i, j, max_heap)

    ans = []
    while max_heap and len(ans) < 3:
      top = -heapq.heappop(max_heap)
      if top not in ans:
        ans.append(top)

    return ans

  def min_diff_sum(self, nums):
    """
    2163: Leetcode -> Minimum Difference in Sums After Removal of Elements
    """
    length = len(nums)

    n = length // 3
    prefix = [-1
              ] * length  # prefix[i] = sum of first n elements from left side.
    suffix = [-1
              ] * length  # suffix[i] = sum of first n element from right side.

    SUM = 0
    max_heap = []  # for prefix
    for i in range(length):
      SUM += nums[i]

      heapq.heappush(max_heap, -nums[i])

      # pop max elements.
      if len(max_heap) > n:
        SUM -= -heapq.heappop(max_heap)

      if len(max_heap) == n:
        prefix[i] = SUM

    SUM = 0
    min_heap = []  # for suffix
    for i in range(length - 1, -1, -1):
      SUM += nums[i]

      heapq.heappush(min_heap, nums[i])

      # pop min elements.
      if len(min_heap) > n:
        SUM -= heapq.heappop(min_heap)

      if len(min_heap) == n:
        suffix[i] = SUM

    ans = sys.maxsize
    for i in range(n - 1, 2 * n):
      ans = min(ans, prefix[i] - suffix[i + 1])

    return ans

  def min_number_refueling_stops(self, target, startFuel, stations):
    """
    871: Leetcode -> Minimum Number of Refueling Stops
    """
    stops = 0
    dist = 0
    i = 0
    fuel = startFuel
    max_heap = []  # pair for fuel and position

    while True:
      while i < len(stations):
        # push stations within the reach with my current fuel levels from my current pos.
        if stations[i][0] <= dist + fuel:
          heapq.heappush(max_heap, (-stations[i][1], stations[i][0]))
        else:
          break
        i += 1

      # travel with full fuel level.
      dist += fuel
      fuel = 0

      # reached
      if dist >= target:
        break

      # no fuel stations found.
      if not max_heap:
        stops = -1
        break

      # refuel and re-adjust dist and fuel based on the distance travelled and fuel used till that station.
      top = heapq.heappop(max_heap)
      fuel = (dist - top[1]) + (-top[0])
      dist = top[1]
      stops += 1

    return stops
