class Questions:

  def __init__(self) -> None:
    pass

  def no_of_square(self):
    """
    Number of square full arrays.
    """

  def word_break(self):
    """
    word break 2
    """

  def letter_tile(self):
    """
    letter tile combination.
    """

  def sum_of_all_subset(self):
    """
    sum of all subset XOR.
    """

  def combination_sum(self):
    """
    39. Leetcode
    Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    """

    def solve(idx, ans, target, temp):
      # base
      if target == 0:
        """
          Appending the temp list directly to ans means that changes to temp will 
          affect the contents of ans.
          Appending a copy of temp to ans with temp[:] to avoid modifications.
          """
        ans.append(temp[:])
        return

      if target < 0:
        return

      for i in range(idx, len(candidates)):
        temp.append(candidates[i])
        solve(i, ans, target - candidates[i], temp)
        temp.pop()

    candidates = [2, 3, 6, 7]
    target = 7
    ans = []
    temp = []
    solve(0, ans, target, temp)
    return ans

  def combination_sum_2(self):
    """
    40. leetcode
    Given a collection of candidate numbers (candidates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]
    """

    def solve(idx, target, temp, ans):
      # base
      if target == 0:
        ans.append(temp[:])
        return

      if target < 0:
        return

      for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
          continue
        temp.append(candidates[i])
        solve(i + 1, target - candidates[i], temp, ans)
        temp.pop()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    candidates.sort()
    ans = []
    temp = []
    solve(0, target, temp, ans)
    return ans
