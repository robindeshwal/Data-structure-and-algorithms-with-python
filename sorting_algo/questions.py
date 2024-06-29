class Questions:

  def merge_sort(self):
    """"""

    def merge(temp, s, mid, e):
      i = s
      j = mid + 1
      k = s
      while i <= mid and j <= e:
        if arr[i] <= arr[j]:
          temp[k] = arr[i]
          i += 1
        else:
          temp[k] = arr[j]
          j += 1
        k += 1

      while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

      while j <= e:
        temp[k] = arr[j]
        k += 1
        j += 1

      while s <= e:
        arr[s] = temp[s]
        s += 1

    def merge_sort(temp, s, e):
      if s >= e:
        return 0
      mid = s + (e - s) // 2

      merge_sort(temp, s, mid)
      merge_sort(temp, mid + 1, e)

      merge(temp, s, mid, e)

    arr = [2, 4, 1, 3, 5]
    temp = list(0 for _ in range(len(arr)))

    start = 0
    end = len(arr) - 1
    merge_sort(temp, start, end)
    print(arr)

  def count_inversions(self):
    """
    Given an array of integers. Find the Inversion Count in the array. 
    Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
    Input: n = 5, arr[] = {2, 4, 1, 3, 5}
    Output: 3
    Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
    """

    def merge(temp, s, mid, e):
      i = s
      j = mid + 1
      k = s
      c = 0
      while i <= mid and j <= e:
        if arr[i] <= arr[j]:
          temp[k] = arr[i]
          i += 1
        else:
          temp[k] = arr[j]
          j += 1
          c += mid - i + 1
        k += 1

      while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

      while j <= e:
        temp[k] = arr[j]
        k += 1
        j += 1

      while s <= e:
        arr[s] = temp[s]
        s += 1

      return c

    def merge_sort(temp, s, e):
      if s >= e:
        return 0
      mid = s + (e - s) // 2

      c = 0
      c += merge_sort(temp, s, mid)
      c += merge_sort(temp, mid + 1, e)

      c += merge(temp, s, mid, e)

      return c

    arr = [5, 3, 2, 4, 1]
    count = 0
    temp = list(0 for _ in range(len(arr)))

    start = 0
    end = len(arr) - 1
    count = merge_sort(temp, start, end)
    return count

  def in_place_merge_sort(self):
    """
    method 1: 
    method 2: Gap method
    gap = math.ceil((n+m)//2)
    or
    gap = (total//2) + (total%2)
    """

    def merge_in_place(start, mid, end):
      total_length = end - start + 1
      gap = total_length // 2 + total_length % 2

      while gap > 0:
        i = start
        j = start + gap
        while j <= end:
          if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

          i += 1
          j += 1

        gap = 0 if gap <= 1 else (gap // 2 + gap % 2)

    def merge_sort(s, e):
      if s >= e:
        return 0
      mid = s + (e - s) // 2

      merge_sort(s, mid)
      merge_sort(mid + 1, e)

      merge_in_place(s, mid, e)

    arr = [2, 4, 1, 3, 5]

    start = 0
    end = len(arr) - 1
    merge_sort(start, end)
    print(arr)

  def quick_sort_better(self):
    """
    arr = [7, 2, 1, 8, 6, 3, 5, 4]

    steps
    choose pivot
    place pivot such that the elememt to the right of pivot > a[pivot]
    and left should be smaller, left elements < a[pivot].

    conditions:
    pivot = end
    i = start-1
    j = start
    """

    def partition(start, end):
      pivot = end
      i = start - 1
      j = start

      while j < pivot:
        if arr[j] < arr[pivot]:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
        j += 1
      i += 1
      arr[i], arr[pivot] = arr[pivot], arr[i]

      return i

    def solve(start, end):
      if start >= end:
        return

      p = partition(start, end)

      # left recursion
      solve(start, p - 1)

      # right recursion
      solve(p + 1, end)

    arr = [7, 2, 1, 8, 6, 3, 5, 4]
    solve(0, len(arr) - 1)

    print(arr)
