class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    def addWord(self, word):
        curr = self
        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ans = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def backtracking (curr, visited, curr_cell, word):
            if curr.isEnd:
                ans.add(''.join(word))
                
            
            row = curr_cell[0]
            col = curr_cell[1]

            if 0 <= row <= len(board) - 1 and 0 <= col <= len(board[0]) - 1 and (row, col) not in visited:
                char = board[row][col]

                i = ord(char) - ord('a')
                if curr.children[i] is not None:
                    word.append(char)
                    visited.add((row, col))

                    for dir in dirs:
                        r = curr_cell[0] + dir[0]
                        c = curr_cell[1] + dir[1]
                        
                        backtracking(curr.children[i], visited, (r, c), word)
                    
                    word.pop()
                    visited.remove((row, col))


        for row in range(len(board)):
            for col in range(len(board[0])):
                backtracking(root, set(), (row, col), [])
                if len(ans) == len(word):
                    return list(ans)
        return list(ans)