from bs_tree import BSTree, Node as TreeNode
import sys

bst = BSTree()


class Questions:

  def inorder_predecessor(self, root, p):
    """
    i/p: root
    inorder: [1,2,3,4,5,6,7,8,9]
    """
    # add your logic here
    if not root or not p:
      return None
    pred = None
    curr = root

    while curr:
      if curr.data < p.data:
        pred = curr
        curr = curr.right
      else:
        curr = curr.left

    return pred

  def inorder_successor(self, root, x):
    """
    Inorder successor and predecessor.
    """
    # Code here
    if not root or not x:
      return None

    succ = None
    curr = root

    while curr:
      if curr.data > x.data:
        succ = curr
        curr = curr.left
      else:
        curr = curr.right

    return succ

  def build_bst_using_preorder(self, preorder):
    """
    1008: Leetcode -> Construct Binary Search Tree from Preorder Traversal
    """

    def build(i, min, max, arr):
      if i[0] >= len(arr):
        return None

      root = None
      if arr[i[0]] > min and arr[i[0]] < max:
        root = TreeNode(arr[i[0]])
        i[0] += 1
        root.left = build(i, min, root.data, arr)
        root.right = build(i, root.data, max, arr)

      return root

    min = -sys.maxsize - 1
    max = sys.maxsize

    return build([0], min, max, preorder)

  def brothers_different_roots(self, root1, root2, x):
    """
    GFG: Count pairs from two BST, who sum is equal to given x.

    Approch: using stack.
    """
    #code here.
    ans = 0
    s1 = []
    s2 = []

    a = root1
    b = root2

    while True:
      while a:
        # inorder
        s1.append(a)
        a = a.left

      while b:
        # reverse inorder
        s2.append(b)
        b = b.right

      if not s1 or not s2:
        break

      atop = s1[-1]
      btop = s2[-1]

      sum = atop.data + btop.data

      if sum == x:
        ans += 1
        s1.pop()
        s2.pop()
        a = atop.right
        b = btop.left
      elif sum < x:
        s1.pop()
        a = atop.right
      else:
        s2.pop()
        b = btop.left

    return ans

  def median_of_bst(self, root):
    """
    GFG: Median of BST
  
    Using morris traversal.
    """

    def find_median(root, n):
      i = 0
      odd1 = (n + 1) // 2
      odd1Val = -1
      even1 = (n // 2)
      even1Val = -1
      even2 = (n // 2) + 1
      even2Val = -1

      curr = root

      while curr:
        # left node is Null, then visited it and go right.
        if curr.left == None:
          i += 1
          if i == odd1:
            odd1Val = curr.data
          if i == even1:
            even1Val = curr.data
          if i == even2:
            even2Val = curr.data
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
            i += 1
            if i == odd1:
              odd1Val = curr.data
            if i == even1:
              even1Val = curr.data
            if i == even2:
              even2Val = curr.data
            curr = curr.right

      median = 0
      if n & 1:
        # odd
        median = odd1Val
      else:
        # even
        median = (even1Val + even2Val) / 2
      return int(median) if median - int(median) == 0.0 else median

    n = len(bst.morris_traversal(root))
    return find_median(root, n)

  def check_dead_end(self, root):
    """
    GFG: Check whether BST contains Dead End
    """

    def solve(root, mp, ans):
      if not root:
        return

      mp[root.data] = 1
      if not root.left and not root.right:
        xp1 = root.data + 1
        xm1 = root.data - 1 if root.data - 1 != 0 else root.data
        if xp1 in mp and xm1 in mp:
          ans[0] = True
        return

      solve(root.left, mp, ans)
      solve(root.right, mp, ans)

    # Code here
    ans = [False]
    visited = {}
    solve(root, visited, ans)
    return ans[0]

  def range_sum(self, root, low, high):
    """
    938: Leetcode -> Range Sum of BST
    """

    def solve(root, sum):
      if not root:
        return

      if low <= root.val <= high:
        sum[0] += root.val

      if root.val > low:
        solve(root.left, sum)

      if root.val < high:
        solve(root.right, sum)

      return sum

    sum = [0]
    solve(root, sum)
    return sum[0]

  def flatten_bst_LL(self):
    """
    GFG: Flatten BST to sorted Linked list.
    """

    def inorder(root, prev):
      if not root:
        return
      inorder(root.left, prev)
      prev.left = None
      prev.right = root
      prev = root
      inorder(root.right, prev)

    def solve(root):
      dummy = TreeNode(-1)
      prev = dummy

      inorder(root, prev)
      prev.left = prev.right = None
      root = dummy.right
      return root

  def flatten_bst_LL_d(self):
    """
    GFG: Flatten BST to sorted Linked list decressin order.
    """

  def replace_least_greater(self, arr):
    """
    GFG: Replace every element with the least greater element on its right.
    """

    def insert(root, val, succ):
      if not root:
        return TreeNode(val)

      if val >= root.data:
        root.right = insert(root.right, val, succ)
      else:
        succ[0] = root.data
        root.left = insert(root.left, val, succ)

      return root

    # code here
    n = len(arr)
    ans = [-1] * n

    root = None

    for i in range(n - 1, -1, -1):
      succ = [-1]
      root = insert(root, arr[i], succ)
      ans[i] = succ[0]

    return ans

  def valid_bst_preorder(self, A):
    """
    interview bit -> valid BST from preorder.
    """

    def helper(i, min_val, max_val, A):
      if i[0] >= len(A):
        return True

      if A[i[0]] > min_val and A[i[0]] < max_val:
        rootData = A[i[0]]
        i[0] += 1
        left_valid = helper(i, min_val, rootData, A)
        right_valid = helper(i, rootData, max_val, A)
        return left_valid and right_valid
      else:
        return False

    min_val = -sys.maxsize - 1
    max_val = sys.maxsize

    i = [0]
    return 1 if helper(i, min_val, max_val, A) else 0

  def merge_two_bst(self, root1, root2):
    """
    GFG: Merge two BST's

    method 1: inorder for both and then merge the arrays. and create bst again.

    method 2: inorder traversal using stack, and keeping two pointer and merger
    and make BST.
    """
    ans = []
    sa = []
    sb = []

    a = root1
    b = root2

    while a or b or sa or sb:
      while a:
        sa.append(a)
        a = a.left

      while b:
        sb.append(b)
        b = b.left

      if not sb or (sa and sa[-1].data <= sb[-1].data):
        atop = sa.pop()
        ans.append(atop.data)
        a = atop.right
      else:
        btop = sb.pop()
        ans.append(btop.data)
        b = btop.right

    return ans
