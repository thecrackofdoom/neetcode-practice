class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.isEnd = True
    def search(self, word: str) -> bool:
        
        def wildcard(word, curr):
            if curr is None:
                return False
            for index, char in enumerate(word):
                i = ord(char) - ord('a')
                if char == '.':
                    for idx in range(26):
                        return wildcard(word[index + 1 : ], curr.children[idx])
                elif curr.children[i] is None:
                    return False
                
                curr = curr.children[i]
            return curr.isEnd
        return wildcard(word, self.root)
