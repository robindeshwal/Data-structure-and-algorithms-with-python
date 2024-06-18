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
