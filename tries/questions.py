from tries.trie import TrieNode


class LongestCommonPrefix:
  """
  14: Leetcode -> Longest Common Prefix
  """

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    current = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch not in current.children:
        current.children[ch] = TrieNode(ch)
      current = current.children[ch]
    current.isTerminal = True

  def findLCP(self, string, ans):
    current = self.root

    for i in range(len(string)):
      ch = string[i]
      if len(current.children) > 1 or current.isTerminal:
        return ans

      ans.append(ch)
      current = current.children[ch]
    return ans

  def longestCommonPrefix(self, strs=["flower", "flow", "flight"]):

    for i in range(len(strs)):
      self.insert(strs[i])

    ans = []
    first = strs[0]

    self.findLCP(first, ans)

    return "".join(ans)


class ImplementDictUsingTrie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    current = self.root
    for i in range(len(word)):
      ch = word[i]
      if ch not in current.children:
        current.children[ch] = TrieNode(ch)
      current = current.children[ch]
    current.isTerminal = True

  def insert_list(self, li):
    for i in range(len(li)):
      curr = li[i]
      self.insert(curr)

  def store_all_suggestions(self, node, temp, prefix):
    # base case
    if node.isTerminal:
      temp.append(prefix)

    for ch, child in node.children.items():
      # prefix += ch
      self.store_all_suggestions(child, temp, prefix + ch)
      # backtrack
      # prefix -= ch # should be use list for backtrack.

  def getSuggestions(self, input):

    curr = self.root
    for i in range(len(input)):
      ch = input[i]
      if ch in curr.children:
        curr = curr.children[ch]
      else:
        return []

    temp = []
    self.store_all_suggestions(curr, temp, input)
    return temp

  def implement_dict(self, input="la"):

    li = ["love", "lover", "loving", "last", "lost", "lane", "lord"]
    self.insert_list(li)

    # if want an answer with all typing suggestions.
    # dic = {}
    # prefix = ""
    # for ch in input:
    #   prefix += ch
    #   ans = self.getSuggestions(prefix)
    #   dic[prefix] = ans

    # print(dic)
    # return dic

    ans = self.getSuggestions(input)
    print(ans)
    return ans
