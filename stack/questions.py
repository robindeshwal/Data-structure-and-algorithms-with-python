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

  def largest_rectangle_histogram(self, heights=[2, 1, 5, 6, 2, 3]):
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

  def minimum_bracket_reversal(self):
    """
    GFG: Count the Reversals.
    """

    def pairing(ch1, ch2):
      if ch1 == ch2:
        return 1
      else:
        return 2

    s = "}{{}}{{{"
    # your code here
    if len(s) % 2 != 0:
      return -1

    #  remove valid pairs.
    stack = list()
    for i in range(len(s)):
      ch = s[i]
      if ch == '{':
        stack.append(ch)
      else:
        if len(stack) != 0 and stack[-1] == '{':
          stack.pop()
        else:
          stack.append(ch)

    count = 0
    while len(stack) != 0:
      ch1 = stack.pop()
      ch2 = stack.pop()

      count += pairing(ch1, ch2)

    return count

  def next_greater_in_ll(self):
    """
    1019: leetcode ->  Next greater element in linked list.
    """

    def solve(head):
      if not head:
        return []
      if not head.next:
        return [head.val]

      ll = list()
      while head:
        ll.append(head.val)
        head = head.next

      n = len(ll)
      result = [0] * n

      stack = list()

      for i in range(n):
        while len(stack) != 0 and ll[i] > ll[stack[-1]]:
          kids = stack[-1]
          stack.pop()
          result[kids] = ll[i]
        stack.append(i)

      return result

    solve(head)

  def celebrity_problem(self):
    """
    GFG: The Celebrity Problem.
    """
    # code here
    stack = list()

    # step 1: push all persons in stack.
    for i in range(n):
      stack.append(i)

    #  step 2: discard method to get might be celebrity.
    while len(stack) != 1:
      a = stack.pop()
      b = stack.pop()

      if M[a][b]:
        #  a is not celebrity, b might be
        stack.append(b)
      else:
        stack.append(a)

    #  step 3: check that single person is actually celebrity.
    mightBeC = stack.pop()

    # celebrity should not know anyone.
    for i in range(n):
      if M[mightBeC][i] != 0:
        return -1

    # every body should know celebrity.
    for i in range(n):
      if M[i][mightBeC] == 0 and i != mightBeC:
        return -1

    return mightBeC

  def online_stack_span(self):
    """
    901: Leetcode -> online stock span
    """

    def __init__(self):
      self.stock = []
      self.stack = list()

    def next(self, price):
      self.stock.append(price)
      span = 1
      while self.stack and self.stack[-1][0] <= price:
        span += self.stack[-1][1]
        self.stack.pop()

      pair = (price, span)
      self.stack.append(pair)

      return span

  def simplify_span(self):
    """
    71: Leetcode
    """

    def buildAns(st):
      if not st:
        return ""
      minPath = st.pop()
      ans = buildAns(st)

      return ans + minPath

    def simplifyPath(self, path):
      st = list()
      length = len(path)

      i = 0
      while i < length:
        start = i
        end = i + 1
        while end < length and path[end] != '/':
          end += 1

        minPath = path[start:end]
        i = end
        if minPath == "/" or minPath == "/.":
          continue
        if minPath != "/..":
          st.append(minPath)
        elif st:
          st.pop()

      ans = "/" if not st else ""

      ans += buildAns(st)
      return ans

  def word_is_valid(self):
    """
    1003: Leetcode -> Check If Word Is Valid After Substitutions
    """
    s = "aabcbc"

    if s[0] != 'a':
      return False

    stack = list()
    for i in range(len(s)):
      ch = s[i]
      if ch == "a":
        stack.append(ch)
      elif ch == "b":
        if stack and stack[-1] == 'a':
          stack.append(ch)
        else:
          return False
      else:
        if stack and stack[-1] == "b":
          stack.pop()
          if stack and stack[-1] == "a":
            stack.pop()
          else:
            return False
        else:
          return False
    return len(stack) == 0

  def decode_string(self):
    """
    394: Leetcode -> Decode String.
    """
    stack = list()
    n = len(s)

    for i in range(n):
      ch = s[i]
      if ch == ']':
        strtoRepeat = ""
        while stack and not stack[-1].isdigit():
          temp_pop = stack.pop()
          strtoRepeat += temp_pop if temp_pop != '[' else ''
        numric = ""
        while stack and stack[-1].isdigit():
          numric += stack.pop()
        rev_numric = int(numric[::-1])

        #  final decoding
        curr = strtoRepeat * rev_numric
        stack.append(curr)
      else:
        stack.append(str(ch))

    ans = ""
    while stack:
      ans += stack.pop()

    return ans[::-1]

  def max_ractangle_binary_matrix(self):
    """
    IMP
    85: Leetcode -> Maximal Rectangle
    """
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

    n = len(matrix)
    m = len(matrix[0])

    int_matrix = []
    for i in range(n):
      temp = []
      for j in range(m):
        temp.append(int(matrix[i][j]))

      int_matrix.append(temp)

    area = self.largest_rectangle_histogram(int_matrix[0])
    for i in range(1, n):
      for j in range(m):
        # update curr row with previous values.
        if int_matrix[i][j]:
          int_matrix[i][j] += int_matrix[i - 1][j]
        else:
          int_matrix[i][j] = 0

      area = max(area, self.largest_rectangle_histogram(int_matrix[i]))

    return area

  def car_fleet(self):
    """
    853: Leetcode -> Car Fleet
    """
