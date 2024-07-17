class Heap:

  def __init__(self, arr=[]):
    self.arr = arr
    self.size = 0

  def insert(self, value):
    # value insert at end
    self.size = self.size + 1
    self.arr.append(value)
    index = self.size - 1

    # place at its right(correct) position.
    while (index > 0):
      parentIndex = (index - 1) // 2
      if self.arr[index] > self.arr[parentIndex]:
        self.arr[index], self.arr[parentIndex] = self.arr[
            parentIndex], self.arr[index]
        index = parentIndex
      else:
        break

  def deletion(self):
    # replace root value with last data.
    ans = self.arr[0]
    self.arr[0] = self.arr[-1]
    del self.arr[-1]
    self.size -= 1

    # plase root data on its correct position.
    index = 0
    while (index < self.size - 1):
      left = 2 * index + 1
      right = 2 * index + 2

      largest = index
      if left < self.size and self.arr[largest] < self.arr[left]:
        largest = left

      if right < self.size and self.arr[largest] < self.arr[right]:
        largest = right

      if largest == index:
        # value is at correct position
        break
      else:
        self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
        index = largest

    return ans

  def heapify(self, arr, n, i):
    """
    heapify (creation.)
    """
    index = i
    leftIndex = 2 * i + 1
    rightIndex = 2 * i + 2

    largest = index
    if leftIndex < n and arr[largest] < arr[leftIndex]:
      largest = leftIndex

    if rightIndex < n and arr[largest] < arr[rightIndex]:
      largest = rightIndex

    if index != largest:
      # left ya right child koi large hai.
      arr[index], arr[largest] = arr[largest], arr[index]
      index = largest
      self.heapify(arr, n, index)

  def build_heap(self, arr, n):

    for i in range(n // 2 - 1, -1, -1):
      self.heapify(arr, n, i)

    return arr

  def heap_sort(self, arr):
    n = len(arr)
    # TODO: check why while loop is not working.
    self.build_heap(arr, n)

    while n != 0:
      arr[0], arr[n - 1] = arr[n - 1], arr[0]
      n -= 1
      self.heapify(arr, n, 0)

    # return arr
    # working both ways.
    # self.build_heap(arr, n)

    # for i in range(n - 1, 0, -1):
    #   # Move current root to end
    #   arr[i], arr[0] = arr[0], arr[i]
    #   # call max heapify on the reduced heap
    #   self.heapify(arr, i, 0)

    return arr
