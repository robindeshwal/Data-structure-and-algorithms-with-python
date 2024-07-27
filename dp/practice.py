class Practice:

  def fibonacci(self, num=5):
    """
    509: Leetcode -> Fibonacci Number
    """

    def recursion(n):
      # base case:
      if n == 1 or n == 0:
        return n

      ans = recursion(n - 1) + recursion(n - 2)
      return ans

    def topDown(n, dp):
      # base case:
      if n == 1 or n == 0:
        return n

      # check if ans already exists.
      if dp[n] != -1:
        return dp[n]

      dp[n] = topDown(n - 1, dp) + topDown(n - 2, dp)

      return dp[n]

    def bottomUp(n):  # tabulation method.

      # step1: create dp array.
      dp = [-1] * (n + 1)

      # step2: base cases.
      # if n is 0
      if n == 0:
        return 0

      dp[0] = 0
      dp[1] = 1

      # step3:
      for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

      return dp[n]

    def space_optimisation(n):

      # step1: base cases.
      if n < 2:
        return n

      prev2 = 0
      prev1 = 1

      curr = 0
      # step2:
      for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

      return curr

    # return recursion(n)

    # dp = [-1]*(n+1)
    # return topDown(n, dp)

    # return bottomUp(n)

    return space_optimisation(n)
