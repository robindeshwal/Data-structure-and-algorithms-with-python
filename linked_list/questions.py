from linked_list.singly_linked_list import Node, LinkedList


class Questions:
  """
  """

  def __init__(self):
    self.ll = LinkedList()

  def lengthLL(self, head):
    i = 0
    temp = head
    while temp:
      temp = temp.next
      i += 1
    return i

  def reverse_ll(self, head):
    """
    206: Leetcode
    Reverse a linked list.
    """

    def solve_by_loop(prev, curr):
      while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
      return prev

    def solve_by_recursion(prev, curr):
      # base
      if curr is None:
        return prev

      temp = curr.next
      curr.next = prev

      return solve_by_recursion(curr, temp)

    self.ll.insert(10)
    self.ll.insert(20)
    self.ll.insert(30)
    self.ll.insert(40)
    self.ll.insert(50)
    self.ll.print_ll()

    prev = None
    curr = self.ll.head

    # by recursion:
    self.ll.head = solve_by_recursion(prev, curr)

    # by loop:
    self.ll.head = solve_by_loop(prev, curr)

    print("\nReversed : ")
    self.ll.print_ll()

    return solve_by_loop(None, head)

  def middle_of_ll(self):
    """
    876: Leetcode -> find a middle of linked list.
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.
    """

    def solution():

      def ll_len(head):
        if not head:
          return 0

        i = 0
        currNode = head
        while currNode:
          currNode = currNode.next
          i += 1

        return i

      self.ll.insert(10)
      self.ll.insert(20)
      self.ll.insert(30)
      self.ll.insert(40)
      self.ll.insert(50)

      head = self.ll.head

      length = ll_len(head)
      node_number = length // 2

      i = 1
      currNode = head
      print(node_number)
      while True:
        if i == node_number + 1:
          return currNode
        currNode = currNode.next
        i += 1

    def optimize_solution():
      """
      Two pointer approach.
      Slow and fast pointer.
      Tortoise algorithm.
      """
      self.ll.insert(10)
      self.ll.insert(20)
      self.ll.insert(30)
      self.ll.insert(40)
      self.ll.insert(50)

      head = self.ll.head

      slow = head
      fast = head

      while slow and fast:
        fast = fast.next
        if fast:
          fast = fast.next
          slow = slow.next

      return slow

  def reverse_in_k_groups(self):
    """
    25: Leetcode
    Given the head of a linked list, reverse the nodes of the list k at a time, 
    and return the modified list.
    k is a positive integer and is less than or equal to the length of the linked list.
    If the number of nodes is not a multiple of k then left-out nodes, in the end,
    should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    """

    def ll_length(head):
      currNode = head
      i = 0
      while currNode:
        currNode = currNode.next
        i += 1
      return i

    def solve(head, k):
      if not head:
        return head

      length = ll_length(head)
      if k > length:
        return head

      prev = None
      temp = None
      curr = head
      count = 0

      while count < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count += 1

      if temp is not None:
        head.next = solve(temp, k)

      return prev

    head = [1, 2, 3, 4, 5]
    k = 2
    return solve(head, k)

  def is_circular(self):
    """
    check if linked list is circular.
    """
    self.ll.insert(10)
    self.ll.insert(20)
    self.ll.insert(30)
    self.ll.insert(40)
    self.ll.insert(50)

    head = self.ll.head

    if not head:
      return head

    temp = head.next
    while True:
      if temp == head:
        return 1
      if not temp:
        break
      temp = temp.next
    return 0

  def linked_list_cycle(self):
    """
    Find a loop in a linked list.
    141: leetcode
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    """

    def slow_fast_pointer(head):
      if not head:
        return False

      slow = head
      fast = head

      while fast:
        fast = fast.next
        if fast:
          fast = fast.next
          slow = slow.next

        if slow == fast:
          return True

      return False

  def starting_point_loop_ll(self):
    """
    142: Leetcode -> Find the starting point of a loop in a linked list.
    
    Given the head of a linked list, return the node where the cycle begins. If there is 
    no cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached 
    again by continuously following the next pointer. Internally, pos is used to denote the 
    index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there 
    is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.
    """

    def solve(head):
      """
      steps:
      A: detect a loop , when slow and fast meets.
      B: reassign slow = head.
      C: then slow/fast -> i step on one time -> meeting point will be the (loop starting point)
      
      why??
      
      """
      if not head:
        return head

      slow = head
      fast = head

      isCycle = False
      while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
          isCycle = True
          break

      if isCycle:
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next

        return slow
      return None

  def check_ll_is_palindrome(self):
    """
    234: Leetcode
    check whether your ll is palindrome or not.
    Given the head of a singly linked list, return true if it is a 
    palindrome or false otherwise.

    brute force - reverse ll in temp and the compair both the ll.

    approch#2:  
    """

    def reverseLL(curr):
      prev = None
      while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
      return prev

    def solve(head):
      if not head or not head.next:
        return True

      slow = head
      fast = head

      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

      # reverse ll after middle.
      second_half = reverseLL(slow)

      #  Start comparision.
      first_half = head
      result = True
      while second_half:
        if first_half.val != second_half.val:
          result = False
          break
        first_half = first_half.next
        second_half = second_half.next

      return result

  def remove_duplicates_sorted_ll(self):
    """
    83: Leetcode
    Given the head of a sorted linked list, delete all duplicates such that each element 
    appears only once. Return the linked list sorted as well.
    """

    def solve(head):
      if not head or not head.next:
        return head

      curr = head
      while curr:
        if curr.next and curr.val == curr.next.val:
          temp = curr.next
          curr.next = curr.next.next
          temp.next = None
          del temp
        else:
          curr = curr.next

      return head

  def sort_ll(self):
    """
    GFG
    Sort a linked list of 0s, 1s and 2s
    """

    def solve(head):
      if not head:
        return head

      zeroHead = Node(-1)
      zeroTail = zeroHead

      oneHead = Node(-1)
      oneTail = oneHead

      twoHead = Node(-1)
      twoTail = twoHead

      curr = head
      while curr:
        if curr.data == 0:
          # take out zero node.
          temp = curr
          curr = curr.next
          temp.next = None

          # append zero node in zeroHead
          zeroTail.next = temp
          zeroTail = temp
          del temp

        elif curr.data == 1:
          # take out one node.
          temp = curr
          curr = curr.next
          temp.next = None

          # append one node in zeroHead
          oneTail.next = temp
          oneTail = temp
          del temp

        elif curr.data == 2:
          # take two zero node.
          temp = curr
          curr = curr.next
          temp.next = None

          # append two node in zeroHead
          twoTail.next = temp
          twoTail = temp
          del temp

      # join them

      zeroTail.next = oneHead.next if oneHead.next else twoHead.next
      oneTail.next = twoHead.next
      twoHead.next = None

      # remove dummy node

      return zeroHead.next

  def add_two_numbers(self):
    """
    GFG.
    Add two numbers represented by Linked List.
    """
    #  should be a linked list.
    num1 = Node(0)
    num2 = Node(0)

    rev_num1 = self.reverse_ll(num1)
    rev_num2 = self.reverse_ll(num2)

    carry = 0
    newLL = Node(0)
    newHead = newLL

    while rev_num1 or rev_num2 or carry:
      first = rev_num1.data if rev_num1 else 0
      second = rev_num2.data if rev_num2 else 0

      add = first + second + carry

      newLL.next = Node(add % 10)
      newLL = newLL.next

      carry = add // 10

      if rev_num1:
        rev_num1 = rev_num1.next
      if rev_num2:
        rev_num2 = rev_num2.next

    newHead = self.reverse_ll(newHead)
    return newHead

  def kth_node_from_end(self):
    """
    Hackerrank : Get Node Value
    print kth node from the end.
    """

    def solve(head, pos):
      if not head:
        return 0, None

      index, result = solve(head.next, pos)
      index += 1

      if index == pos + 1:
        result = head.data

      return index, result

    llist = self.ll.head
    positionFromTail = 2

    _, ans = solve(llist, positionFromTail)
    return ans

  def intersection_ll(self):
    """
    160: Leetcode
    Intersection of Two Linked Lists
    """

    def solve(headA, headB):
      a = headA
      b = headB
      while a.next and b.next:
        if a == b:
          return a

        a = a.next
        b = b.next

      if a.next is None:
        # b is big
        blen = 0
        while b.next:
          blen += 1
          b = b.next

        while blen:
          headB = headB.next
          blen -= 1
      else:
        # a is big
        alen = 0
        while a.next:
          alen += 1
          a = a.next

        while alen:
          headA = headA.next
          alen -= 1

      while headA != headB:
        headA = headA.next
        headB = headB.next

      return headA

  def merge_two_ll(self):
    """
    21: Leetcode -> Merge Two Sorted Lists
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together 
    the nodes of the first two lists.

    Return the head of the merged linked list.
    """

    def solve(list1, list2):
      if not list1:
        return list2

      if not list2:
        return list1

      ans = Node(-1)
      mptr = ans

      left = list1
      right = list2

      while left and right:
        if left.val <= right.val:
          mptr.next = left
          left = left.next
        else:
          mptr.next = right
          right = right.next
        mptr = mptr.next

      while left:
        mptr.next = left
        mptr = mptr.next
        left = left.next

      while right:
        mptr.next = right
        mptr = mptr.next
        right = right.next

      return ans.next

  def sort_using_merge_sort(self):
    """
    """

    def find_mid(head):
      slow = head
      fast = head.next

      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

      return slow

    def merge(left, right):
      if not left:
        return right

      if not right:
        return left

      ans = Node(-1)
      mptr = ans

      while left and right:
        if left.val <= right.val:
          mptr.next = left
          left = left.next
        else:
          mptr.next = right
          right = right.next
        mptr = mptr.next

      if left:
        mptr.next = left

      if right:
        mptr.next = right

      return ans.next

    def sortList(head):
      if not head or not head.next:
        return head

      #  break into two halves using mid node.
      mid = find_mid(head)

      left = head
      right = mid.next
      mid.next = None

      left = sortList(left)
      right = sortList(right)

      #  merge both left and right ll.

      mergedLL = merge(left, right)
      return mergedLL

  def flatten_ll(self):
    """
    GFG: Flattening a Linked List
    Given a Linked List of size n, where every node represents a sub-linked-list and contains 
    two pointers:
    (i) a next pointer to the next node,
    (ii) a bottom pointer to a linked list where this node is head.
    Each of the sub-linked-list is in sorted order.
    Flatten the Link List such that all the nodes appear in a single level while maintaining 
    the sorted order.
    """

    def mergeLL(l1, l2):
      if not l1:
        return l2
      if not l2:
        return l1

      ans = None
      if l1.data <= l2.data:
        ans = l1
        ans.bottom = mergeLL(l1.bottom, l2)
      else:
        ans = l2
        ans.bottom = mergeLL(l1, l2.bottom)

      return ans

    def flatten(root):
      #Your code here
      if not root or not root.next:
        return root

      # merging from the last using recursion.
      root.next = flatten(root.next)

      root = mergeLL(root, root.next)

      return root

  def clone_ll(self):
    """
    138: leetcode -> Copy List with Random Pointer.
    """

    def solve_using_map(head, mapping):
      if not head:
        return head

      newHead = Node(head.val)
      mapping[head] = newHead

      newHead.next = solve_using_map(head.next, mapping)

      if head.random:
        newHead.random = mapping[head.random]
      return newHead

    def solve_without_map(head):
      if not head:
        return head

      #  clone A -> A'
      it = head
      while it:
        clonedNode = Node(it.val)
        clonedNode.next = it.next
        it.next = clonedNode
        it = it.next.next

      # Assign random linkes on A' with the help of A.
      # it.next.random = it.random.next

      it = head
      while it:
        clonedNode = it.next
        clonedNode.random = it.random.next if it.random else None

        it = it.next.next

      #  Detach A' and A.
      it = head
      clonedHead = it.next
      result = clonedHead
      while it:
        temp = it.next
        it.next = it.next.next
        if temp.next:
          temp.next = temp.next.next
        clonedHead = temp

        it = it.next

      return result

    head = self.ll.head

    mapping = {}
    return solve_using_map(head, mapping)

  def rotate_list(self):
    """
    61: Leetcode
    Given the head of a linked list, rotate the list to the right by k places.

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

    steps:
    1 -> 2 -> 3 -> 4 -> 5
    5 -> 1 -> 2 -> 3 -> 4
    4 -> 5 -> 1 -> 2 -> 3
    """

    head = self.ll.head
    k = 2

    if not head:
      return head

    length = self.lengthLL(head)
    rotate = k % length
    if rotate == 0:
      return head

    newLastNodePos = length - rotate - 1

    newLastNode = head

    for i in range(newLastNodePos):
      newLastNode = newLastNode.next

    newHead = newLastNode.next
    newLastNode.next = None

    it = newHead
    while it.next:
      it = it.next

    it.next = head

    return newHead

  def delete_n_nodes_after_m_nodes(self):
    """
    GFG: Delete N nodes after M nodes of a linked list.

    Given a linked list, delete N nodes after skipping M nodes of a linked list until the 
    last of the linked list.
    """

    def skipMdeleteN(head, M, N):
      # Code here
      if not head:
        return head

      it = head
      for i in range(M - 1):
        # if m nodes are not available.
        if not it:
          return
        it = it.next

      # now it is on mth node.
      if not it:
        return

      mthNode = it
      it = mthNode.next
      for i in range(N):
        if not it:
          break
        temp = it.next
        del it
        it = temp

      mthNode.next = it

      return skipMdeleteN(it, M, N)

  def find_min_max(self):
    """
    2058: Leetcode -> Find the Minimum and Maximum Number of Nodes Between Critical Points

    A critical point in a linked list is defined as either a local maxima or a local minima.
    A node is a local maxima if the current node has a value strictly greater than the 
    previous node and the next node.
    A node is a local minima if the current node has a value strictly smaller than the previous 
    node and the next node.
    Note that a node can only be a local maxima/minima if there exists both a previous node and a 
    next node.

    Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] 
    where minDistance is the minimum distance between any two distinct critical points and 
    maxDistance is the maximum distance between any two distinct critical points. If there are 
    fewer than two critical points, return [-1, -1].
    
    head = [5,3,1,2,5,1,2]
    """

    head = self.ll.head  # temp head you need to pass the ll.

    ans = [-1, -1]  # minDistance, maxDistance
    prev = head
    if not prev:
      return ans

    curr = head.next
    if not curr:
      return ans

    nxt = head.next.next
    if not nxt:
      return ans

    firstCP = -1
    lastCP = -1

    minDist = sys.maxsize

    i = 1
    while nxt:
      isCP = (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val)

      if isCP and firstCP == -1:
        firstCP = i
        lastCP = i
      elif isCP:
        minDist = min(minDist, i - lastCP)
        lastCP = i
      i += 1
      prev = prev.next
      curr = curr.next
      nxt = nxt.next

    if lastCP == firstCP:
      return ans

    maxDist = lastCP - firstCP
    return [minDist, maxDist]

  def merge_nodes_bw_zeros(self):
    """
    2181: Merge Nodes in Between Zeros

    You are given the head of a linked list, which contains a series of integers separated by 0's.
    The beginning and end of the linked list will have Node.val == 0.

    For every two consecutive 0's, merge all the nodes lying in between them into a single node 
    whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

    Return the head of the modified linked list.
    """
    head = self.ll.head

    if not head:
      return
    slow = head
    fast = head.next
    lastNode = None

    sum = 0
    while fast:
      if fast.val != 0:
        sum = sum + fast.val
      else:
        slow.val = sum
        lastNode = slow
        slow = slow.next
        sum = 0
      fast = fast.next

    temp = lastNode.next
    lastNode.next = None

    while temp:
      nxt = temp.next
      del temp
      temp = nxt

    return head
