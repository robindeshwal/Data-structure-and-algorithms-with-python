class TrieNode:

  def __init__(self, data=None):
    self.data = data
    self.children = {}
    self.isTerminal = False
    self.count = 0  # used for specific question.
    self.index = -1  # used for specific question.


class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    # base case
    current = self.root

    for i in range(len(word)):
      ch = word[i]
      if ch not in current.children:
        current.children[ch] = TrieNode(ch)
      current = current.children[ch]

    current.isTerminal = True

  def search(self, word):
    current = self.root

    for i in range(len(word)):
      ch = word[i]
      if ch not in current.children:
        return False
      current = current.children[ch]

    return current.isTerminal

  def delete(self, word):

    def _delete(node, word, depth):
      if depth == len(word):
        if not node.isTerminal:
          return False  # Word not found
        node.isTerminal = False
        return len(node.children) == 0  # If true, delete this node

      char = word[depth]
      if char not in node.children:
        return False  # Word not found

      can_delete_child = _delete(node.children[char], word, depth + 1)

      if can_delete_child:
        del node.children[char]
        return len(node.children) == 0 and not node.isTerminal

      return False

    _delete(self.root, word, 0)

  def starts_with(self, prefix):
    current = self.root

    for i in range(len(prefix)):
      ch = prefix[i]
      if ch not in current.children:
        return False
      current = current.children[ch]

    return True
