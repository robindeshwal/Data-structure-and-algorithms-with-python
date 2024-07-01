from linked_list.singly_linked_list import LinkedList


class Questions:
  """
  """

  def __init__(self):
    self.ll = LinkedList()

  def reverse_ll(self):
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

    return

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
