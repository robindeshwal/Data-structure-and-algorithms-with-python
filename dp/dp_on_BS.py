from bisect import bisect_left


class Questions:
  """
  DP on binary search
  """

  def LIS(self):
    """
    300: Leetcode -> Longest Increasing Subsequence
    """

    def _lis_binary_search(nums):
      if not nums:
        return 0

      ans = []
      ans.append(nums[0])

      for i in range(1, len(nums)):
        if nums[i] > ans[-1]:
          ans.append(nums[i])
        else:
          # overide
          idx = bisect_left(ans, nums[i])
          ans[idx] = nums[i]

      return len(ans)

  def russian_doll(self):
    """
    HW
    354: Leetcode -> Russian Doll Envelopes
    """
 