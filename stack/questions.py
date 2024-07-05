from stack.stack import Stack


class Questions:

  def valid_parenthesis(self):
    """
    20: leetcode -> valid parenthesis
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    """

    s = "()[]{}"

    st = list()

    for i in range(len(s)):

      #  opening bracker
      if s[i] == '(' or s[i] == '{' or s[i] == '[':
        st.append(s[i])
      else:
        # closing bracket
        if not st:
          return False
        temp = st.pop()
        if s[i] == ')' and temp != '(':
          return False
        elif s[i] == '}' and temp != '{':
          return False
        elif s[i] == ']' and temp != '[':
          return False
    return len(st) == 0

  def sort_stack(self):
    """
    GFG: Sort a Stack.
    Given a stack, the task is to sort it such that the top of the stack has the greatest element.
    """

    def insertSorted(s, target):
      if not len(s):
        s.append(target)
        return

      if s[-1] <= target:
        s.append(target)
        return

      temp = s.pop()

      insertSorted(s, target)

      s.append(temp)

    def Sorted(s):
      # Code here

      if not s:
        return

      temp = s.pop()
      Sorted(s)
      insertSorted(s, temp)

    s = Stack()
    Sorted(s)

  def redundent_brackets(self):
    """
    GfG: remove redundent branckets
    Given a valid expression containing only binary operators '+', '-', '*', '/' and operands, 
    remove all the redundant parenthesis.

    A set of parenthesis is said to be redundant if, removing them, does not change the value of 
    the expression.

    Input:
    Exp = A+(B+(C))
    Output: A+B+C
    """

  def longest_valid_paranthesis(self):
    """
    32: Longest valid paranthesis.
    Given a string containing just the characters '(' and ')', return the length of the 
    longest valid (well-formed) parentheses substring.
    """
    st = list()
    st.append(-1)

    maxLen = 0

    for i in range(len(s)):
      ch = s[i]
      if ch == '(':
        st.append(i)
      else:
        st.pop()
        if len(st) == 0:
          st.append(i)
        else:
          length = i - st[-1]
          maxLen = max(length, maxLen)

    return maxLen

  def next_smaller_element(self):
    """
    find the next smaller element for every element.
    i/p : [2,1,4,3]
    o/p: [1, -1, 3, -1]
    """
    s = Stack()
    s.push(-1)

    li = [2, 1, 4, 3]
    ans = [-1] * len(li)
    for i in range(len(li) - 1, -1, -1):
      curr = li[i]
      while s.top() >= curr:
        s.pop()
      ans[i] = s.top()
      s.push(curr)

    print(ans)

  def previous_smaller_element(self):
    """
    find the previous smaller element for all the elements.
    i/p: [2,1,4, 3]
    o/p: [-1, -1, 1, 1]
    """
    s = Stack()
    s.push(-1)

    li = [2, 1, 4, 3]
    li = [2, 1, 5, 6, 2, 3]
    n = len(li)
    ans = [-1] * n

    for i in range(n):
      curr = li[i]
      while s.top() >= curr:
        s.pop()
      ans[i] = s.top()
      s.push(curr)

    print(ans)

  def largest_rectangle_histogram(self):
    """
    84: Leetcode -> Largest Rectangle in Histogram
    Given an array of integers heights representing the histogram's bar height where the width 
    of each bar is 1, return the area of the largest rectangle in the histogram.
    i/p : [2, 1, 5, 6, 2, 3]
    area = 5*2 = 10
    """

    def previous_smaller_element(li, n):
      """
      find the previous smaller element for all the elements.
      i/p: [2,1,4, 3]
      o/p: [-1, -1, 1, 1]
      """
      s = Stack()
      s.push(-1)

      n = len(li)
      ans = [-1] * n

      for i in range(n):
        curr = li[i]
        while s.top() != -1 and li[s.top()] >= curr:
          s.pop()
        ans[i] = s.top()
        s.push(i)

      return ans

    def next_smaller_element(li, n):
      """
      find the next smaller element for every element.
      i/p : [2,1,4,3]
      o/p: [1, -1, 3, -1]
      """
      n = len(li)

      s = Stack()
      s.push(n)

      ans = [-1] * n
      for i in range(n - 1, -1, -1):
        curr = li[i]
        while s.top() != n and li[s.top()] >= curr:
          s.pop()
        ans[i] = s.top()
        s.push(i)

      return ans

    heights = [2, 1, 5, 6, 2, 3]
    n = len(heights)

    prev = previous_smaller_element(heights, n)
    nxt = next_smaller_element(heights, n)

    maxArea = 0
    for i in range(n):
      length = heights[i]
      width = nxt[i] - prev[i] - 1

      area = length * width
      maxArea = max(maxArea, area)

    return maxArea

  def remove_adjacent(self):
    """
    1047: Remove all adjacent duplicates in string.
    """
    s = "abbaca"
    st = Stack()
    for i in range(len(s)):
      ch = s[i]
      if not st.is_empty() and ch == st.top():
        st.pop()
      else:
        st.push(ch)
    result = ""
    while st.is_empty():
      result += st.pop()
    return result
