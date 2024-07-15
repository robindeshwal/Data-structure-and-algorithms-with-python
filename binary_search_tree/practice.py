from .bs_tree import Node, BSTree


class Practice:

  def __init__(self):
    self.bst = BSTree()

  def createBst(self):

    root = None
    print("Enter the data for Node: ")
    root = self.bst.take_input(root)
    print("Printing the tree: ")
    self.bst.print_tree_lot(root)

    print("printing inorder: ")
    self.bst.inorder(root)
    print("Printing preorder: ")
    self.bst.preorder(root)
    print("printing postorder: ")
    self.bst.postorder(root)

  def search(self, root, val):
    """
    700: Leetcode -> Search in a Binary Search Tree
    """
    if not root:
      return root

    if root.val == val:
      return root

    if root.val > val:
      return self.search(root.left, val)
    else:
      return self.search(root.right, val)

  def min_max_in_bst(self):
    """
    GFG: Given a Binary Tree, find maximum and minimum elements in it.
    """

    def findMax(root):
      #code here
      if not root:
        return root

      if not root.right:
        return root.data

      while root.right:
        root = root.right

      return root.data

    def findMin(root):
      #code here
      if not root:
        return root

      if not root.left:
        return root.data

      while root.left:
        root = root.left

      return root.data

  def inorder_predeccessor_or_successor(self):
    """
    """

  def delete_a_node(self):
    """
    450: Leetcode -> Delete Node in a BST
    """

    def maxVal(node):
      while node.right:
        node = node.right
      return node

    def solve(root, key):
      # base case
      if not root:
        return root

      if key < root.val:
        root.left = solve(root.left, key)
      elif key > root.val:
        root.right = solve(root.right, key)
      else:
        # check deletion cases.
        if not root.left and not root.right:
          return None
        elif not root.left and root.right:
          return root.right
        elif root.left and not root.right:
          return root.left
        # both child exists.
        # inorde predecessor of left -> left subtree max value.
        inPre = maxVal(root.left)
        root.val = inPre.val
        root.left = solve(root.left, inPre.val)
      return root
