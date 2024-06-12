class Practice:

  def __init__(self):
    pass

  def factorial(self):
    """
    """

    def fact(n):
      if n == 1:
        return 1
      return n * fact(n - 1)

    print(fact(5))

  def binary_search_recursive(self):
    """
    """

  def fibonacci_series(self):
    """
    0, 1, 1, 2, 3, 5, 8, 13 ...
    """

    def fib(n):
      if n == 0 or n == 1:
        return n
      return fib(n - 1) + fib(n - 2)

    n = 8
    print(fib(n))

  def counting(self):
    """
    n = 5
    5, 4, 3, 2, 1
    """
    n = 5

    def reverse_counting(n):
      # Base case
      if n == 0:
        return
      print(n)
      reverse_counting(n - 1)

    reverse_counting(5)

    def simple_counting(n):
      if n == 0:
        return
      simple_counting(n - 1)
      print(n)

    simple_counting(5)

  def print_array(self):
    """
    arr = [10,20,30,40,50]
    """
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    idx = 0

    def print_recursive_1(arr, n, idx):
      if idx >= n:
        return
      print(arr[idx])
      return print_recursive_1(arr, n, idx + 1)

    def print_recursive_2(arr, n):
      if n == 0:
        return
      print(arr[0])
      return print_recursive_2(arr[1:], n - 1)

    # print_recursive_1(arr, n, idx)
    print_recursive_2(arr, n)

  def max_element_array(self):
    """
    """

    def max_element(arr, n, idx, maxi):
      if idx >= n:
        return maxi

      if arr[idx] > maxi:
        maxi = arr[idx]

      return max_element(arr, n, idx + 1, maxi)

    arr = [1, 5, 7, 10, 19, 4, 6, 9]
    n = len(arr)
    idx = 0
    maxi = -2**31

    maxi = max_element(arr, n, idx, maxi)
    print(maxi)

  def min_element_array(self):
    """
    """

    def min_element(arr, n, idx, mini):
      if idx >= n:
        return

      if arr[idx] < mini[0]:
        mini[0] = arr[idx]

      return min_element(arr, n, idx + 1, mini)

    arr = [2, 5, 7, 10, 19, 4, 6, 9]
    n = len(arr)
    idx = 0
    mini = [2**31 - 1]

    min_element(arr, n, idx, mini)
    print(mini[0])

  def find_string(self):
    """
    find a character in a string using recursion.
    string = "robindeshwal"
    chr = "e"
    """

    def chr_idx(string, n, chr, idx, ans):
      if idx >= n:
        return -1

      if string[idx] == chr:
        ans.append(idx)

      return chr_idx(string, n, chr, idx + 1, ans)

    string = "robindeshwalrobindeshwal"
    n = len(string)
    chr = "r"
    idx = 0
    ans = []

    chr_idx(string, n, chr, idx, ans)
    print(ans)

  def print_digits(self):
    """
    input = 647
    print all digits.
    """

    def print_digit(number):
      if number == 0:
        return

      print_digit(number // 10)

      digit = number % 10
      print(digit)

    input = 647
    if input == 0:
      print(0)
    print_digit(input)
