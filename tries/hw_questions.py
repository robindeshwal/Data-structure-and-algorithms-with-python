from collections import Counter


class LLNode:

  def __init__(self, data):
    self.data = data
    self.next = None


class Questions:

  def array_subset(self, a1, a2, n, m):
    """
    GFG: Array Subset -> Array subset of another array.
    """
    a1 = Counter(a1)

    for i in range(m):
      if a2[i] in a1 and a1[a2[i]] > 0:
        a1[a2[i]] -= 1
      else:
        return "No"

    return "Yes"

  def union_two_ll(self, head1, head2):
    """
    GFG: Union of Two Linked Lists
    """
    # code here
    # return head of resultant linkedlist
    hmap = {}
    curr = head1
    while curr:
      if curr.data not in hmap:
        hmap[curr.data] = curr
      curr = curr.next

    curr = head2
    while curr:
      if curr.data not in hmap:
        hmap[curr.data] = curr
      curr = curr.next

    ul = LLNode(None)
    curr = ul

    for key in sorted(hmap):
      curr.next = hmap[key]
      curr = curr.next

    curr.next = None

    return ul.next

  def intersection_LL(self, head1, head2):
    """
    GFG: Intersection of Two Linked Lists.
    """
    # code here
    # return head of intersection list
    hmap = {}
    curr = head2
    while curr:
      if curr.data not in hmap:
        hmap[curr.data] = 0
      hmap[curr.data] += 1
      curr = curr.next

    ic = LLNode(0)
    ic_curr = ic

    curr = head1
    while curr:
      if curr.data in hmap and hmap[curr.data] > 0:
        ic_curr.next = curr
        ic_curr = ic_curr.next
        hmap[curr.data] -= 1
      curr = curr.next

    ic_curr.next = None

    return ic.next

  def sum_equals(self, arr, n):
    """
    GFG: Sum equals to Sum
    """
    #code here.
    hmap = {}

    for i in range(n):
      for j in range(i + 1, n):
        ele1 = arr[i]
        ele2 = arr[j]
        sm = ele1 + ele2
        if sm in hmap:
          return 1
        else:
          hmap[sm] = 1

    return 0

  def largest_subarray(self):
    """
    GFG: Largest subarray with 0 sum.
    """
