class UniqueElement:
  """
  find unique element from a array.
  """

  def __init__(self) -> None:
    print('==== Unique element ====')

  #brute force solution
  def unique_element_BF(self, arr):
    length = len(arr)
    for i in range(length):
      exists = False
      for j in range(i + 1, length):
        if arr[i] == arr[j]:
          exists = True
          break
        else:
          exists = False
      if not exists:
        print(f"unique: {i}")
        break

  # by using XOR oprator.
  def unique_element_BF2(self, arr):
    ans = 0
    print(arr)
    for i in range(0, len(arr)):
      ans = ans ^ arr[i]
    print(ans)
