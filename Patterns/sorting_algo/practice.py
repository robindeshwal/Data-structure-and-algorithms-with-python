class Sorting:

  def __init__(self) -> None:
    pass

  def selection_sort(self):
    """
    """
    arr = [10, 4, 1, 5, 8, 7]

    def sort(arr):

      for idx in range(len(arr)):
        min = 2**31
        min_idx = 0
        for j in range(idx, len(arr)):
          if arr[j] < min:
            min = arr[j]
            min_idx = j

        if min < arr[idx]:
          min, arr[idx] = arr[idx], min

      return arr

    print(sort(arr))
