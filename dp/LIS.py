from bisect import bisect_left


class Questions:

  def lis(self, nums):
    """
    300: Leetcode -> Longest Increasing Subsequence.
    """

    def _lis_r(nums, idx, prev):
      if idx >= len(nums):
        return 0

      # include
      include = 0
      if prev == -1 or nums[idx] > nums[prev]:
        include = 1 + _lis_r(nums, idx + 1, idx)

      # exclude
      exclude = 0 + _lis_r(nums, idx + 1, prev)

      ans = max(include, exclude)

      return ans

    def _lis_m(nums, idx, prev, dp):
      if idx >= len(nums):
        return 0

      if dp[idx][prev + 1] != -1:
        return dp[idx][prev + 1]

      # include
      include = 0
      if prev == -1 or nums[idx] > nums[prev]:
        include = 1 + _lis_m(nums, idx + 1, idx, dp)

      # exclude
      exclude = 0 + _lis_m(nums, idx + 1, prev, dp)

      dp[idx][prev + 1] = max(include, exclude)

      return dp[idx][prev + 1]

    def _lis_t(nums):
      n = len(nums)
      dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

      for idx in range(n - 1, -1, -1):
        for prev in range(idx - 1, -2, -1):
          # include
          include = 0
          if prev == -1 or nums[idx] > nums[prev]:
            include = 1 + dp[idx + 1][idx + 1]

          # exclude
          exclude = 0 + dp[idx + 1][prev + 1]

          dp[idx][prev + 1] = max(include, exclude)

      return dp[0][0]

    def _lis_so(nums):
      n = len(nums)
      curr = [0 for _ in range(n + 1)]
      next = [0 for _ in range(n + 1)]

      for idx in range(n - 1, -1, -1):
        for prev in range(idx - 1, -2, -1):
          # include
          include = 0
          if prev == -1 or nums[idx] > nums[prev]:
            include = 1 + next[idx + 1]

          # exclude
          exclude = 0 + next[prev + 1]

          curr[prev + 1] = max(include, exclude)

        next = curr[:]

      return next[0]

    def _lis_optimal(nums):
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

    # # Recursion
    # ans = _lis_r(nums, 0, -1)

    # # Memoization
    # n = len(nums)
    # dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    # ans = _lis_m(nums, 0, -1, dp)

    # # DP: Tablulation
    # ans = _lis_t(nums)

    # # DP: SO
    # ans = _lis_so(nums)

    # Using binary search.
    ans = _lis_optimal(nums)

    return ans

  def stacking_cuboid(self):
    """
    1691. Maximum Height by Stacking Cuboids 
    """
