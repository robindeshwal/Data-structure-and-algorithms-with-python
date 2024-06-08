class Questions:

  def __init__(self) -> None:
    "binary search on 2D array."
    pass

  def binary_search_2d(self, arr, target):
    """
    """
    start = 0
    length = len(arr) * len(arr[0])
    end = length - 1

    while (start <= end):
      mid = start + (end - start) // 2
      rowIndex = mid // len(arr[0])
      colIndex = mid % len(arr[0])
      element = arr[rowIndex][colIndex]

      if element > target:
        end = mid - 1
      elif element < target:
        start = mid + 1
      else:
        return rowIndex, colIndex
    return -1, -1

  def practice(self):
    """
    Search in 2D array using binary search.
    """
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],
           [17, 18, 19, 20]]

    target = 20

    result = self.binary_search_2d(arr, target)
    print(result)

  def search_nearly_sorted(self):
    """
    search in a nearly sorted array in log time
    """
    arr = [10, 3, 40, 20, 50, 80, 70]
    target = 70

    def search(arr, target):
      start = 0
      end = len(arr) - 1

      while (start < end):
        mid = start + (end - start) // 2

        if arr[mid] == target:
          return mid
        if mid - 1 >= 0 and arr[mid - 1] == target:
          return mid - 1
        if mid + 1 < len(arr) and arr[mid + 1] == target:
          return mid + 1

        if target > arr[mid]:
          start = mid + 2
        else:
          end = mid - 2

      return -1

    print(search(arr, target))

  def division_two_numbers(self):
    """
    Division of 2 numbers using binary search.
    divident = 10
    divisor = 2
    quocent = ?
    """
    dividend = 21
    divisor = 7

    def solve(dividend, divisor):
      start = 0
      end = abs(dividend)
      ans = 0
      while (start <= end):
        mid = start + (end - start) // 2
        if abs(mid * divisor) == abs(dividend):
          ans = mid
          break

        if abs(mid * divisor) > abs(dividend):
          end = mid - 1
        else:
          ans = mid
          start = mid + 1

      if (divisor < 0 and dividend < 0) or (divisor > 0 and dividend > 0):
        ans = ans
      else:
        ans = ans * -1
      return ans

    ans = solve(dividend, divisor)
    """ and .00 value for exact quocent value. """
    precedence = 3
    for i in range(3):
      # while(ans+)
      pass

  def find_odd_occuring(self):
    """
    find the odd occuring element using binary search.
    """
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 3, 600, 600, 4, 4]
    arr = [4, 4, 3, 3, 5, 5, 2, 2, 5]
    arr = [5, 5, 2]

    def my_solution(arr):
      start = 0
      end = len(arr) - 1

      while (start < end):
        mid = start + (end - start) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
          print(mid, arr[mid])
          return mid
        if mid % 2 == 0 and arr[mid] == arr[mid + 1]:
          start = mid + 2
        else:
          end = mid

      return -1

    def solution(arr):
      start = 0
      end = len(arr) - 1

      while (start <= end):
        mid = start + (end - start) // 2
        if start == end:
          return start, arr[start]

        if (mid % 2 == 0):
          if arr[mid] == arr[mid + 1]:
            start = mid + 2
          else:
            end = mid
        else:
          if arr[mid] == arr[mid - 1]:
            start = mid + 1
          else:
            end = mid - 1

    print(solution(arr))

  def pairs_with_difference(self):
    """
    find pairs with difference 'k' in an array.
    """
    arr = [3, 1, 4, 1, 5]
    k = 2

    def bs(arr, s, target):
      e = len(arr) - 1
      while (s <= e):
        mid = s + (e - s) // 2
        if arr[mid] == target:
          return target
        elif arr[mid] < target:
          s = mid + 1
        else:
          e = mid - 1
      return None

    length = len(arr)

    ans = set()
    arr.sort()

    for i in range(length):
      target = arr[i] + k
      if bs(arr, i + 1, target) is not None:
        ans.add((arr[i], target))
    return len(ans)

  def k_closest_element(self):
    """
    find 'k' closest element to a given value in an array.
    """

    def two_pointer_method(arr, k, x):
      l = 0
      h = len(arr) - 1

      while (h - l >= k):
        if abs(x - arr[l]) > abs(arr[h] - x):
          l += 1
        else:
          h -= 1

      return arr[l:h + 1]

    def bs_lower_bound(arr, x):
      s = 0
      e = len(arr) - 1
      ans = e
      while (s <= e):
        m = s + (e - s) // 2
        if arr[m] >= x:
          ans = m
          e = m - 1
        else:
          s = m + 1

      return ans

    def bs_method(arr, k, x):
      h = self.bs_lower_bound(arr, x)
      l = h - 1

      while k:
        k -= 1
        if l < 0:
          h += 1
        elif h >= len(arr):
          l -= 1
        elif abs(x - arr[l]) > abs(arr[h] - x):
          h += 1
        else:
          l -= 1
      return arr[l + 1:h]

  def exponential_search(self):
    """
    exponential search.
    """
    arr = [3, 4, 5, 6, 11, 13, 14, 15, 56, 70]
    x = 3

    def bs(arr, s, e, x):
      while (s <= e):
        mid = s + (e - s) // 2
        if arr[mid] == x:
          return mid
        elif arr[mid] > x:
          e = mid - 1
        else:
          s = mid + 1
      return -1

    def expSearch(arr, x):
      if arr[0] == x:
        return 0
      i = 1
      while i < len(arr) and arr[i] <= x:
        i *= 2

      return bs(arr, i // 2, min(i, len(arr) - 1), x)

    print(expSearch(arr, x))

  def unbounded_bs(self):
    """
    Unbounded binary search.
    arr = [1,3,5, 7, 9, 10 ....]
    """

  # Advance binary search
  def book_allocation(self):
    """
    book allocation.
    """
    arr = [12, 34, 67, 90]
    n = 4
    m = 2

    def possible_solution(arr, n, m, mid):
      pageSum = 0
      count = 1
      for i in range(n):
        if arr[i] > mid:
          return False
        if pageSum + arr[i] > mid:
          count += 1
          pageSum = arr[i]
          if count > m:
            return False
        else:
          pageSum += arr[i]
      return True

    def bs(arr, s, e):
      ans = -1
      while (s <= e):
        mid = s + (e - s) // 2
        if possible_solution(arr, n, m, mid):
          ans = mid
          e = mid - 1
        else:
          s = mid + 1
      return ans

    if m > n:
      return -1

    s = 0
    e = sum(arr)
    return bs(arr, s, e)

  def painter_partition(self):
    """
    painter partition.
    """

  def aggression_cows(self):
    """
    """
    arr = []
    n = len(arr)
    k = 3

    def possible(arr, n, k, mid):
      # can we place k cows with at least mid distance between cows.
      count = 1
      pos = arr[0]
      for i in range(1, n):
        if arr[i] - pos >= mid:
          count += 1
          pos = arr[i]
        if count == k:
          return True
      return False

    def bs(arr, s, e):
      ans = -1
      while (s <= e):
        mid = s + (e - s) // 2
        if possible(arr, n, k, mid):
          ans = mid
          s = mid + 1
        else:
          e = mid - 1

      return ans

    arr.sort()

    s = 0
    e = arr[n - 1] - arr[0]

    return bs(arr, s, e)

  def tree_cutting_spoj(self):
    """
    EKO SPOJ QUESTION:
    
    Mirko needs to chop down M metres of wood. It is an easy job for him since he has a 
    nifty new woodcutting machine that can take down forests like wildfire. However, 
    Mirko is only allowed to cut a single row of trees.

    Input:
    4 7
    20 15 10 17

    Output:
    15
    """
    arr = [20, 15, 10, 17]
    n = 4
    m = 7

    def possible(arr, n, m, mid):
      wood = 0
      for i in range(n):
        if arr[i] > mid:
          wood += arr[i] - mid
      return wood >= m

    def bs(arr, s, e):
      ans = -1
      while (s <= e):
        mid = s + (e - s) // 2
        if possible(arr, n, m, mid):
          ans = mid
          s = mid + 1
        else:
          e = mid - 1
      return ans

    s = 0
    e = max(arr)

    return bs(arr, s, e)

  def prata_spoj(self):
    """
    """
    arr = [1, 2, 3, 4]
    P = 10
    C = 4

    def possible(arr, P, C, mid):
      totalParata = 0
      for i in range(C):
        rank = arr[i]
        j = 1
        timeTaken = 0
        while (True):
          if timeTaken + j * R <= mid:
            totalParata += 1
            timeTaken += j * R
            j += 1
          else:
            break
      if totalParata >= P:
        return True
      return False

    def bs(arr, s, e):
      ans = -1
      while (s <= e):
        mid = s + (e - s) // 2
        if possible(arr, P, C, mid):
          ans = mid
          e = mid - 1
        else:
          s = mid + 1
      return ans

    s = 0
    max_effecient = max(arr)
    e = max_effecient * (C * (C - 1) // 2)
    return bs(arr, s, e)
