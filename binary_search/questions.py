from .practice import BinarySearch


class BinarySearchQuestions:

  def __init__(self) -> None:
    pass

  def first_occurance(self,
                      arr=[1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9],
                      target=4):
    """
    find the first occurance of an element in sorted array.
    arr = [1,3,4,4,4,4,4,4,6,7,9]
    ouptut = 2
    """
    start = 0
    end = len(arr) - 1

    ans = -1

    while (start <= end):
      mid = start + (end - start) // 2
      if arr[mid] == target:
        ans = mid
        end = mid - 1
      elif arr[mid] < target:
        start = mid + 1
      else:
        end = mid - 1

    return ans

  def last_occurance(self, arr=[1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9], target=4):
    """
    find the last occurance of an element in sorted array.
    arr = [1,3,4,4,4,4,4,4,6,7,9]
    ouptut = 2
    """
    start = 0
    end = len(arr) - 1

    ans = -1

    while (start <= end):
      mid = start + (end - start) // 2
      if arr[mid] == target:
        ans = mid
        start = mid + 1
      elif arr[mid] < target:
        start = mid + 1
      else:
        end = mid - 1

    return ans

  def total_occurance(self):
    """
    arr = [1,3,4,4,4,4,4,4,6,7,9]
    ouptut = 2
    """
    arr = [1, 3, 4, 5, 5, 5, 5, 6, 7, 9]
    target = 5
    first_occ = self.first_occurance(arr, target)
    last_occ = self.last_occurance(arr, target)

    return last_occ - first_occ + 1

  def find_missing_element(self):
    """
    arr=[1, 2, 3, 4, 6, 7, 8]
    find the missing element using binary search
    """
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

    start = 0
    end = len(arr) - 1
    ans = -1
    while (start <= end):
      mid = start + (end - start) // 2
      if arr[mid] != mid + 1:
        ans = mid + 1
        end = mid - 1
      else:
        start = mid + 1

    return ans

  def peak_element(self):
    """
    peak element in a mountain array.
    """
    arr = [0, 10, 5, 2, 1]

    length = len(arr)

    start = 0
    end = length - 1

    while (start < end):
      mid = start + (end - start) // 2
      if arr[mid] < arr[mid + 1]:
        start = mid + 1
      else:
        end = mid
    return end, arr[end]

  def find_pivot(self):
    """
    find pivot using binary search.
    """
    arr = [2, 3, 5, 1]

    start = 0
    end = len(arr) - 1

    while (start <= end):
      mid = start + (end - start) // 2

      if mid + 1 < len(arr) and arr[mid] > arr[mid + 1]:
        return mid, arr[mid]
      if mid - 1 >= 0 and arr[mid] < arr[mid - 1]:
        return mid - 1, arr[mid - 1]

      if arr[start] >= arr[mid]:
        end = mid - 1
      else:
        start = mid + 1
    return start

  def search_rotated_sorted(self):
    """
    search in a rotated and sorted array.
    """

    def binary_search(nums, target, start, end):
      while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
          end = mid - 1
        elif nums[mid] < target:
          start = mid + 1
        else:
          return mid
      return -1

    def pivot(nums):
      start = 0
      end = len(nums) - 1

      while start < end:
        mid = start + (end - start) // 2
        if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
          return mid
        if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
          return mid - 1

        if nums[start] >= nums[mid]:
          end = mid - 1
        else:
          start = mid
      return start

    def search(nums, target):

      pvt = pivot(nums)
      if (target >= nums[0] and target <= nums[pivot]):
        ans = binary_search(nums, target, 0, pivot)
        return ans

      if (pvt + 1 < len(nums) and target >= nums[pvt + 1]
          and target <= nums[len(nums) - 1]):
        ans = binary_search(nums, target, pvt + 1, len(nums) - 1)
        return ans

      return -1

    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    print(search(arr, target))

  def square_root(self):
    """
    square root of a number using binary search.
    """
    n = 10

    def finsSqrt(n):
      start = 0
      end = n
      ans = -1
      while (start <= end):
        mid = start + (end - start) // 2
        if mid * mid == n:
          return mid
        elif mid * mid > n:
          end = mid - 1
        else:
          ans = mid
          start = mid + 1
      return ans

    square_root = finsSqrt(n)
    print(square_root)
