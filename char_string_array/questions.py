class Questions:

  def __init__(self) -> None:
    pass

  def remove_adjacents(self):
    """
    str = "abbaca"
    output = "ca".
    """
    str = "abbaca"

    temp = []
    for i in range(len(str)):
      if temp and str[i] == temp[-1]:
        temp.pop()
      else:
        temp.append(str[i])

    return "".join(temp)

  def remove_occurrences_substring(self):
    """
    Remove All Occurrences of a Substring
    s = "daabcbaabcbc"
    part = "abc"
    """
    s = "daabcbaabcbc"
    part = "abc"

    def simple_find_replace(s, part):
      pos = s.find(part)
      while pos >= 0:
        s = s.replace(part, "", 1)
        pos = s.find(part)
        print(pos, s, part)
      return s

    print(simple_find_replace(s, part))

  def minimuTime_difference(self):
    """
    """
    timePoints = ["00:00", "23:59", "00:00"]

    temp = []
    for i in range(len(timePoints)):
      currentTime = timePoints[i].split(":")
      hours = currentTime[0]
      mintues = currentTime[1]
      totalMintues = int(hours) * 60 + int(mintues)
      temp.append(totalMintues)

    temp.sort()

    mini = 2**31
    for i in range(len(temp) - 1):
      diff = temp[i + 1] - temp[i]
      mini = min(mini, diff)

    lastDiff1 = (temp[0] + 1440) - temp[-1]
    lastDiff2 = temp[-1] - temp[0]
    lastDiff = min(lastDiff1, lastDiff2)

    mini = min(mini, lastDiff)

    return mini

  def substrings(self):
    """
    str = abc
    substr = "a", "ab" , "abc", "b", "bc", "c"
    """
    str = "abc"

    def print_substring(str):
      result = []
      for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
          temp = str[i:j]
          result.append(temp)

      return result

    print(print_substring(str))

  def palindromic_substrings(self):
    """
    """
    str = "aaa"

    def palindrome(str):
      i = 0
      j = len(str) - 1
      while (i <= j):
        if str[i] != str[j]:
          return False
        i += 1
        j -= 1
      return True

    """
    Complexity: O(n3)
    """

    def all_substring(str):
      result = set()
      for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
          temp = str[i:j]
          if palindrome(temp):
            result.add(temp)

      return result

    print(all_substring(str))
    """
    Complexity: O(n2)
    """
    count = 0

    def search(s, i, j):
      count = 0
      while 0 <= i and j < len(s):
        if s[i] == s[j]:
          count += 1
        else:
          break
        i -= 1
        j += 1
      return count

    for i in range(len(str)):
      # odd search
      count = count + search(str, i, i)

      # even search
      count = count + search(str, i, i + 1)

    return count

  def valid_anagrams(self):
    """
    valid anagrams - 242 Leetcode.
    """
    s = "anagram"
    t = "nagaram"

    def algo(s, t):
      temp = list(0 for i in range(256))
      for i in range(len(s)):
        temp[ord(s[i])] += 1

      for i in range(len(t)):
        temp[ord(t[i])] -= 1

      for i in range(256):
        if temp[i] != 0:
          return False
      return True

    print(algo(s, t))

  def reverse_only_letters(self):
    """
    reverse only letters - 917
    """
    s = "Test1ng-Leet=code-Q!"

    def isEnglishLetter(letter):
      if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
        return True
      return False

    start = 0
    end = len(s) - 1
    temp = list(s)

    while (start <= end):
      if not isEnglishLetter(temp[start]):
        start += 1
      elif not isEnglishLetter(temp[end]):
        end -= 1
      else:
        temp[start], temp[end] = temp[end], temp[start]
        start += 1
        end -= 1
    return "".join(temp)

  def longest_common_prefix(self):
    """
    longest common prefix - 14
    """
    """
    reverse vowels of a string - 345
    """
    """
    Isomorphic string.
    """
    """
    reorganise string.
    """
    """
    Group Anagrams.
    """
    """
    Longest palindromic substring.
    """
    """
    find index of first occurance in a string
    """
    """
    string compression.
    """
    """
    string to integer.
    """
    """
    integer to roman.
    """
    """
    Zig-zag conversion.
    """
    """
    largest number - 179 leetcode
    """
    """
    custom sort string - 791
    """
    """
    verify alien dictionary. - 953
    """
    """
    longest word in dictionary through deleting - 524
    """
