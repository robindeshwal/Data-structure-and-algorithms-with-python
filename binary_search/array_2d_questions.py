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

  def k_closest_element(self):
    """
    find 'k' closest element to a given value in an array.
    """

  def exponential_search(self):
    """
    exponential search.
    """

  def unbounded_bs(self):
    """
    Unbounded binary search.
    """

  # Advance binary search
  def book_allocation(self):
    """
    book allocation.
    """

  def painter_partition(self):
    """
    painter partition.
    """

  def aggression_cows(self):
    """
    """

  def roti_spoj(self):
    """
    """

  def eko_spoj(self):
    """
    """