from collections import deque


class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  """
  1. Build tree using level order travesal
  2. using recursively.
  """

  def build_tree_lot(self):
    """
    Level order traversal.
    using queue.
    """
    q = deque()

    root = Node(5)
    q.append(root)
    q.append(None)

    while q:
      temp = q.popleft()

      if temp == None:
        if q:
          q.append(None)

      if temp.left:
        q.append(temp.left)

      if temp.right:
        q.append(temp.right)

    print(q)

  def using_recursion(self):
    """
    create root node
    root -> left == recursion()
    root -> right = recursion()
    """
    data = [90, 20, 11, -1, -1, 13, -1, -1]

    if data == -1:
      return None

    root = Node(data)

    root.left = self.using_recursion()
    root.right = self.using_recursion()

    return root

  def inorder(self, root):
    """
    LNR
    left , current node, right
    root = Node(data), data = 10
    """
    if not root:
      return

    self.inorder(root.left)
    print(root.data)
    self.inorder(root.right)

  def preorder(self, root):
    """
    NLR
    current node, left, right
    root = Node(data)
    """
    if not root:
      return

    print(root.data)
    self.preorder(root.left)
    self.preorder(root.right)

  def postorder(self, root):
    """
    LRN
    left, right, current node
    root = Node(data)
    """
    if not root:
      return

    self.postorder(self.left)
    self.postorder(self.right)
    print(root.data)
