from tries.trie import Trie


class Practice:

  def __init__(self):
    self.trie = Trie()

  def trie_checking(self):
    self.trie.insert("code")
    self.trie.insert("coder")
    self.trie.insert("coding")

    print(self.trie.search("coder"))
    print(self.trie.search("codi"))

    print(self.trie.starts_with("codi"))

    print("coder deleted.")
    self.trie.delete("coder")

    print(f'Is coder present : {self.trie.search("coder")}')
