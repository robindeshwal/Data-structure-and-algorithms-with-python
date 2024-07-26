from collections import Counter
from tries.trie import TrieNode
from linked_list.singly_linked_list import Node as LLNode

import heapq


class CamelMatch:
  """
  1023: Leetcode -> Camelcase Matching
  """

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch not in curr.children:
        curr.children[ch] = TrieNode(ch)
      curr = curr.children[ch]
    curr.isTerminal = True

  def isMatched(self, word):
    curr = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch in curr.children:
        curr = curr.children[ch]
      elif ch.islower():
        continue
      else:
        return False

    if curr.isTerminal:
      return True
    return False

  def camelMatch(self, queries, pattern):

    self.insert(pattern)

    ans = []
    for query in queries:
      if self.isMatched(query):
        ans.append(True)
      else:
        ans.append(False)

    return ans


class ReplaceWords:
  """
  648: Leetcode -> Replace Words
  """

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch not in curr.children:
        curr.children[ch] = TrieNode(ch)
      curr = curr.children[ch]
    curr.isTerminal = True

  def search(self, word):
    curr = self.root
    ans = ""
    for i in range(len(word)):
      ch = word[i]
      if ch in curr.children:
        ans += ch
        curr = curr.children[ch]
        if curr.isTerminal:
          return ans
      else:
        return None
    return None

  def replaceWords(self, dictionary, sentence):

    for word in dictionary:
      self.insert(word)

    slist = sentence.split(" ")

    for i in range(len(slist)):
      word = slist[i]

      matchFound = self.search(word)
      if matchFound:
        slist[i] = matchFound

    return " ".join(slist)


class TopKFrequent:
  """
  692: Leetcode -> Top K Frequent Words
  """

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch not in curr.children:
        curr.children[ch] = TrieNode(ch)
      curr = curr.children[ch]
    curr.isTerminal = True
    curr.count += 1

  def traverse(self, mh, k):

    def _traverse(curr, temp):
      if not curr:
        return

      if curr.isTerminal:
        heapq.heappush(mh, (-curr.count, temp))

      for ch, child in curr.children.items():
        _traverse(child, temp + ch)

    _traverse(self.root, "")

  def topKFrequent(self, words, k):

    for i in range(len(words)):
      word = words[i]
      self.insert(word)

    max_heap = []
    self.traverse(max_heap, k)

    ans = []
    while max_heap and k:
      top = heapq.heappop(max_heap)
      ans.append(top[1])
      k -= 1
    return ans


class PalindromePairs:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, idx, word):
    curr = self.root
    for ch in list(word):
      if ch not in curr.children:
        curr.children[ch] = TrieNode(ch)
      curr = curr.children[ch]
    curr.index = idx

  def isPalindrome(self, s, l, h):
    while l <= h:
      if s[l] != s[h]:
        return False
      l += 1
      h -= 1
    return True

  def searchCase2(self, curr, temp, s):
    if curr.index != -1:
      if self.isPalindrome(s, 0, len(s) - 1):
        temp.append(curr.index)

    for ch, child in curr.children.items():
      self.searchCase2(child, temp, s + ch)

  def search(self, word, temp):
    curr = self.root

    # case 1: when a prefix of string word, exactly matched with a word in trie.
    for i in range(len(word)):
      ch = word[i]
      if curr.index != -1:
        # check rest of the word is palindrome.
        if self.isPalindrome(word, i, len(word) - 1):
          temp.append(curr.index)

      if ch in curr.children:
        curr = curr.children[ch]
      else:
        return

    # case 2: search word is a prefix of a word in the trie.
    # check remaining subtrees in the trie for the palindrome.

    self.searchCase2(curr, temp, "")

  def palindromePairs(self, words):

    # insert all words its reversed order to check the palindrome.
    for i in range(len(words)):
      self.insert(i, words[i][::-1])

    ans = []
    # find palidromic pairs of each word.
    for i in range(len(words)):
      myPalindrome = []
      self.search(words[i], myPalindrome)

      for idx in myPalindrome:
        if idx != i:
          ans.append([i, idx])

    return ans


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

  def largest_subarray(self, arr, n):
    """
    GFG: Largest subarray with 0 sum.
    """
    #Code here
    hmap = {}
    csum = 0
    ans = 0

    for i in range(n):
      csum += arr[i]
      if csum == 0:
        ans = max(ans, i + 1)
      elif csum not in hmap:
        hmap[csum] = i
      else:
        # map has already csum.
        ans = max(ans, i - hmap[csum])

    return ans

  def largest_subarray_0s_1s(self, arr, n):
    """
    GFG: Largest subarray of 0's and 1's
    """
    # code here
    hmap = {}

    csum = 0
    ans = 0

    for i in range(n):
      value = -1 if not arr[i] else 1
      csum += value
      if csum == 0:
        ans = max(ans, i + 1)

      elif csum not in hmap:
        hmap[csum] = i

      else:
        ans = max(ans, i - hmap[csum])

    return ans
