class Climbing_stars:

  def __init__(self):
    """
    70. Leetcode:
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to      the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    """

  def recursion_approach(self):
    n = 2

    def steps(n):
      if n == 0 or n == 1:
        return 1
      return steps(n - 1) + steps(n - 2)

    return steps(n)
