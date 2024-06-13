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

  def phone_keypad_problem():
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


      a = solve(n-x, x, y, z) + 1
      b = solve(n-y, x, y, z) + 1
      c = solve(n-z, x, y, z) + 1
      
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
      solve(arr, n, idx+2, sum+arr[idx], maxi)

      #exclude
      solve(arr, n, idx+1, sum, maxi)

    arr = [2, 1, 4, 9]
    arr = [1,2,4]
    arr = [1,2,3,5,4]
    n = len(arr)
    idx = 0
    sum = 0
    maxi = [-2**31]
    
    solve(arr, n, idx, sum, maxi)
    print(maxi[0])


  def house_robbery_1():
    """
    """        