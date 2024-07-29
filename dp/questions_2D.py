import sys


class Questions:

  #Function to return max value that can be put in knapsack of capacity W.
  def knapSack(self, W=4, wt={4, 5, 1}, val={1, 2, 3}, n=3):
    # code here

    def _knapSack_r(cap, idx, val, wt):
      # base case
      if idx == 0:
        if wt[0] <= cap:
          return val[0]
        else:
          return 0

      # include
      include = 0
      if wt[idx] <= cap:
        include = val[idx] + _knapSack_r(cap - wt[idx], idx - 1, val, wt)

      # exclude
      exclude = 0 + _knapSack_r(cap, idx - 1, val, wt)

      ans = max(include, exclude)

      return ans

    def _knapsack_m(cap, idx, val, wt, dp):
      # base case
      if idx == 0:
        if wt[0] <= cap:
          return val[0]
        else:
          return 0

      if dp[idx][cap] != -1:
        return dp[idx][cap]

      # include
      include = 0
      if wt[idx] <= cap:
        include = val[idx] + _knapsack_m(cap - wt[idx], idx - 1, val, wt, dp)

      # exclude
      exclude = 0 + _knapsack_m(cap, idx - 1, val, wt, dp)

      dp[idx][cap] = max(include, exclude)

      return dp[idx][cap]

    def _knapsack_t(cap, n, val, wt):
      dp = [[0 for _ in range(cap + 1)] for _ in range(n)]

      for w in range(cap + 1):
        if wt[0] <= w:
          dp[0][w] = val[0]
        else:
          dp[0][w] = 0

      for idx in range(1, n):
        for w in range(cap + 1):
          include = 0
          if wt[idx] <= w:
            include = val[idx] + dp[idx - 1][w - wt[idx]]

          exclude = 0 + dp[idx - 1][w]

          dp[idx][w] = max(include, exclude)

      return dp[n - 1][cap]

    def _knapsack_so(cap, n, val, wt):
      prev = [0 for _ in range(cap + 1)]
      curr = [0 for _ in range(cap + 1)]

      for w in range(cap + 1):
        if wt[0] <= w:
          prev[w] = val[0]
        else:
          prev[w] = 0

      for idx in range(1, n):
        for w in range(cap + 1):
          include = 0
          if wt[idx] <= w:
            include = val[idx] + prev[w - wt[idx]]

          exclude = 0 + prev[w]

          curr[w] = max(include, exclude)

        # shift: copy contents of curr to prev
        prev[:] = curr  # Need to remamber, copy

      return prev[cap]

    def _knapsack_further_so(cap, n, val, wt):
      curr = [0 for _ in range(cap + 1)]

      for w in range(cap + 1):
        if wt[0] <= w:
          curr[w] = val[0]
        else:
          curr[w] = 0

      for idx in range(1, n):
        for w in range(cap, -1, -1):
          include = 0
          if wt[idx] <= w:
            include = val[idx] + curr[w - wt[idx]]

          exclude = 0 + curr[w]

          curr[w] = max(include, exclude)

      return curr[cap]

    # # Recursion
    # ans = _knapSack_r(W, n-1, val, wt)

    # # DP: Memoization
    # dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    # ans = _knapsack_m(W, n-1, val, wt, dp)

    # # DP: Tabulation
    # ans = _knapsack_t(W, n, val, wt)

    # # space optimization.
    # ans = _knapsack_so(W, n, val, wt)

    # further space optimization.
    ans = _knapsack_further_so(W, n, val, wt)

    return ans

  def partition_equal_subset(self, nums=[1, 5, 11, 5]):
    """
    416: Leetcode -> Partition Equal Subset Sum
    """

    def _canP_r(nums, idx, target):
      # base case
      if idx >= len(nums):
        return False

      if target < 0:
        return False

      if target == 0:
        return True

      include = _canP_r(nums, idx + 1, target - nums[idx])

      exclude = _canP_r(nums, idx + 1, target)

      return include or exclude

    def _canP_m(nums, idx, target, dp):
      # base case
      if idx >= len(nums):
        return False
      if target < 0:
        return False
      if target == 0:
        return True

      if dp[idx][target] != -1:
        return dp[idx][target]

      include = _canP_m(nums, idx + 1, target - nums[idx], dp)
      exclude = _canP_m(nums, idx + 1, target, dp)

      dp[idx][target] = (include or exclude)
      return dp[idx][target]

    def _canP_t(nums, target):
      n = len(nums)
      dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

      for i in range(n):
        dp[i][0] = True

      for i in range(n - 1, -1, -1):
        for t in range(1, target + 1):
          include = False
          if t - nums[i] >= 0:
            include = dp[i + 1][t - nums[i]]
          exclude = dp[i + 1][t]

          dp[i][t] = (include or exclude)
      return dp[0][target]

    def _canP_so(nums, target):
      n = len(nums)
      curr = [False for _ in range(target + 1)]
      next = [False for _ in range(target + 1)]

      next[0] = True

      for i in range(n - 1, -1, -1):
        for t in range(1, target + 1):
          include = False
          if t - nums[i] >= 0:
            include = next[t - nums[i]]
          exclude = next[t]

          curr[t] = (include or exclude)

        next = curr[:]  # Copy curr to next to move to the next iteration
      return curr[target]

    def _canP_so_2(nums, target):
      """
      HW
      """

    total_sum = sum(nums)
    # need to remember.
    if total_sum & 1:
      return False
    target = total_sum // 2

    # # Recursion
    # n = len(nums) - 1
    # ans = _canP_r(nums, 0, target)

    # # DP: Memoization
    # n = len(nums)
    # dp = [[-1 for _ in range(target+1)] for _ in range(n)]
    # ans = _canP_m(nums, 0, target, dp)

    # # DP: Tabulation
    # ans = _canP_t(nums, target)

    # Space optimization.
    ans = _canP_so(nums, target)

    return ans

  def dice_rolls(self, n=1, k=6, target=3):
    """
    1155: Leetcode -> Number of Dice Rolls With Target Sum
    """
    MOD = 10**9 + 7

    def _nrt_r(n, k, target):
      # base
      if n < 0:
        return 0
      if n == 0 and target == 0:
        return 1
      if n == 0 and target != 0:
        return 0
      if n != 0 and target == 0:
        return 0

      ans = 0
      for i in range(1, k + 1):
        ans += _nrt_r(n - 1, k, target - i)

      return ans

    def _nrt_m(n, k, target, dp):
      # base
      if target < 0:
        return 0
      if n == 0:
        return 1 if target == 0 else 0

      if dp[n][target] != -1:
        return dp[n][target]

      ans = 0
      for i in range(1, k + 1):
        ans = (ans % MOD + _nrt_m(n - 1, k, target - i, dp) % MOD) % MOD

      dp[n][target] = ans
      return dp[n][target]

    def _nrt_t(n, k, target):
      dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

      dp[0][0] = 1

      for idx in range(1, n + 1):
        for t in range(1, target + 1):
          dp[idx][t] = 0
          for i in range(1, k + 1):
            if t - i >= 0:
              dp[idx][t] = (dp[idx][t] % MOD + dp[idx - 1][t - i] % MOD) % MOD

      return dp[n][target]

    def _nrt_so(n, k, target):
      prev = [0 for _ in range(target + 1)]
      curr = [0 for _ in range(target + 1)]

      prev[0] = 1

      for idx in range(1, n + 1):
        for t in range(target + 1):
          curr[t] = 0
          for i in range(1, k + 1):
            if t - i >= 0:
              curr[t] = (curr[t] + prev[t - i]) % MOD

        prev, curr = curr, prev  # Swap the references

      return prev[target]

    def _nrt_so_2(n, k, target):
      """
        HW
        """

    # # recursion
    # ans = _nrt_r(n, k, target)

    # # DP: Memoization
    # dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
    # ans = _nrt_m(n, k, target, dp)

    # # DP: tabulation
    # ans = _nrt_t(n, k, target)

    # space optimization
    ans = _nrt_so(n, k, target)

    return ans

  def minimum_swaps(self):
    """
    HW
    801: Leetcode -> Minimum Swaps To Make Sequences Increasing.
    """

  def guess_number(self, n=10):
    """
    375: Leetcode -> Guess Number Higher or Lower II
    """

    def _getMini_r(start, end):
      if start >= end:
        return 0

      ans = sys.maxsize

      for i in range(start, end + 1):
        ans = min(ans,
                  i + max(_getMini_r(start, i - 1), _getMini_r(i + 1, end)))

      return ans

    def _getMini_td(start, end, dp):
      if start >= end:
        return 0

      if dp[start][end] != -1:
        return dp[start][end]

      ans = sys.maxsize
      for i in range(start, end + 1):
        ans = min(
            ans, i +
            max(_getMini_td(start, i - 1, dp), _getMini_td(i + 1, end, dp)))

      dp[start][end] = ans
      return dp[start][end]

    def _getMini_t(n):
      dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

      for start in range(n, 0, -1):
        for end in range(1, n + 1):
          if start >= end:
            continue
          else:
            ans = sys.maxsize
            for i in range(start, end + 1):
              ans = min(ans, i + max(dp[start][i - 1], dp[i + 1][end]))

            dp[start][end] = ans

      return dp[1][n]

    # # Recursion
    # ans = _getMini_r(1, n)

    # # DP: Memoization
    # dp = [[-1 for _ in range(n + 1)] for _ in range( n + 1)]
    # ans = _getMini_td(1, n, dp)

    # DP: Tabulation
    ans = _getMini_t(n)

    return ans

  def min_cost_leaf_values(self, arr=[9,2, 4]):
    """
    1130: Leetcode -> Minimum Cost Tree From Leaf Values
    """

    def _mct_r(arr, hm, left, right):
      # base case
      if left == right:
        return 0

      ans = sys.maxsize

      for i in range(left, right):
        ans = min(
            ans, hmap[(left, i)] * hmap[(i + 1, right)] +
            _mct_r(arr, hm, left, i) + _mct_r(arr, hm, i + 1, right))

      return ans

    def _mct_m(arr, hm, left, right, dp):
      # base case
      if left == right:
        return 0

      if dp[left][right] != -1:
        return dp[left][right]

      ans = sys.maxsize
      for i in range(left, right):
        ans = min(
            ans, hm[(left, i)] * hm[(i + 1, right)] +
            _mct_m(arr, hm, left, i, dp) + _mct_m(arr, hm, i + 1, right, dp))

      dp[left][right] = ans

      return dp[left][right]

    def _mct_t(arr, hm):
      # base case
      dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

      for left in range(len(arr) - 1, -1, -1):
        for right in range(len(arr)):

          if left >= right:
            continue
          else:
            ans = sys.maxsize
            for i in range(left, right):
              ans = min(
                  ans, hm[(left, i)] * hm[(i + 1, right)] + dp[left][i] +
                  dp[i + 1][right])
            dp[left][right] = ans

      return dp[0][n - 1]

    # store maximum value for every range.
    hmap = {}
    n = len(arr)
    # pre compute
    for i in range(n):
      hmap[(i, i)] = arr[i]
      for j in range(i + 1, n):
        hmap[(i, j)] = max(arr[j], hmap[(i, j - 1)])

    # # Recursion
    # ans = _mct_r(arr, hmap, 0, n-1)

    # # DP: Memoization
    # dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    # ans = _mct_m(arr, hmap, 0, n-1, dp)

    # DP: Tabulation.
    ans = _mct_t(arr, hmap)

    return ans
