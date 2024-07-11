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
