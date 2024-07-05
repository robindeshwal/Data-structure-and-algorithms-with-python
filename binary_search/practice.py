class BinarySearch:

  def __init__(self) -> None:
    pass

  def binary_search_algo(self, arr=[2, 4, 6, 8, 10, 12, 16], target=10):
    """
    """
    start = 0
    end = len(arr) - 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4

    def binary_search(arr, target, start, end):
      while (start <= end):
        mid = end - (end - start) // 2
        if arr[mid] > target:
          end = mid - 1
        elif arr[mid] < target:
          start = mid + 1
        else:
          return mid
      return -1

    def binary_search_new(arr, target, start, end):
      start = 0
      end = len(arr) - 1

      while (start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == target:
          return mid
        elif arr[mid] > target:
          end = mid - 1
        else:
          start = mid - 1
      return -1

    def pivot(arr, start, end):
      """
      [4, 5, 6, 7, 1, 2]
      pivot: (3, 7)
      """
      
