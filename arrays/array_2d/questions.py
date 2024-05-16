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

  def factorial_large_number(self):
    """
    find factorial of large number.
    """

  def spiral_print(self):
    """
    spiral print
    """

  def wave_print(self):
    """
    wave_print
    """

  def rotate_matrix(self):
    """
    rotate a matrix to 90 degree.
    """
