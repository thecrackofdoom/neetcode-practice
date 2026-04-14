class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None   # store full word here

    def addWord(self, word):
        curr = self
        for ch in word:
            i = ord(ch) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]
            idx = ord(ch) - ord('a')
            nxt = node.children[idx]
            if nxt is None:
                return

            # found a word
            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None   # avoid duplicates

            # mark visited
            board[r][c] = '#'

            # only recurse if valid
            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)
            if r < rows - 1 and board[r + 1][c] != '#':
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)
            if c < cols - 1 and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)

            # restore
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                if root.children[ord(board[r][c]) - ord('a')] is not None:
                    dfs(r, c, root)

        return ans