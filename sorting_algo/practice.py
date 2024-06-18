class Sorting:

  def __init__(self) -> None:
    pass

  def selection_sort(self):
    """
    """
    arr = [10, 4, 1, 5, 8, 7]

    def sort(arr):

      for idx in range(len(arr) - 1):
        min = idx
        for j in range(idx + 1, len(arr)):
          if arr[j] < arr[min]:
            min = j

        if arr[idx] > arr[min]:
          arr[idx], arr[min] = arr[min], arr[idx]
      return arr

    print(sort(arr))

  def bubble_sort(self):
    """
    """
    arr = [10, 1, 7, 6, 14, 9]
    for i in range(1, len(arr)):
      for j in range(len(arr) - i):
        if arr[j] > arr[j + 1]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

  def insertion_sort(self):
    """
    """
    arr = [10, 1, 7, 6, 14, 9]
    for i in range(1, len(arr)):
      val = arr[i]
      j = i - 1
      while j >= 0:
        if arr[j] > val:
          arr[j + 1] = arr[j]
        else:
          break
        j -= 1

      arr[j + 1] = val
    print(arr)

  def merge_2_sorted_array(self, arr, s, e):
    """
    """
    mid = s + (e - s) // 2

    len1 = mid - s + 1
    len2 = e - mid

    left = list(range(len1))
    right = list(range(len2))

    k = s
    for i in range(len1):
      left[i] = arr[k]
      k += 1

    k = mid + 1
    for i in range(len2):
      right[i] = arr[k]
      k += 1

    # Merge
    leftIndex = 0
    rightIndex = 0
    mainArrayIndex = s

    while (leftIndex < len1 and rightIndex < len2):
      if left[leftIndex] < right[rightIndex]:
        arr[mainArrayIndex] = left[leftIndex]
        mainArrayIndex += 1
        leftIndex += 1
      else:
        arr[mainArrayIndex] = right[rightIndex]
        mainArrayIndex += 1
        rightIndex += 1

    while (leftIndex < len1):
      arr[mainArrayIndex] = left[leftIndex]
      mainArrayIndex += 1
      leftIndex += 1

    while (rightIndex < len2):
      arr[mainArrayIndex] = right[rightIndex]
      mainArrayIndex += 1
      rightIndex += 1

    return arr

  def merge_sort(self):
    """
    Merge sort using recursion:
    arr = [7, 3, 2, 16, 24, 4 , 11, 9]

    Time complixity: O(nlogn)
    """

    def solve(arr, s, e):
      # base case
      if s >= e:
        return

      mid = s + (e - s) // 2
      # left part
      solve(arr, s, mid)

      # right part
      solve(arr, mid + 1, e)

      self.merge_2_sorted_array(arr, s, e)

    arr = [7, 3, 2, 16, 24, 4, 11, 9]
    s = 0
    e = len(arr) - 1
    solve(arr, s, e)
    print(arr)

  def quick_sort(self):
    """
    arr = [8, 3, 4, 1, 20, 50, 30]

    time complexity: O(nlogn)
    waste case TC : O(n2)
    """

    def partition(arr, s, e):
      pivotElement = arr[s]

      # find right position for pivot element and place it.
      count = 0
      for i in range(s + 1, e + 1):
        if arr[i] <= pivotElement:
          count += 1

      # ready pivot right place
      pivotIndex = s + count
      arr[s], arr[pivotIndex] = arr[pivotIndex], arr[s]

      # left me chote right me bade
      i = s
      j = e

      while i < pivotIndex and j > pivotIndex:
        while i < pivotIndex and arr[i] <= pivotElement:
          i += 1
        while j > pivotIndex and arr[j] > pivotElement:
          j -= 1

        # if you found the elements to swap
        # no need to swap
        if i < pivotIndex and j > pivotIndex:
          arr[i], arr[j] = arr[j], arr[i]

      return pivotIndex

    def solve(arr, s, e):
      # base case
      if s >= e:
        return

      # partition logic
      p = partition(arr, s, e)

      # recussion
      # left
      solve(arr, s, p - 1)

      # right
      solve(arr, p + 1, e)

    arr = [
        8, 3, 4, 1, 1, 1, 1, 1, -20, -4, 1, 20, 20, 20, 20, -2, -5, 20, 50, 30
    ]
    s = 0
    e = len(arr) - 1
    solve(arr, s, e)
    print(arr)
