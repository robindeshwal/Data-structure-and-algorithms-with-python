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

  def merge_sort(self):
    """
    """

  def quick_sort(self):
    """
    """
