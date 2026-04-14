class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            if root.children[i] is None:
                root.children[i] = TrieNode()
                root = root.children[i]
            else:
                root = root.children[i]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            i = ord(char) - ord('a')
            if root.children[i] is None:
                return False
            else:
                root = root.children[i]
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if root.children[i] is None:
                return False
            else:
                root = root.children[i]
        return True
        