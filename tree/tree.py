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

  def build_tree(self):
    """
    create root node
    root -> left == recursion()
    root -> right = recursion()
    data = [90, 20, 11, -1, -1, 13, -1, -1]
    """
    data = int(input("Please enter data: "))

    if data == -1:
      return None

    root = Node(data)

    print(f"Enter the data for left part of {data} node.")
    root.left = self.build_tree()

    print(f"Enter the data for right part of {data} node.")
    root.right = self.build_tree()

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

    self.postorder(root.left)
    self.postorder(root.right)
    print(root.data)

  def level_order_traversal(self, root):
    """
    GFG: Level order traversal.
    """
    # Code here
    q = deque()
    q.append(root)

    ans = []

    while q:
      temp = q.popleft()

      ans.append(temp.data)

      if temp.left:
        q.append(temp.left)

      if temp.right:
        q.append(temp.right)

    return ans

  def morris_traversal(self, root):
    """
    GFG: Morris traversal.
    """
    ans = []
    curr = root

    while curr:
      # left node is Null, then visited it and go right.
      if curr.left == None:
        ans.append(curr.data)
        curr = curr.right
      # left node is not null
      else:
        # find inorder predecessor.
        pred = curr.left
        while pred.right != curr and pred.right:
          pred = pred.right

        # if right node is NUll, then go left after establishing link from pred           to curr.
        if pred.right == None:
          pred.right = curr
          curr = curr.left
        else:
          # left is already visited, go right after visiting curr node,
          pred.right = None
          ans.append(curr.data)
          curr = curr.right
    print(ans)
    return ans

  def print_tree_lot(self, root):
    """
    using queue -> level order traversal.
    for printing level :
    10
    20 40
    30 50 60
    """
    # Code here
    q = deque()

    q.append(root)
    q.append(None)

    ans = ""
    while q:
      temp = q.popleft()

      if temp == None:
        ans += "\n"
        if q:
          q.append(None)
      else:
        ans += str(temp.data) + " "

        if temp.left:
          q.append(temp.left)

        if temp.right:
          q.append(temp.right)

    print(ans)


if __name__ == "__main__":
  tree = Tree()

  root = tree.build_tree()

  print(tree.level_order_traversal(root))

  tree.print_tree_lot(root)
