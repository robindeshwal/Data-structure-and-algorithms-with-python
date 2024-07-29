import sys


class Questions:

  def coin_change(self, coins=[1, 2, 5], amount=11):
    """
    322: Leetcode -> Coin Change
    """

    def _coinChange_r(amount):
      # base case
      if amount[0] == 0:
        return 0

      if amount[0] < 0:
        return sys.maxsize

      mini = sys.maxsize
      for i in range(len(coins)):
        ans = _coinChange_r([amount[0] - coins[i]])
        if ans != sys.maxsize:
          mini = min(mini, 1 + ans)

      return mini

    def _coinChange_m(coins, amount, dp):
      # base case
      if amount[0] == 0:
        return 0

      if amount[0] < 0:
        return sys.maxsize

      if dp[amount[0]] != -1:
        return dp[amount[0]]

      mini = sys.maxsize
      for i in range(len(coins)):
        ans = _coinChange_m(coins, [amount[0] - coins[i]], dp)
        if ans != sys.maxsize:
          mini = min(mini, 1 + ans)

      dp[amount[0]] = mini
      return dp[amount[0]]

    def _coinChange_t(coins, amount):
      dp = [sys.maxsize] * (amount + 1)

      dp[0] = 0

      for i in range(1, amount + 1):

        for j in range(len(coins)):
          if i - coins[j] >= 0 and dp[i - coins[j]] != sys.maxsize:
            ans = dp[i - coins[j]]
            dp[i] = min(dp[i], 1 + ans)

      return dp[amount]

    # # Recursion
    # ans = _coinChange_r([amount])
    # if ans == sys.maxsize:
    #     return -1
    # return ans

    # # DP: Memoization.
    # dp = [-1] * (amount+1)
    # ans = _coinChange_m(coins, [amount], dp)
    # if ans == sys.maxsize:
    #     return -1
    # return ans

    # DP: Tabulation
    ans = _coinChange_t(coins, amount)
    if ans == sys.maxsize:
      return -1
    return ans

  def house_robber(self, nums=[1, 2, 3, 1]):
    """
    198: Leetcode -> House Robber
    """

    def _house_rob_r(nums, n):
      if n < 0:
        return 0

      if n == 0:
        return nums[0]

      # include
      include = _house_rob_r(nums, n - 2) + nums[n]

      # exclude
      exclude = _house_rob_r(nums, n - 1) + 0

      return max(include, exclude)

    def _house_rob_m(nums, n, dp):
      if n < 0:
        return 0

      if n == 0:
        return nums[0]

      if dp[n] != -1:
        return dp[n]

      # include
      include = _house_rob_m(nums, n - 2, dp) + nums[n]

      # exclude
      exclude = _house_rob_m(nums, n - 1, dp) + 0

      dp[n] = max(include, exclude)

      return dp[n]

    def _house_rob_t(nums, n):
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

    def _house_rob_so(nums, n):

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
    # return _house_rob_r(nums, len(nums) - 1)

    # # DP: Memoization.
    # n = len(nums) - 1
    # dp = [-1] * (n + 1)
    # return _house_rob_m(nums, n, dp)

    # # DP: Tabulation.
    # n = len(nums) - 1
    # return _house_rob_t(nums, n)

    # DP: space optimizarion.
    n = len(nums) - 1
    return _house_rob_so(nums, n)

  def paiting_fences(self, n=4, k=3):
    """
    276: Leetcode -> Paint Fence

    f(n) = [f(n-1) + f(n-2)] * (k -1)

    NOTE: only space optimize solution running all the test cases.
    """
    #code here.
    MOD = (10**9 + 7)

    def _paint_fence_r(n, k):
      if n == 1:
        return k
      if n == 2:
        return k + k * (k - 1)

      ans = (_paint_fence_r(n - 1, k) + _paint_fence_r(n - 2, k)) * (k - 1)

      return ans

    def _paint_fence_m(n, k, dp):
      if n == 1:
        return k
      if n == 2:
        return (k + k * (k - 1)) % MOD

      if dp[n] != -1:
        return dp[n]

      dp[n] = ((_paint_fence_m(n - 1, k, dp) * (k - 1)) % MOD +
               (_paint_fence_m(n - 2, k, dp) * (k - 1)) % MOD) % MOD

      return dp[n]

    def _paint_fence_t(n, k):
      if n == 1:
        return k
      if n == 2:
        return (k + k * (k - 1)) % MOD
      dp = [0] * (n + 1)

      dp[1] = k
      dp[2] = (k + k * (k - 1)) % MOD

      for i in range(3, n + 1):
        dp[i] = ((dp[i - 1] * (k - 1)) % MOD + (dp[i - 2] *
                                                (k - 1)) % MOD) % MOD

      return dp[n]

    def _paint_fence_so(n, k):

      if n == 1:
        return k
      if n == 2:
        return (k + k * (k - 1)) % MOD

      prev2 = k
      prev1 = (k + k * (k - 1)) % MOD

      for i in range(3, n + 1):
        curr = (prev2 + prev1) * (k - 1) % MOD
        prev2 = prev1
        prev1 = curr

      return prev1

    # # recursion
    # ans = _paint_fence_r(n, k)

    # # DP: Memoization
    # dp = [-1] * (n+1)
    # ans = _paint_fence_m(n, k, dp)

    # # DP: Tabulation.
    # ans = _paint_fence_t(n, k)

    # space optimisation.
    ans = _paint_fence_so(n, k)

    return ans

  def suger_egg_drop(self):
    """
    887: Leetcode -> Super Egg Drop
    """
