class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    
    if not word:
      return True

    def dfs(r: int, c: int, k: int) -> bool:

      if k == len(word):
        return True
      
      if not (0 <= r < ROWS and 0 <= c < COLS) or \
         board[r][c] != word[k]:
        return False

      temp_char = board[r][c]
      board[r][c] = "#"  

      found = (dfs(r + 1, c, k + 1) or
               dfs(r - 1, c, k + 1) or
               dfs(r, c + 1, k + 1) or
               dfs(r, c - 1, k + 1))
      
      board[r][c] = temp_char
      
      return found

    for r in range(ROWS):
      for c in range(COLS):
        if dfs(r, c, 0):
          return True
          
    return False