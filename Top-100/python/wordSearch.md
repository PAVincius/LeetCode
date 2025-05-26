# Word Search Problem (LeetCode #79)

## 📜 Problem Description

Given an `m x n` grid of characters `board` and a string `word`, the task is to determine if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in the construction of a single word.

**Example 1:**
Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
Output: `true`

**Example 2:**
Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "SEE"`
Output: `true`

**Example 3:**
Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCB"`
Output: `false`

## 🧠 Approach: Backtracking (Depth-First Search)

This problem is a classic application of the **backtracking** algorithm, which explores all potential paths in a search space and "backtracks" when a path is determined to be invalid or a solution is found. In this case, it's implemented as a Depth-First Search (DFS).

### Algorithm Details

1.  **Main Iteration:**
    * We iterate through every cell (`r`, `c`) of the `board`.
    * For each cell, we attempt to start a search for the `word` if that cell could potentially be the start of the word (i.e., `board[r][c] == word[0]`). Our DFS function will handle this initial character match internally.

2.  **Depth-First Search (DFS) Helper Function:**
    We define a recursive helper function, typically `dfs(row, col, k)`, with the following parameters:
    * `row`, `col`: The current coordinates of the cell being examined in the `board`.
    * `k`: The current index in the `word` that we are trying to match with `board[row][col]`.

    The DFS function operates as follows:

    * **Base Case 1 (Success ✅):**
        If `k` equals the length of `word` (`k == len(word)`), it means we have successfully found and matched all characters of the `word` in sequence. We return `true`.

    * **Base Case 2 (Failure/Pruning 🛑):**
        The search down the current path should stop (return `false`) if any of these conditions are met:
        1.  **Out of Bounds:** The `row` or `col` is outside the valid dimensions of the `board`.
        2.  **Character Mismatch:** The character at `board[row][col]` does not match the character `word[k]`.
        3.  **Already Visited (in current path):** If `board[row][col]` has already been used in the current path to form the word. (This is handled by the marking technique described below; if we mark visited cells with '#', then `board[row][col] == '#'` would lead to a mismatch with `word[k]` unless `word[k]` itself is '#', which is not allowed by problem constraints).

    * **Recursive Step (Explore Neighbors 🧭):**
        If the current cell `board[row][col]` *does* match `word[k]` (and we're within bounds and haven't failed other base cases):
        1.  **Mark as Visited:** To adhere to the "same letter cell may not be used more than once" rule *for the current search path*, we temporarily modify `board[row][col]`. A common technique is to change its value to a special sentinel character (e.g., `'#'`) that is guaranteed not to be in the `word`.
        2.  **Explore Adjacent Cells:** Recursively call the `dfs` function for all four valid neighbors (up, down, left, right):
            * `dfs(row + 1, col, k + 1)` (down)
            * `dfs(row - 1, col, k + 1)` (up)
            * `dfs(row, col + 1, k + 1)` (right)
            * `dfs(row, col - 1, k + 1)` (left)
            If *any* of these recursive calls return `true`, it means the remainder of the `word` (from `k+1` onwards) was found. We can then propagate this `true` result up the call stack.
        3.  **Backtrack (Undo Mark):** This is a **critical** step in backtracking. *Before* the current `dfs(row, col, k)` call returns, we must revert the change made to `board[row][col]`. That is, restore its original character (e.g., `board[row][col] = original_char`). This "unmarking" ensures that the cell is available for consideration in other search paths (e.g., paths that might start from a different initial cell on the board, or alternative branches from a previous decision point in the current search).

3.  **Overall Result:**
    The main function `exist` returns `true` if any of the initial DFS calls (triggered from iterating over the board cells) return `true`. If all possible starting points and subsequent paths are explored and none lead to the complete `word`, the function returns `false`.

### ⚙️ Search Pruning

The described DFS with backtracking inherently includes search pruning:
* **Boundary Pruning:** The search stops immediately if it attempts to go out of the grid boundaries.
* **Mismatch Pruning:** The search stops for a path if a character in the grid doesn't match the corresponding character in the `word`.
* **Visited Cell Pruning:** By temporarily marking cells (e.g., as `'#'`), we prevent reusing the same cell within the *current active path*, effectively pruning cyclic or overlapping paths that violate the problem's constraint.

**Follow-up: Further Pruning for Larger Boards**
While the standard backtracking is generally effective, for significantly larger boards or more complex scenarios, additional pruning can be considered:
* **Character Frequency Pre-Check:** Before initiating any DFS, count the character frequencies in both the `board` and the `word`. If the `word` requires more occurrences of a specific character than are available on the entire `board`, we can immediately determine that the `word` cannot be formed and return `false`. This adds an initial O(M*N + L) overhead (where L is word length) but can save substantial DFS time if it prunes the entire search early. For the given constraints (m, n <= 6, word.length <= 15), this might be a minor optimization.
