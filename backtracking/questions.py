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

  def permutations_2(self):
    """
    47. leetcode
    Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.

    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]
    """

    def solve(nums, start, end, ans):
      #  base
      if start == end:
        ans.append(nums[:])
        return

      visited = {}
      for i in range(start, end):
        if nums[i] in visited and visited[nums[i]]:
          continue
        visited[nums[i]] = True
        nums[start], nums[i] = nums[i], nums[start]
        solve(nums, start + 1, end, ans)
        nums[start], nums[i] = nums[i], nums[start]

    nums = [1, 1, 2]
    ans = []
    solve(nums, 0, len(nums), ans)
    return ans

  def beautiful_arrangement(self):
    """
    526: Leetcode
    Suppose you have n integers labeled 1 through n. A permutation of those n integers 
    perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), 
    either of the following is true:

    perm[i] is divisible by i.
    i is divisible by perm[i].

    Input: n = 2
    Output: 2
    Explanation:
    The first beautiful arrangement is [1,2]:
        - perm[1] = 1 is divisible by i = 1
        - perm[2] = 2 is divisible by i = 2
    The second beautiful arrangement is [2,1]:
        - perm[1] = 2 is divisible by i = 1
        - i = 2 is divisible by perm[2] = 1
    """

    def solve(temp, n, ans, currNum):
      # base
      if currNum == n + 1:
        ans[0] += 1
        return

      for i in range(1, n + 1):
        if temp[i - 1] == 0 and (currNum % i == 0 or i % currNum == 0):
          temp[i - 1] = currNum
          solve(temp, n, ans, currNum + 1)
          temp[i - 1] = 0

    n = 3
    ans = [0]
    temp = [0] * n
    solve(temp, n, ans, 1)
    return ans[0]

  def distribute_repeatine_integers(self):
    """
    1655: Leetcode
    You are given an array of n integers, nums, where there are at most 50 unique values in 
    the array. You are also given an array of m customer order quantities, quantity, 
    where quantity[i] is the amount of integers the ith customer ordered. Determine if it is
    possible to distribute nums such that:

    Input: nums = [1,2,3,4], quantity = [2]
    Output: false
    Explanation: The 0th customer cannot be given two different integers.
    """

    def solve(c, q, iq):
      # base
      if iq == len(quantity):
        return True

      for i in range(len(c)):
        if c[i] >= quantity[iq]:
          c[i] -= quantity[iq]
          if solve(c, q, iq + 1):
            return True
          c[i] += quantity[iq]

      return False

    nums = [1, 1, 2, 2, 2, 2, 3, 3]
    quantity = [2, 2, 3]

    values_map = {}
    for i in range(len(nums)):
      if nums[i] in values_map:
        values_map[nums[i]] += 1
      else:
        values_map[nums[i]] = 1

    counts = list(values_map.values())

    quantity.sort(reverse=True)

    return solve(counts, quantity, 0)
