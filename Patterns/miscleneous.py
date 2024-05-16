from lib.decorator import print_before


class Miscleneous:

  def __init__(self):
    print("==== Miscleneous patterns examples ====")

  """
  1
  2*2
  3*3*3
  4*4*4*4
  4*4*4*4
  3*3*3
  2*2
  1
  """

  @print_before
  def fancy_pattern(self, n):
    for row in range(n):
      temp = ""
      for col in range(2 * row + 1):
        if col % 2 == 0:
          temp += str(row + 1)
        else:
          temp += "*"
      print(temp, end="")
      print()

    for row in range(n):
      temp = ""
      for col in range(2 * (n - row) - 1):
        if col % 2 == 0:
          temp += str(n - row)
        else:
          temp += "*"
      print(temp, end="")
      print()

  """
  1
  2 3
  4 5 6
  7 8 9 10
  11 12 13 14 15
  16 17 18 19 20 21
  """

  @print_before
  def floyds_triangle_pattern(self, n):
    pass

  """
  1
  1 1
  1 2 1
  1 3 3 1
  1 4 6 4 1
  1 5 10 10 5 1
  """

  @print_before
  def pascals_triangle_pattern(self, n):
    pass
