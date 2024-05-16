from lib.decorator import print_before


class Pyramid:

  def __init__(self):
    print("==== Pyramid patterns examples ====")

  """
      *
     * *  
    * * *
   * * * *
  * * * * *
  """

  @print_before
  def full_pyramid(self, n):
    for row in range(n):
      for col in range(n):
        temp = ""
        if col < (n - row) - 1:
          temp += " "
        else:
          temp += "* "
        print(temp, end="")
      print()

  """
  *
  * *
  * * *
  * * * *
  * * * * *
  """

  @print_before
  def half_pyramid_stars(self, n):
    for row in range(n):
      for col in range(n):
        temp = ""
        if col > row:
          temp += " "
        else:
          temp += "*"
        print(temp, end=" ")
      print()

  """
  *
  * *
  * * *
  * * * *
  * * * * *
  """

  @print_before
  def half_pyramid_numbers(self, n):
    for row in range(n):
      for col in range(n):
        temp = ""
        if col > row:
          temp += " "
        else:
          temp += str(col + 1)
        print(temp, end=" ")
      print()

  """
  * * * * *
   * * * *
    * * *
     * *
      *
  """

  @print_before
  def inverted_full_pyramid(self, n):
    for row in range(n):
      for col in range(n):
        temp = ""
        if col < row:
          temp += " "
        else:
          temp += "* "
        print(temp, end="")
      print()

  """
  * * * * *
  * * * *
  * * *
  * *
  *
  """

  @print_before
  def inverted_half_pyramid(self, n):
    for row in range(n):
      for col in range(n):
        temp = ""
        if col < (n - row):
          temp += "* "
        else:
          temp += " "
        print(temp, end=" ")
      print()

  """
       *
      * *
     *   *
    *     *
   *       *
  * * * * * *
  """

  @print_before
  def hollow_full_pyramid(self, n):
    for row in range(n):
      k = 0
      for col in range((2 * n) - 1):
        temp = ""
        if col < (n - row - 1):
          temp += " "
        elif k < (2 * row + 1):
          if k == 0 or k == (2 * row) or row == n - 1:
            temp += "*"
          else:
            temp += " "
          k += 1
        else:
          temp += " "
        print(temp, end="")
      print()

  """
  A
  A B A
  A B C B A
  A B C D C B A
  A B C D E D C B A
  """

  @print_before
  def alphabet_palindrome_pyramid(self, n):
    for row in range(65, 65 + n + 1):
      temp = ""
      for col in range(65, row):
        temp += str(chr(col) + " ")

      for col in range(row, 64, -1):
        temp += str(chr(col) + " ")
      print(temp, end="")
      print()

  """
      1
     1 2
    1   3
   1     4
  1 2 3 4 5
  """

  @print_before
  def numeric_hollow_pyramid(self, n):
    for row in range(n):
      temp = ""
      for space in range(n - row):
        temp += " "
      for number in range(row + 1):
        if number == 0 or number == row or row == n - 1:
          temp += str(number + 1) + " "
        else:
          temp += "  "
      print(temp, end="")
      print()

  """
          1
        2 3 2
      3 4 5 4 3
    4 5 6 7 6 5 4
  5 6 7 8 9 8 7 6 5
  """

  @print_before
  def numeric_full_pyramid(self, n):
    for row in range(n):
      temp = ""
      for space in range(2 * (n - row - 1)):
        temp += " "
      for number in range(row + 1):
        temp += str(row + number + 1) + " "
      for number in range(row):
        temp += str(2 * row - number) + " "
      print(temp, end="")
      print()
