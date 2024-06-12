class Complexity:

  def time_complexity(self):
    """
    k means processing in a function.
    
    T(n) = k + T(n-1)
    .................
    T(1) = k + T(0)

    T(n) = nk +k1
    complexity = O(n)
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def printArray(a):
      if len(a) == 0:
        return
      print(f"{a[0]}")
      printArray(a[1:])

    printArray(a)

  def space_complexity(self):
    """
    O(n)
    """
