class BinarySearch:

  def __init__(self) -> None:
    pass

  def binary_search_algo(self):
    """
    """
    arr = [2, 4, 6, 8, 10, 12, 16]
    target = 10

    start = 0
    end = len(arr) - 1
    result = -1

    count = 0
    while (start <= end):
      count += 1
      mid = end - (end - start) // 2
      if arr[mid] > target:
        end = mid - 1
      elif arr[mid] < target:
        start = mid + 1
      else:
        result = mid
        break
    print(result)
    return result
