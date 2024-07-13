from collections import deque


class Questions:

  def diameter(self, root):
    """
    543: Leetcode -> Diameter of Binary Tree
    fast way to find diameter.
    """

    def height(root, D):
      if not root:
        return 0

      lh = height(root.left, D)
      rh = height(root.right, D)

      currD = lh + rh
      D[0] = max(D[0], currD)

      return max(lh, rh) + 1

    Diameter = [0]
    height(root, Diameter)
    return Diameter[0]

  def height_balanced_tree(self, root):
    """
    110: Balanced Binary Tree.
    """

    def height(root, isBalanced):
      if not root:
        return 0

      lh = height(root.left, isBalanced)
      rh = height(root.right, isBalanced)

      # check for current node, is it balanced?
      if isBalanced[0] and abs(lh - rh) > 1:
        isBalanced[0] = False

      return max(lh, rh) + 1

    isBalanced = [True]
    height(root, isBalanced)
    return isBalanced[0]

  def tree_identical(self, p, q):
    """
    100: Leetcode -> is tree identical?
    """
    if not p and not q:
      return True

    if p and q:
      return ((p.val == q.val) and self.tree_identical(p.left, q.left)
              and self.tree_identical(p.right, q.right))

    return False

  def symmetric_tree(self, root):
    """
    101: Symmetric tree (mirror of itself.)
    """

    def isMirror(p, q):
      if not p and not q:
        return True

      if p and q:
        return ((p.val == q.val) and isMirror(p.left, q.right)
                and isMirror(p.right, q.left))

      return False

    if not root:
      return True

    if not root.left and not root.right:
      return True

    return isMirror(root.left, root.right)

  def diagonal_traversal(self, root):
    """
    GFG: diagonal traversal  
    """
    #code here
    ans = []

    if not root:
      return ans

    q = deque()
    q.append(root)

    while q:
      temp = q.popleft()

      while temp:
        ans.append(temp.data)
        if temp.left:
          # will check leter
          q.append(temp.left)
        temp = temp.right

    return ans

  def zig_zag_traversal(self, root):
    """
    103: Leetcode -> Binary Tree Zig Zag Level order tranversal.
    """

    def solve(root, result):

      if not root:
        return

      q = deque()
      q.append(root)
      q.append(None)

      LtoR = True
      temp = []
      while q:
        element = q.popleft()

        if element == None:
          if q:
            if not LtoR:
              temp = temp[::-1]
            result.append(temp)
            q.append(None)
            temp = []
            LtoR = not LtoR
        else:
          temp.append(element.val)

          if element.left:
            q.append(element.left)

          if element.right:
            q.append(element.right)

      if temp:
        if not LtoR:
          temp.reverse()
        result.append(temp)

      return result

    result = []
    solve(root, result)
    return result

  def vertical_order_traversal(self, root):
    """
    V. IMP
    987: Leetcode -> 
    we can use heap queue as well to solve this questions.
    """

    def solve(root, mapping):

      q = deque()
      q.append((root, 0, 0))

      while q:
        front = q.popleft()
        node = front[0]
        row = front[1]
        col = front[2]

        if node:
          if col not in mapping:
            mapping[col] = []
          mapping[col].append((row, node.val))

          if node.left:
            q.append((node.left, row + 1, col - 1))

          if node.right:
            q.append((node.right, row + 1, col + 1))

    mapping = {}
    solve(root, mapping)
    sorted_keys = sorted(mapping.keys())

    result = []
    for col in sorted_keys:
      column_nodes = sorted(mapping[col], key=lambda x: (x[0], x[1]))
      result.append([val for key, val in column_nodes])
    return result

  def k_sum_paths(self, root):
    """
    437: Leetcode -> Path Sum III
    """

    def solve(self, root, ans, sum):
      if not root:
        return

      if sum == root.val:
        ans[0] += 1

      self.solve(root.left, ans, sum - root.val)
      self.solve(root.right, ans, sum - root.val)

    def pathSum(self, root, targetSum):

      if not root:
        return 0

      ans = [0]

      self.solve(root, ans, targetSum)
      ls = self.pathSum(root.left, targetSum)
      rs = self.pathSum(root.right, targetSum)

      return ans[0] + ls + rs

  def flatten_bt_into_ll(self, root):
    """
    114: Leetcode -> Flatten Binary Tree to Linked List
    """
    if not root:
      return

    curr = root
    while curr:

      if curr.left:
        pred = curr.left
        while pred.right:
          pred = pred.right

        pred.right = curr.right
        curr.right = curr.left
        curr.left = None

      curr = curr.right

    return root

  def maximum_sum_of_non_adjacent(self):
    """
    Need practice.
    GFG: Maximum sum of Non-adjacent nodes.
    """

    def helper(self, root):
      if not root:
        return (0, 0)

      left = self.helper(root.left)
      right = self.helper(root.right)

      # sum
      a = root.data + left[1] + right[1]
      b = max(left[0], left[1]) + max(right[0], right[1])

      return (a, b)

    def getMaxSum(self, root):
      #code here
      ans = self.helper(root)

      return max(ans[0], ans[1])

  def longest_bloodline(self, root):
    """
    GFG: Sum of nodes on the longest path from root to leaf node.
    sum of the longest bloodline of a tree.
    """

    def height(root):
      if not root:
        return (0, 0)

      lh = height(root.left)
      rh = height(root.right)

      sum = root.data
      if lh[0] == rh[0]:
        sum += lh[1] if lh[1] > rh[1] else rh[1]
      elif lh[0] > rh[0]:
        sum += lh[1]
      else:
        sum += rh[1]

      return (max(lh[0], rh[0]) + 1, sum)

    h = height(root)
    return h[1]

  def burning_tree(self, root, target):
    """
    GFG: Burning Tree
    """

    def findTargetNode(root, pm, target):
      if not root:
        return

      # level order traversal.
      q = deque()
      targetNode = None
      q.append(root)
      pm[root] = None

      while q:
        front = q.popleft()

        if front.data == target:
          targetNode = front

        if front.left:
          q.append(front.left)
          pm[front.left] = front

        if front.right:
          q.append(front.right)
          pm[front.right] = front

      return targetNode

    def burnTree(targetNode, pm):
      visited = {}

      q = deque()  # currently set on fire nodes.

      T = 0
      q.append(targetNode)
      visited[targetNode] = 1

      while q:
        size = len(q)
        isFireSpreaded = False
        for i in range(size):
          front = q.popleft()
          if front.left and front.left not in visited:
            q.append(front.left)
            visited[front.left] = 1
            isFireSpreaded = True

          if front.right and front.right not in visited:
            q.append(front.right)
            visited[front.right] = 1
            isFireSpreaded = True

          if pm[front] and pm[front] not in visited:
            q.append(pm[front])
            visited[pm[front]] = 1
            isFireSpreaded = True

        if isFireSpreaded:
          T += 1

      return T

    # code here
    parent_map = {}
    targetNode = findTargetNode(root, parent_map, target)
    return burnTree(targetNode, parent_map)

  def duplicate_subtrees(self, root):
    """
    652: Leetcode -> find duplicate subtrees.
    """

    def solve(root, ans, mapping):
      if not root:
        return "N"

      curr = str(root.val)
      ls = solve(root.left, ans, mapping)
      rs = solve(root.right, ans, mapping)

      string = curr + "," + ls + "," + rs

      if string in mapping:
        if mapping[string] == 1:
          ans.append(root)
        mapping[string] += 1
      else:
        mapping[string] = 1

      return string

    ans = []
    mapping = {}
    solve(root, ans, mapping)
    return ans
