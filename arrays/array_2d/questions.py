class Practice:

  def sort_colors(self):
    """
    sort 0's, 1's and 2's in an array.
    """
    array = [2, 0, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0]

    # array = [2, 0, 2, 1, 1, 0]
    array = [2, 0, 1]

    # Brute force approch:
    def brute_force(array):
      zeros = 0
      ones = 0
      twos = 0
      for idx in range(len(array)):
        if array[idx] == 0:
          zeros += 1
        elif array[idx] == 1:
          ones += 1
        else:
          twos += 1
      result = [0] * zeros + [1] * ones + [2] * twos
      return result

    # Better solution.
    def better_solution(array):
      start = 0
      mid = 0
      end = len(array) - 1

      while (mid <= end):
        if array[mid] == 0:
          array[start], array[mid] = array[mid], array[start]
          start += 1
          mid += 1
        elif array[mid] == 1:
          mid += 1
        else:
          array[end], array[mid] = array[mid], array[end]
          end -= 1
      return array

    print(better_solution(array))

  def move_negative_one_side(self):
    """
    move all -ve numbers to one side of array.
    """
    array = [1, 2, -3, 4, -5, 6]

    def brute_force(array):
      # Do yourself
      pass

    def better_solution(array):
      start = 0
      end = len(array) - 1
      while (start <= end):
        if array[start] < 0:
          start += 1
        elif array[end] > 0:
          end -= 1
        else:
          array[start], array[end] = array[end], array[start]
          start += 1
          end -= 1
      return array

    print(better_solution(array))

  def duplicate_element(self):
    """
    find all duplicate element from an array.
    """
    array = [1, 3, 4, 2, 2]

    def brute_force(array):
      dict = {}
      for i in range(len(array)):
        if array[i] in dict:
          return array[i]
        else:
          dict[array[i]] = 1

    def better_solution(array):
      """
      Modifying array.
      """
      index = -1
      for i in range(0, len(array)):
        index = abs(array[i])
        if array[index] < 0:
          ans = index
          break
        array[index] *= -1

      return index

    def best_solution(array):
      """
      without modifying array. 
      Not working because list modification doesn't work properly?
      solution: array[0] modified first due to that array[array[0]] will get always updated value, not the old value.
      """
      while array[0] != array[array[0]]:
        temp = array[array[0]]
        array[array[0]] = array[0]
        array[0] = temp

      return array[0]

    print(best_solution(array))

  def missing_element(self):
    """
    find missing element from an array.
    """

  def first_repeat_element(self):
    """
    find first repeating element.
    """

  def common_elements(self):
    """
    find common element in 3 arrays.
    """
    a = [1, 5, 10, 20, 40, 80]
    b = [6, 7, 20, 80, 100]
    c = [3, 4, 15, 20, 30, 70, 80, 120]

    def brute_force(a, b, c):
      result = []
      for i in range(len(a)):
        for j in range(len(b)):
          for k in range(len(c)):
            if a[i] == b[j] == c[k]:
              result.append(a[i])

      return result

    def better_solution(a, b, c):
      result = set()
      i, j, k = 0, 0, 0
      while (i < len(a) and j < len(b) and k < len(c)):
        if a[i] == b[j] == c[k]:
          result.add(a[i])
          i, j, k = i + 1, j + 1, k + 1
        elif a[i] < b[j]:
          i += 1
        elif b[j] < c[k]:
          j += 1
        else:
          k += 1
      return result

    print(better_solution(a, b, c))

  def add_two_numbers(self):
    """
    add two numbers represented by two arrays.
    [1,2], and [2, 1]
    output: [3,3]
    """
    arr1 = [9, 5, 4, 9]
    arr2 = [2, 1, 4]
    # 9763

    i = len(arr1) - 1
    j = len(arr2) - 1

    carry = 0
    result = []
    while (i >= 0 and j >= 0):
      temp = arr1[i] + arr2[j] + carry
      digit = temp % 10
      result.insert(0, digit)
      carry = temp // 10
      i -= 1
      j -= 1
    while (i >= 0):
      temp = arr1[i] + carry
      digit = temp % 10
      result.insert(0, digit)
      carry = temp // 10
      i -= 1

    while (j >= 0):
      temp = arr1[j] + carry
      digit = temp % 10
      result.insert(0, digit)
      carry = temp // 10
      j -= 1
    if carry:
      result.insert(0, carry)

    print(result)
    return result

  def factorial_large_number(self):
    """
    find factorial of large number.
    """
    n = 200
    result = [1]
    carry = 0
    for i in range(2, n + 1):
      length = len(result)
      while (length > 0):
        temp = result[length - 1] * i + carry
        result[length - 1] = temp % 10
        carry = temp // 10
        length -= 1
      while (carry):
        result.insert(0, carry % 10)
        carry = carry // 10
    result = "".join(map(str, result))
    print(result)
    return result

  def spiral_print(self):
    """
    spiral print
    1 2 3
    4 5 6
    7 8 9
    10 11 12

    Leetcode: 54
    """

  def wave_print(self):
    """
    wave print 2D array.
    1 2 3 4
    5 6 7 8
    9 10 11 12

    output: 1 5 9 10 6 2 3 7 11 12 8 4
    """
    array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    rows = len(array)
    columns = len(array[0])

    for col in range(columns):
      for row in range(rows):
        if col % 2 == 0:
          print(array[row][col], end=" ")
        else:
          print(array[rows - row - 1][col], end=" ")

  def rotate_matrix(self):
    """
    rotate a matrix to 90 degree.
    """
