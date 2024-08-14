import sys


class FixedSizeWindow:

  def sliding_window_maximum(self):
    """
    239: Leetcode -> Sliding Window Maximum
    """


class VariableSizeWindow:

  def maximum_size(self, nums, target):
    """
    209: Leetcode -> Minimum Size Subarray Sum
    """
    i = 0
    j = 0
    temp_sum = 0
    length = sys.maxsize

    while j < len(nums):
      temp_sum += nums[j]

      while temp_sum >= target:
        length = min(length, j - i + 1)
        temp_sum -= nums[i]
        i += 1
      j += 1

    if length == sys.maxsize:
      return 0
    return length


class TwoPointerApproach:

  def twosum(self, nums, target):
    """
    1: Leetcode -> two sum
    """
    temp = []

    for i in range(len(nums)):
      num = nums[i]
      temp.append((num, i))

    temp.sort()
    s = 0
    e = len(nums) - 1

    while s < e:
      if temp[s][0] + temp[e][0] == target:
        return [temp[s][1], temp[e][1]]
      elif temp[s][0] + temp[e][0] > target:
        e -= 1
      else:
        s += 1

    return [-1, -1]


class OptimizedSlidingWindows:

  def t(self):
    ""
