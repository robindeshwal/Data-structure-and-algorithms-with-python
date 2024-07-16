from collections import deque


class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BSTree:

  def __init__(self):
    self.node = None

  def take_input(self, root):
    data = int(input("Enter the input"))

    while (data != -1):
      root = self.insertIntoBst(root, data)
      data = int(input("Enter the input"))

    return root

  def insertIntoBst(self, root, data):
    if not root:
      # this is first node we have to create.
      root = Node(data)
      return root

    # no first node
    if root.data > data:
      root.left = self.insertIntoBst(root.left, data)

    else:
      root.right = self.insertIntoBst(root.right, data)

    return root

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
