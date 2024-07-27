import sys


class Questions:

  def coin_change(self, coins, amount):
    """
    322: Leetcode -> Coin Change
    """

    def _recursion(amount):
      # base case
      if amount[0] == 0:
        return 0

      if amount[0] < 0:
        return sys.maxsize

      mini = sys.maxsize
      for i in range(len(coins)):
        ans = _recursion([amount[0] - coins[i]])
        if ans != sys.maxsize:
          mini = min(mini, 1 + ans)

      return mini

    def _solveTopDown(coins, amount, dp):
      # base case
      if amount[0] == 0:
        return 0

      if amount[0] < 0:
        return sys.maxsize

      if dp[amount[0]] != -1:
        return dp[amount[0]]

      mini = sys.maxsize
      for i in range(len(coins)):
        ans = _solveTopDown(coins, [amount[0] - coins[i]], dp)
        if ans != sys.maxsize:
          mini = min(mini, 1 + ans)

      dp[amount[0]] = mini
      return dp[amount[0]]

    def _solveTabulation(coins, amount):
      dp = [sys.maxsize] * (amount + 1)

      dp[0] = 0

      for i in range(1, amount + 1):

        for j in range(len(coins)):
          if i - coins[j] >= 0 and dp[i - coins[j]] != sys.maxsize:
            ans = dp[i - coins[j]]
            dp[i] = min(dp[i], 1 + ans)

      return dp[amount]

    # # using recursion
    # ans = _coinChange([amount])
    # if ans == sys.maxsize:
    #     return -1
    # return ans

    # # topdown approach.
    # dp = [-1] * (amount+1)
    # ans = _solveTopDown(coins, [amount], dp)
    # if ans == sys.maxsize:
    #     return -1
    # return ans

    # bottom up approach (tabulation)
    ans = _solveTabulation(coins, amount)
    if ans == sys.maxsize:
      return -1
    return ans

  def house_robber(self, nums):
    """
    198: Leetcode -> House Robber
    """

    def _recursion(nums, n):
      if n < 0:
        return 0

      if n == 0:
        return nums[0]

      # include
      include = _recursion(nums, n - 2) + nums[n]

      # exclude
      exclude = _recursion(nums, n - 1) + 0

      return max(include, exclude)

    def _topDown(nums, n, dp):
      if n < 0:
        return 0

      if n == 0:
        return nums[0]

      if dp[n] != -1:
        return dp[n]

      # include
      include = _topDown(nums, n - 2, dp) + nums[n]

      # exclude
      exclude = _topDown(nums, n - 1, dp) + 0

      dp[n] = max(include, exclude)

      return dp[n]

    def _tabulation(nums, n):
      dp = [0] * (n + 1)
      dp[0] = nums[0]

      for i in range(1, n + 1):
        temp = 0
        if i - 2 >= 0:
          temp = dp[i - 2]

        include = temp + nums[i]
        exclude = dp[i - 1] + 0

        dp[i] = max(include, exclude)

      return dp[n]

    def _space_optimize(nums, n):

      prev2 = 0
      prev1 = nums[0]

      curr = 0

      for i in range(1, n + 1):
        temp = 0
        if i - 2 >= 0:
          temp = prev2

        include = temp + nums[i]
        exclude = prev1 + 0

        curr = max(include, exclude)
        prev2 = prev1
        prev1 = curr

      return max(prev1, curr)

    # # using recursion.
    # return _recursion(nums, len(nums) - 1)

    # # top down approach.
    # n = len(nums) - 1
    # dp = [-1] * (n + 1)
    # return _topDown(nums, n, dp)

    # # tabulation approach.
    # n = len(nums) - 1
    # return _tabulation(nums, n)

    # tabulation approach.
    n = len(nums) - 1
    return _space_optimize(nums, n)

  def paiting_fences(self):
    """
    276: Leetcode -> Paint Fence

    f(n) = [f(n-1) + f(n-2)] * (k -1)

    NOTE: only space optimize solution running all the test cases.
    """
    #code here.
    MOD = (10**9 + 7)

    def _recursion(n, k):
        if n == 1:
            return k
        if n == 2:
            return k + k*(k-1)

        ans = (_recursion(n-1, k) + _recursion(n-2, k)) * (k - 1)

        return ans

    def _topdown(n, k, dp):
        if n == 1:
            return k
        if n == 2:
            return ( k + k*(k-1) ) % MOD

        if dp[n] != -1:
            return dp[n]

        dp[n] = ( (_topdown(n-1, k, dp) * (k - 1)) % MOD + (_topdown(n-2, k, dp) * (k - 1)) % MOD ) % MOD

        return dp[n]

    def _tabulation(n, k):
        if n == 1:
            return k
        if n == 2:
            return ( k + k*(k-1) ) % MOD
        dp = [0] * (n + 1)

        dp[1] = k
        dp[2] = ( k + k*(k-1) ) % MOD

        for i in range(3, n+1):
            dp[i] = ( (dp[i-1] * (k - 1)) % MOD + ( dp[i-2] * (k - 1)) % MOD ) % MOD

        return dp[n]

    def _space_optimize(n, k):

        if n == 1:
            return k
        if n == 2:
            return ( k + k*(k-1) ) % MOD

        prev2 = k
        prev1 = ( k + k*(k-1) ) % MOD

        for i in range(3, n+1):
            curr = ( prev2 + prev1 ) * (k - 1) % MOD
            prev2 = prev1
            prev1 = curr

        return prev1


    # # recursion
    # ans = _recursion(n, k)

    # # topdown
    # dp = [-1] * (n+1)
    # ans = _topdown(n, k, dp)

    # # tabulation.
    # ans = _tabulation(n, k)

    # space optimisation.
    ans = _space_optimize(n, k)

    return ans
  
  def suger_egg_drop(self):
    """
    887: Leetcode -> Super Egg Drop
    """
