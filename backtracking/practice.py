class Practice:

  def __init__(self) -> None:
    pass

  def permutations(self):
    """
    string = "abc"
    all permutations of a string: ["abc", "bca", "bac", "cab", "cab", "cba", "acb"]

    time complexity: O(n.n!)
    """

    def solve(string, start):
      if start >= len(string):
        ans.append("".join(string))
        return

      for i in range(start, len(string)):
        string[start], string[i] = string[i], string[start]

        solve(string, start + 1)

        string[start], string[i] = string[i], string[start]

    string = "abc"
    string = list(string)
    ans = []

    solve(string, 0)
    print(ans)

  def rat_in_maze(self):
    """
    find all solutions to reach destination.
    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 1, 1]]
    """

    def isSafe(x, y, row, column, arr, visited):
      if (((x >= 0 and x < row) and (y >= 0 and y < column)) and arr[x][y] == 1
          and visited[x][y] == 0):
        return True
      return False

    def solve(maze, row, column, i, j, visited, output, result):
      #  base case
      if i == row - 1 and j == column - 1:
        result.append(output)
        return

      #  down:  i+1, j
      if isSafe(i + 1, j, row, column, maze, visited):
        visited[i + 1][j] = 1
        solve(maze, row, column, i + 1, j, visited, output + "D", result)
        visited[i + 1][j] = 0

      # left: i, j-1
      if isSafe(i, j - 1, row, column, maze, visited):
        visited[i][j - 1] = 1
        solve(maze, row, column, i, j - 1, visited, output + "L", result)
        visited[i][j - 1] = 0

      # right: i, j+1
      if isSafe(i, j + 1, row, column, maze, visited):
        visited[i][j + 1] = 1
        solve(maze, row, column, i, j + 1, visited, output + "R", result)
        visited[i][j + 1] = 0

      # up: i-1, j
      if isSafe(i - 1, j, row, column, maze, visited):
        visited[i - 1][j] = 1
        solve(maze, row, column, i - 1, j, visited, output + "U", result)
        visited[i - 1][j] = 0

    maze = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
    maze = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]

    if maze[0][0] == 0:
      return []

    row = len(maze)
    column = len(maze[0])

    visited = list(list(0 for i in range(column)) for i in range(row))
    visited[0][0] = 1

    path = []
    result = []

    solve(maze, row, column, 0, 0, visited, "", result)
    print(result)

  def n_queens(self):
    """
    """
    row_check = {}
    uppper_left_diagnol_check = {}
    bottom_left_diagnol_check = {}

    def print_sol(board, n):
      for i in range(n):
        for j in range(n):
          print(board[i][j], end="")
        print()

    def isSafe(row, col, board, n):
      # upper left diagnol
      # left row
      # bottom left diagnol
      i = row
      j = col
      while j >= 0:
        if board[i][j] == 'Q':
          return False
        j -= 1

      i = row
      j = col
      while j >= 0 and i >= 0:
        if board[i][j] == 'Q':
          return False
        i -= 1
        j -= 1

      i = row
      j = col
      while i < n and j >= 0:
        if board[i][j] == 'Q':
          return False
        i += 1
        j -= 1

      return True

    def optimize_isSafe(row, col, board, n):
      """
      """
      if row in row_check and row_check[row] == True:
        return False
      if n-1+col-row in uppper_left_diagnol_check \
        and uppper_left_diagnol_check[n-1+col-row] == True:
        return False
      if row+col in bottom_left_diagnol_check \
        and bottom_left_diagnol_check[row+col] == True:
        return False

      return True

    def optimize_solve(board, col, n):
      if col >= n:
        print_sol(board, n)
        print("\n")
        return

      # try place q on every col.
      for row in range(n):
        if optimize_isSafe(row, col, board, n):
          board[row][col] = 'Q'
          row_check[row] = True
          uppper_left_diagnol_check[n - 1 + col - row] = True
          bottom_left_diagnol_check[row + col] = True

          optimize_solve(board, col + 1, n)

          board[row][col] = '-'
          row_check[row] = False
          uppper_left_diagnol_check[n - 1 + col - row] = False
          bottom_left_diagnol_check[row + col] = False

    def solve(board, col, n):
      if col >= n:
        print_sol(board, n)
        print("\n")
        return

      # try place q on every col.
      for row in range(n):
        if isSafe(row, col, board, n):
          board[row][col] = 'Q'

          solve(board, col + 1, n)

          board[row][col] = '-'

    n = 4
    board = list(list('-' for i in range(n)) for i in range(n))
    col = 0

    optimize_solve(board, col, n)

  def generate_parentheses(self):
    """
    leetcode : 22
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    """

    def solve(ans, n, open, close, output):
      #  base case
      if open == 0 and close == 0:
        ans.append("".join(output))

      #  include open
      if open > 0:
        output.append('(')
        solve(ans, n, open - 1, close, output)
        output.pop()

      # include close
      if close > open:
        output.append(')')
        solve(ans, n, open, close - 1, output)
        output.pop()

    n = 3
    ans = []
    open = n
    close = n

    solve(ans, n, open, close, [])
    return ans

  def phone_keypad_problem(self):
    """
    leetcode: 17
    Letter combinations of a phone number.
    """
    dic = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    def solve(digits, idx, output, ans):
      # base case
      if idx >= len(digits):
        ans.append("".join(output))
        return

      # solve one case
      digit = ord(digits[idx]) - ord("0")
      value = dic[digit]
      for i in range(len(value)):
        ch = value[i]
        output.append(ch)
        solve(digits, idx + 1, output, ans)
        output.pop()

    digits = "23"

    idx = 0
    output = []
    ans = []
    if digits == "":
      return ans

    solve(digits, idx, output, ans)
    print(ans)

  def sudoku_solver(self):
    """
    Do not return anything, modify board in-place instead.
    """

    def isSafe(value, board, curr_row, curr_col):
      # row check
      for col in range(9):
        if board[curr_row][col] == value:
          return False

      # col check
      for row in range(9):
        if board[row][curr_col] == value:
          return False

      #  3*3 box
      for i in range(9):
        # [i][j] = [3*(curr_row//3) + i//3][3*(curr_col//3) + i%3]
        if board[3 * (curr_row // 3) + i // 3][3 * (curr_col // 3) +
                                               i % 3] == value:
          return False
      return True

    def solve(board, n):
      for i in range(n):
        for j in range(n):
          # check available
          if board[i][j] == ".":
            #  loop for inserting value.
            for value in range(1, 10):
              value = str(value)
              if isSafe(value, board, i, j):
                board[i][j] = value
                if solve(board, n):
                  return True
                board[i][j] = "."
            return False
      return True

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    n = len(board)

    solve(board, n)
    print(board)

