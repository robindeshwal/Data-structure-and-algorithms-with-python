from tree.tree import Node, Tree
from collections import deque, OrderedDict


class Questions:

  def __init__(self):
    self.tree = Tree()

  def making_tree(self):
    """
    """
    root = self.tree.build_tree()

    self.tree.print_tree_lot(root)

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

  def make_tree_using_inorder_preorder(self, preorder, inorder):
    """
    105: Leetcode -> Construct Binary Tree from Preorder and Inorder Traversal
    i/p: inorder, preorder => make tree.
    """

    def find_position(arr, element):
      for i in range(len(arr)):
        if arr[i] == element:
          return i
      return -1

    def solve(preorder, inorder, size, po_index, io_start, io_end):
      # base case
      if po_index[0] >= size or io_start > io_end:
        return

      # step A:
      element = preorder[po_index[0]]
      po_index[0] += 1

      root = Node(element)

      root_index = find_position(inorder, element)

      # step B: root.left solve
      root.left = solve(preorder, inorder, size, po_index, io_start,
                        root_index - 1)

      # step C: root.right solve
      root.right = solve(preorder, inorder, size, po_index, root_index + 1,
                         io_end)

      return root

    size = len(preorder)
    return solve(preorder, inorder, size, [0], 0, size - 1)

  def make_tree_using_inorder_postorder(self, postorder, inorder):
    """
    106: Leetcode -> Construct Binary Tree from Inorder and Postorder Traversal
    """

    def find_position(arr, element, size):
      for i in range(size):
        if arr[i] == element:
          return i

    def solve(inorder, postorder, size, po_index, io_start, io_end):
      # base case
      if po_index[0] < 0 or io_start > io_end:
        return

      # creating root
      print(po_index[0])
      element = postorder[po_index[0]]
      po_index[0] -= 1

      root = Node(element)

      pos = find_position(inorder, element, size)

      # right
      root.right = solve(inorder, postorder, size, po_index, pos + 1, io_end)

      # left
      root.left = solve(inorder, postorder, size, po_index, io_start, pos - 1)

      return root

    size = len(postorder)
    po_index = [size - 1]
    return solve(inorder, postorder, size, po_index, 0, size - 1)

  def vertical_order_traversal(self):
    """
    987: Leetcode -> Vertical Order Traversal of a Binary Tree
    """

  def zig_zag_traversal(self):
    """
    103: Leetcode -> Binary Tree Zigzag Level Order Traversal
    """

  def top_view(self, root):
    """
    GFG: Top View of Binary Tree
    """
    # code here
    if not root:
      return

    # creating a map for storing HD -> TopNode -> data
    topNode = {}

    # Level Order
    # will store a pair consisting of node and horizontal distance.
    q = deque()

    q.append((root, 0))

    while q:
      temp = q.popleft()

      frontNode = temp[0]
      hd = temp[1]

      # check if ans exists or not in topNode.
      if hd not in topNode:
        topNode[hd] = frontNode.data

      if frontNode.left:
        q.append((frontNode.left, hd - 1))

      if frontNode.right:
        q.append((frontNode.right, hd + 1))

    # ans store in topNode values():
    result = OrderedDict(sorted(topNode.items()))
    # sorted_keys, sorted_values = zip(*sorted(topNode.items()))
    # return list(sorted_values)
    return result.values()

  def bottom_view(self, root):
    """
    GFG: Bottom view of binary tree.
    """
    # code here
    if not root:
      return

    ans = {}

    q = deque()

    q.append((root, 0))

    while q:
      temp = q.popleft()

      frontNode = temp[0]
      hd = temp[1]

      ans[hd] = frontNode.data

      if frontNode.left:
        q.append((frontNode.left, hd - 1))

      if frontNode.right:
        q.append((frontNode.right, hd + 1))

    keys, values = zip(*sorted(ans.items()))

    return values

  def left_view(self, root):
    """
    GFG:
    """

    # code here
    def solve(root, ans, level):
      if not root:
        return

      if level == len(ans):
        ans.append(root.data)

      solve(root.left, ans, level + 1)

      solve(root.right, ans, level + 1)

    ans = []
    solve(root, ans, 0)
    return ans

  def right_view(self, root):
    """
    199: leetcode -> Binary Tree Right Side View
    GFG: right view.
    """

    def solve(root, ans, level):
      if not root:
        return

      if level == len(ans):
        ans.append(root.val)

      # right child call before right view.
      solve(root.right, ans, level + 1)

      solve(root.left, ans, level + 1)

    ans = []
    solve(root, ans, 0)
    return ans

  def boundry_traversal(self, root):
    """
    GFG: Tree Boundary Traversal
    """

    def printLeftNodes(root, ans):
      if not root:
        return

      # if root is a leaf node, return
      if not root.left and not root.right:
        return

      ans.append(root.data)

      if root.left:
        printLeftNodes(root.left, ans)
      else:
        printLeftNodes(root.right, ans)

    def printLeafNodes(root, ans):
      if not root:
        return

      if not root.left and not root.right:
        ans.append(root.data)

      printLeafNodes(root.left, ans)
      printLeafNodes(root.right, ans)

    def printRightNodes(root, ans):
      if not root:
        return

      if not root.left and not root.right:
        return

      if root.right:
        printRightNodes(root.right, ans)
      else:
        printRightNodes(root.left, ans)

      ans.append(root.data)

    # Code here
    if not root:
      return

    if not root.left and not root.right:
      return [root.data]

    ans = []

    printLeftNodes(root.left, ans)

    printLeafNodes(root, ans)

    printRightNodes(root.right, ans)

    return ans
