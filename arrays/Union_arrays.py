class UnionArray:

  def __init__(self) -> None:
    pass

  def union_2_arrays(self, arr):
    l1 = [1, 2, 4, 5, 7]
    l2 = [3, 6, 8]
    result = []
    for i in range(0, len(l1)):
      result.append(l1[i])

    for j in range(0, len(l2)):
      result.append(l2[j])

    print(result)

  def intersection_2_arrays(self):
    l1 = [1, 2, 3, 3, 3, 4, 6, 8]
    l2 = [3, 3, 4, 9, 10]
    result = []

    for i in range(len(l1)):
      for j in range(len(l2)):
        if l1[i] == l2[j]:
          l2[j] = -1
          result.append(l1[i])
          break
    print(result)

  def union_without_duplicate(self):
    pass

  def pair_sum(self):
    arr = [1, 3, 5, 7]
    sum = 8

    for i in range(len(arr)):
      element = arr[i]
      for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == sum:
          print(f'{arr[i], arr[j]}')

  def triplet_sum(self):
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    sum = 9

    for i in range(len(arr)):
      x = arr[i]
      for j in range(i + 1, len(arr)):
        y = arr[i]
        for k in range(j + 1, len(arr)):
          if arr[i] + arr[j] + arr[k] == sum:
            print(f'{arr[i], arr[j], arr[k]}')

  def sort_zeros_and_ones(self):
    arr = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]
    arr = [1, 0, 1, 0, 0,0,0,0,0,0]

    start = 0
    end = len(arr) - 1

    while start < end:
      if arr[start] == 0:
        start += 1

      if arr[start] == 1:
        # swap from right
        arr[start], arr[end] = arr[end], arr[start]
        end -= 1

    print(arr)
