from lib.decorator import print_before


class TwoPointers:

  def __init__(self) -> None:
    print('==== Two Pointers ====')

  def extreme_print(self, arr) -> None:
    start = 0
    end = len(arr) - 1

    while start <= end:
      if start == end:
        print(arr[start])
      else:
        print(arr[start])
        print(arr[end])

      start += 1
      end -= 1

  def reverse_array(self, arr):
    start = 0
    end = len(arr) - 1

    while start < end:
      # swap
      # temp = arr[start]
      # arr[start] = arr[end]
      # arr[end] = temp

      arr[start], arr[end] = arr[end], arr[start]

      start += 1
      end -= 1
    print(arr, end="")
