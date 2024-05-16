class Practice2D:

  def __init__(self) -> None:
    pass

  # Print Row Sum.
  def row_sum(self):
    array_2d = [[1, 2, 3, 4], [2, 3, 4, 1], [5, 6, 1, 3], [2, 4, 6, 8],
                [1, 9, 9, 6]]
    row_len = len(array_2d)
    col_len = len(array_2d[0])
    for row in range(row_len):
      sum = 0
      for col in range(col_len):
        sum += array_2d[row][col]

      print(sum, end=" ")
    print("end")

  def column_sum(self):
    array_2d = [[1, 2, 3, 4], [2, 3, 4, 1], [5, 6, 1, 3], [2, 4, 6, 8],
                [1, 9, 9, 6]]
    row_len = len(array_2d)
    col_len = len(array_2d[0])

    for col in range(col_len):
      sum = 0
      for row in range(row_len):
        sum += array_2d[row][col]

      print(sum, end=" ")

  def linear_search(self):

    def find_key(array, key):
      row_len = len(array)
      col_len = len(array[0])
      isExists = False
      for row in range(row_len):
        for col in range(col_len):
          if array_2d[row][col] == key:
            return True

      return isExists

    array_2d = [[5, 6, 8], [7, 2, 4], [1, 6, 9]]
    k = 4

    print(find_key(array_2d, k))

  # max min
  def max_min_2d_array(self):
    array_2d = [[5, 6, 9], [7, 1, 2], [4, 3, 12]]

    max = -2**31
    min = 2**31 - 1

    for row in range(len(array_2d)):
      for col in range(len(array_2d[0])):
        if array_2d[row][col] > max:
          max = array_2d[row][col]
        if array_2d[row][col] < min:
          min = array_2d[row][col]

    print(f'max: {max} min: {min}')

  def transpose_matrix(self):
    array_2d = [[1, 2, 3, 4], [2, 3, 4, 1], [5, 6, 1, 3], [2, 4, 6, 8],
                [1, 9, 9, 6]]
    row_len = len(array_2d)
    col_len = len(array_2d[0])

    transpose_matrix = []
    for _ in range(col_len):
      temp_list = []
      for _ in range(row_len):
        temp_list.append(-1)
      transpose_matrix.append(temp_list)

    for row in range(row_len):
      for col in range(col_len):
        transpose_matrix[col][row] = array_2d[row][col]

    print(transpose_matrix, end=" ")
