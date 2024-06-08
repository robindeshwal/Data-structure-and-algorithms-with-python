class Practice:

  def __init__(self):
    pass

  def reverse_string(self):
    name = "robin"

    def convert_to_list(name):
      n = len(name)
      s = 0
      e = n - 1
      temp = list(name)
      while (s < e):
        temp[s], temp[e] = temp[e], temp[s]
        s += 1
        e -= 1
      name = "".join(temp)
      return name

    def list_slicing(name):
      return name[::-1]

    print(list_slicing(name))

  def replace_all_spaces(self):
    string = "my name is robin."

    def algo(string):
      temp = list(string)
      for i in range(len(temp)):
        if temp[i] == " ":
          temp[i] = '@'
      string = "".join(temp)
      return string

    def replace_method(string):
      return string.replace(" ", "@")

    print(replace_method(string))

  def palindrome(self):
    string = "noeon"

    def algo(string):
      temp = list(string)
      s = 0
      e = len(temp) - 1

      while (s < e):
        if temp[s] != temp[e]:
          return False
        s += 1
        e -= 1
      return True

    print(algo(string))

  def convert_to_uppar(self):
    string = "robin"

    def algo(string):
      temp = list(string)
      n = len(temp)
      for i in range(n):
        if temp[i] != " ":
          temp[i] = chr(ord(temp[i]) - ord('a') + ord('A'))
        else:
          temp[i] = " "

      return "".join(temp)

    print(algo(string))

  def compare_strings(string):
    a = 'robin'
    b = 'rahul'

    def algo(a, b):
      if len(a) != len(b):
        return False
      for i in range(len(a)):
        if a[i] != b[i]:
          return False
      return True

    print(algo(a, b))

  def replace_string(string):
    string = "this is my message."
    word = "robin"
