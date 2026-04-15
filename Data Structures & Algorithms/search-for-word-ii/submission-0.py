class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                i = ord(char) - ord('a')
                if curr.children[i] is None:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
            curr.isEnd = True
        
        ans = []
        dirs = [(1,0), (0,1), (-1, 0), (0,-1)]
        def backtracking (curr, visited, curr_cell, word):
            if curr.isEnd:
                ans.append(''.join(word))
                
            for dir in dirs:
                if 0 <= curr_cell[0] + dir[0] <= len(board) - 1 and 0 <= curr_cell[1] + dir[1] <= len(board[0]) - 1 and (curr_cell[0] + dir[0], curr_cell[1] + dir[1]) not in visited:
                    char = board[curr_cell[0] + dir[0]][curr_cell[1] + dir[1]]
                    i = ord(char) - ord('a')
                    if curr.children[i] is not None:
                        word.append(char)
                        visited.add((curr_cell[0] + dir[0], curr_cell[1] + dir[1]))
                        
                        backtracking(curr.children[i], visited, (curr_cell[0] + dir[0], curr_cell[1] + dir[1]), word)

                        visited.remove((curr_cell[0] + dir[0], curr_cell[1] + dir[1]))
                        word.pop()
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtracking(root, set(), (row,col), [])
        return list(set(ans))