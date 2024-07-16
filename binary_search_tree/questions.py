from bs_tree import Node
import sys


class Questions:

  def height(self):
    """
    same logic of tree.
    """

  def diameter(self):
    """
    same logic of tree.
    """

  def validate_bst(self, root):
    """
    98: Leetcode -> Validate Binary Search Tree
    """

    def solve(root, lb, ub):
      # base case
      if not root:
        return True

      if root.val <= lb or root.val >= ub:
        return False

      left = solve(root.left, lb, root.val)
      right = solve(root.right, root.val, ub)

      return left and right

    lb = -sys.maxsize - 1
    ub = sys.maxsize

    return solve(root, lb, ub)

  def lca(self):
    """
    235: Leetcode -> Lowest Common Ancestor of a Binary Search Tree
    """

    def solve(root, p, q):
      if not root:
        return root

      if p.val < root.val and q.val < root.val:
        return solve(root.left, p, q)

      if p.val > root.val and q.val > root.val:
        return solve(root.right, p, q)

      return root

  def k_smallest_element(self, root, k):
    """
    230: Leetcode -> Kth Smallest Element in a BST
    """

    def solve(root, k):
      if not root:
        return -1

      left = solve(root.left, k)

      if left != -1:
        return left

      k[0] -= 1
      if k[0] == 0:
        k[0] = root.val
        return

      right = solve(root.right, k)

      return right

    k = [k]
    solve(root, k)
    return k[0]

  def bst_using_inorder(self, nums):
    """
    108: Leetcode -> Convert Sorted Array to Binary Search Tree
    i/p: [10, 20, 30, 40, 50, 60, 70, 80]
    """

    def solve(nums, s, e):
      if s > e:
        return

      mid = s + (e - s) // 2

      root = Node(nums[mid])

      root.left = solve(nums, s, mid - 1)
      root.right = solve(nums, mid + 1, e)

      return root

    start = 0
    end = len(nums) - 1

    return solve(nums, start, end)

  def bst_into_balanced_bst(self, root):
    """
    1382: Leetcode -> Balance a Binary Search Tree
    """

    def inorder(root, temp):
      if not root:
        return temp

      inorder(root.left, temp)

      temp.append(root.val)

      inorder(root.right, temp)

      return temp

    def solve(nums, s, e):
      if s > e:
        return

      mid = s + (e - s) // 2

      root = Node(nums[mid])

      root.left = solve(nums, s, mid - 1)
      root.right = solve(nums, mid + 1, e)

      return root

    arr = []
    inorder(root, arr)

    start = 0
    end = len(arr) - 1

    return solve(arr, start, end)

  def two_sum(self, root, k):
    """
    653: Leetcode -> Two Sum IV - Input is a BST
    """

    def inorder(root, arr):
      if not root:
        return arr

      inorder(root.left, arr)

      arr.append(root.val)

      inorder(root.right, arr)

      return arr

    arr = []
    arr = inorder(root, arr)

    s = 0
    e = len(arr) - 1

    while s < e:
      sum = arr[s] + arr[e]

      if sum == k:
        return True

      if sum < k:
        s += 1
      else:
        e -= 1

    return False

  def bst_into_DLL(self, root):
    """
    Leetcode -> convert Binary search tree to Doubly Linked list.
    """

    def solve(root, head):
      # base case
      if not root:
        return

      # right subtree into LL.
      solve(root.right, head)

      # attach root node.
      root.right = head

      if head:
        head.left = root

      # update head
      head = root

      #  left subtree ll.
      solve(root.left, head)

    head = None
    solve(root, head)
    return head

  def DLL_to_bst(self):
    """
    """

    def solve(head, n):
      # base case
      if n <= 0 or not head:
        return None

      leftSubtree = solve(head, (n // 2) - 1)

      root = head
      root.left = leftSubtree

      head = head.right

      # right part
      root.right = solve(head, n // 2)
      return root

  def largest_bst(self, root):
    """
    GFG: Largest BST in Binary tree.

    create -> (size, maxVal, minVal, validBST)
    """

    def solve(root, ans):
      # base case
      if not root:
        return (0, -sys.maxsize - 1, sys.maxsize, True)

      # left ans
      leftAns = solve(root.left, ans)
      rightAns = solve(root.right, ans)

      # checking curr node ans
      size = leftAns[0] + rightAns[0] + 1
      maxVal = max(root.data, rightAns[1])
      minVal = min(root.data, leftAns[2])

      if leftAns[3] and rightAns[3] and \
          (root.data > leftAns[1] and root.data < rightAns[2]):
        validBST = True
      else:
        validBST = False

      currNode = (size, maxVal, minVal, validBST)

      if validBST:
        ans[0] = max(ans[0], size)

      return currNode

    ans = [0]
    solve(root, ans)

    return ans[0]
