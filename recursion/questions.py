import sys


class Questions:

  def __init__(self):
    """
    """

  def check_array_sorted(self):
    """
    Check array is sorted or not using recursion.
    return True and False
    """

    def check_sorted(arr, n, idx):
      if idx >= n - 1:
        return True

      if arr[idx + 1] <= arr[idx]:
        return False

      return check_sorted(arr, n, idx + 1)

    # arr = [1, 2, 3, 4, 5, 6, 7]
    # arr = [2, 4, 5, 6, 8, 9, 7]
    # arr = [7, 6, 5, 4, 3, 2, 1]
    arr = [1]

    n = len(arr)
    idx = 0

    print(check_sorted(arr, n, idx))

  def binary_search_recursion(self):
    """
    """

    def bs(arr, start, end, key):
      if start > end:
        return -1

      mid = start + (end - start) // 2
      if arr[mid] == key:
        return mid

      if arr[mid] < key:
        return bs(arr, mid + 1, end, key)
      else:
        return bs(arr, start, mid - 1, key)

    arr = [2, 5, 7, 10, 14, 17, 20, 25, 39]
    n = len(arr)
    start = 0
    end = n - 1
    key = 5

    ans = bs(arr, start, end, key)

    print(ans)

  def subsquences_of_string(self):
    """
    input = "abc"
    subsequence = ["", "a", "ab", "ac", "abc", "b", "bc", "c"]
    power set ( all sub sets.)
    all subsquence = 2**n
    """

    def solve(string, output, idx, result):
      if idx >= len(string):
        result.append(output)
        return

      # Include
      solve(string, output + string[idx], idx + 1, result)

      # Exclude
      solve(string, output, idx + 1, result)

      return

    string = "abc"
    output = ""
    result = []
    idx = 0

    solve(string, output, idx, result)
    print(result)

  def phone_keypad_problem(self):
    """
    """

  def minimum_no_to_target_sum(self):
    """
    minimum number of elements required to reach target sum.
    input : [1,2,3]
    target : 5
    {1,1,1,1,1} : 5
    {1,1,1,2} : 4
    {1,2,2} : 3
    {1,1,3} : 3
    {2,3} : 2

    Answer = 2
    """

    def solve(arr, target):
      int_max = 2**31 - 1
      if target == 0:
        return 0

      if target < 0:
        return int_max

      mini = int_max
      for i in range(len(arr)):
        ans = solve(arr, target - arr[i])
        if ans != int_max:
          mini = min(mini, ans + 1)

      return mini

    arr = [1, 2, 3]
    target = 7

    ans = solve(arr, target)
    print(ans)

  def cut_into_segments(self):
    """
    N length rod, determine the maximum no of segements you can make of this rod, 
    provide that each segment should be of length x, y, z.
    """
    n = 3
    x = 5
    y = 2
    z = 2

    def solve(n, x, y, z):
      if n == 0:
        return 0

      if n < 0:
        return -2**31 - 1

      a = solve(n - x, x, y, z) + 1
      b = solve(n - y, x, y, z) + 1
      c = solve(n - z, x, y, z) + 1

      ans = max(a, b, c)

      return ans

    ans = solve(n, x, y, z)
    if ans < 0:
      ans = 0
    print(ans)

  def maximum_sum_non_adjecent(self):
    """
    maximum sum of non- adjacent elements.
    return the maximum sum of subsquence in which no two elements are ajdacent.
    arr = [2, 1, 4, 9]
    {2, 4} : 6
    {2, 9} : 11
    {1, 9} : 10

    output = 11
    """

    def solve(arr, n, idx, sum, maxi):
      if idx >= n:
        maxi[0] = max(sum, maxi[0])
        return

      # include
      solve(arr, n, idx + 2, sum + arr[idx], maxi)

      #exclude
      solve(arr, n, idx + 1, sum, maxi)

    arr = [2, 1, 4, 9]
    arr = [1, 2, 4]
    arr = [1, 2, 3, 5, 4]
    n = len(arr)
    idx = 0
    sum = 0
    maxi = [-2**31]

    solve(arr, n, idx, sum, maxi)
    print(maxi[0])

  def last_occurence_char(self):
    """
    find last occurence of a character.
    string = "abcddefg"
    """

    def solve_left_right(string, idx, key, ans):
      if idx >= len(string):
        return -1

      if key == string[idx]:
        ans[0] = idx

      return solve_left_right(string, idx + 1, key, ans)

    def solve_right_left(string, idx, key, ans):
      if idx < 0:
        return -1

      if key == string[idx]:
        ans[0] = idx

      return

    string = "absddefdg"
    idx = 0
    key = "z"
    ans = [-1]

    solve_left_right(string, idx, key, ans)
    print(string.rfind(""))

  def reverse_a_string(self):
    """
    """

    def solve(str_arr, start, end):
      if start >= end:
        return

      str_arr[start], str_arr[end] = str_arr[end], str_arr[start]

      solve(str_arr, start + 1, end - 1)

    string = "robin"
    str_arr = list(string)
    start = 0
    end = len(string) - 1

    solve(str_arr, start, end)

    print("".join(str_arr))

  def addition_two_string(self):
    """
    """
    num1 = "456"
    num2 = "77"

    def solve(num1, p1, num2, p2, ans, carry=0):

      if p1 < 0 and p2 < 0:
        if carry != 0:
          ans[0] += str(carry)
        return

      n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
      n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

      temp_sum = n1 + n2 + carry
      digit = temp_sum % 10
      carry = temp_sum // 10

      ans[0] += str(digit)

      solve(num1, p1 - 1, num2, p2 - 1, ans, carry)

    p1 = len(num1) - 1
    p2 = len(num2) - 1
    ans = [""]
    solve(num1, p1, num2, p2, ans)
    return ans[0][::-1]

  def check_palindrome_recursive(self):
    """
    """

    def solve(string, s, e):
      if s >= e:
        return True

      if string[s] != string[e]:
        return False

      return solve(string, s + 1, e - 1)

    string = "racecar"
    # string = "racetar"
    s = 0
    e = len(string) - 1

    ans = solve(string, s, e)
    print(ans)

  def remove_occurence_substring(self):
    """
    string = "daabcbaabcbc"
    part = "abc"
    """

    def solve(s, part):
      print(f"before : {s}")
      pos = s.find(part)
      if pos < 0:
        return s
      s = s.replace(part, "", 1)
      print(f"after : {s}")
      return solve(s, part)

    s = "eemckxmckx"
    part = "emckx"
    ans = solve(s, part)
    print(ans)

  def print_subarrays(self):
    """
    Print all subarrays using recursion.
    """

    def solve_util(arr, start, end):

      if end == len(arr):
        return

      for i in range(start, end + 1):
        print(arr[i], end=" ")
      print()

      solve_util(arr, start, end + 1)

    def solve(arr):
      for start in range(len(arr)):
        end = start
        solve_util(arr, start, end)

    arr = [1, 2, 3, 4, 5]
    solve(arr)

  def buy_sell_stock(self):
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy 
    before you sell.
    """

    def solve(prices, i, min_price, max_profit):

      if i == len(prices):
        return

      if prices[i] < min_price:
        min_price = prices[i]

      today_profit = prices[i] - min_price
      if today_profit > max_profit[0]:
        max_profit[0] = today_profit

      return solve(prices, i + 1, min_price, max_profit)

    prices = [7, 1, 5, 3, 6, 4]
    min_price = sys.maxsize
    max_profit = [0]
    i = 0

    solve(prices, i, min_price, max_profit)
    return max_profit[0]

  def house_robbery_1(self):
    """
    """

    def solve(nums, i):
      if i >= len(nums):
        return 0

      rob_amt1 = nums[i] + solve(nums, i + 2)
      rob_amt2 = 0 + solve(nums, i + 1)

      return max(rob_amt1, rob_amt2)

    nums = [2, 1, 1, 2]
    return solve(nums, 0)

  def interger_to_english(self):
    """
    Leetcode: 273
    Example 1:

    Input: num = 123
    Output: "One Hundred Twenty Three"
    Example 2:

    Input: num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"
    """

  def wild_card(self):
    """
    leetcode: 44
    Given an input string (s) and a pattern (p), implement wildcard pattern matching 
    with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).
    """

  def perfect_square(self):
    """
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, it is 
    the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect 
    squares while 3 and 11 are not.
    """

  
