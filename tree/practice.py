from tree.tree import Node


class Practice:

  def height(self, root):
    """
    104: Maximum depth of a tree.
    """
    if not root:
      return 0

    leftHeight = self.height(root.left)
    rightHeight = self.height(root.right)

    ans = max(leftHeight, rightHeight) + 1

    return ans

  def diameter(self, root):
    """
    543: Leetcode -> Diameter of Binary Tree
    """

    if not root:
      return 0

    op1 = self.diameter(root.left)
    op2 = self.diameter(root.right)

    op3 = self.height(root.left) + self.height(root.right)

    ans = max(op1, op2, op3)

    return ans

  def same_tree(self, p=Node(10), q=Node(10)):
    """
    100: Leetcode -> same tree.
    """
    if not p and not q:
      return True

    if not p or not q:
      return False

    if p.val != q.val:
      return False

    left = self.same_tree(p.left, q.left)
    right = self.same_tree(p.right, q.right)

    return left and right

  def mirror_tree(self, root):
    """
    226: Leetcode -> Invert Binary Tree
    """
    if not root:
      return

    left = root.left
    right = root.right

    root.left = self.mirror_tree(right)
    root.right = self.mirror_tree(left)

    return root

  def is_balanced(self, root):
    """
    110: Leetcode -> Balanced Binary Tree
    """
    if not root:
      return True

    left = self.height(root.left)
    right = self.height(root.right)

    ans1 = abs(left - right) <= 1

    # recursion
    leftAns = self.is_balanced(root.left)
    rightAns = self.is_balanced(root.right)

    return ans1 and leftAns and rightAns

  def to_sum_tree(self, root):
    """
    GFG : Transfer to sum tree.
    """
    #code here
    if not root:
      return 0

    old_val = root.data

    left = self.to_sum_tree(root.left)
    right = self.to_sum_tree(root.right)

    root.data = left + right  # updated from leaf 8 to 0

    return root.data + old_val

  def lowest_common_ancestor(self, root, p, q):
    """
    236: Leetcode -> Lowest Common Ancestor of a Binary Tree.
    """
    #  base case
    if not root:
      return None

    #  check p or q.
    if root.val == p.val:
      return p
    if root.val == q.val:
      return q

    leftAns = self.lowest_common_ancestor(root.left, p, q)
    rightAns = self.lowest_common_ancestor(root.right, p, q)

    if not leftAns and not rightAns:
      return None

    elif leftAns and not rightAns:
      return leftAns

    elif not leftAns and rightAns:
      return rightAns

    else:
      return root

  def kth_ancestor(self, root, k, node):
    """
    GFG: Kth Ancestor in a Tree.
    """

    #code here
    def solve(root, crnt, val):
      if not root:
        return 0

      if root.data == node:
        return 1

      left = solve(root.left, crnt, val)
      right = solve(root.right, crnt, val)

      if left or right:
        crnt[0] -= 1
        if crnt[0] == 0:
          val[0] = root.data
        return 1
      return 0

    crnt = [k]
    val = [-1]

    solve(root, crnt, val)

    return val[0]

  def path_sum_2(self, root, targetSum):
    """
    113: Leetcode -> Path Sum II
    """

    def solve(root, result, temp, sum):
      # base
      if not root:
        return

      # leef node
      if not root.left and not root.right:
        if sum + root.val == targetSum:
          result.append(temp + [root.val])
        return

      # include current node.
      temp.append(root.val)
      sum += root.val

      solve(root.left, result, temp, sum)
      solve(root.right, result, temp, sum)

      # backtrack
      temp.pop()
      sum -= root.val

    result = []
    solve(root, result, [], 0)

    return result
