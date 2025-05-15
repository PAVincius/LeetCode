# Explanation:

## Bit Manipulation:
cols: A bitmask to keep track of columns that are under attack.
diag1: A bitmask to keep track of the diagonals running from top-left to bottom-right. The key is row + col.
diag2: A bitmask to keep track of the diagonals running from top-right to bottom-left. The key is row - col + n.
solve Function:

The function solve takes the current row and the three bitmasks as arguments.
If row == n, it means we have successfully placed all queens, so we add the current board configuration to the result list.
For each column in the current row, we check if placing a queen at board[row][col] is safe using the bitmasks.

If it is safe, we place the queen, update the bitmasks, and recursively call solve for the next row.
After the recursive call, we backtrack by removing the queen and resetting the bitmasks.

## Initialization:

We initialize an empty board with all positions set to '.' and call the solve function starting from the first row with all bitmasks set to 0.
This optimized approach significantly reduces the time complexity by using bit manipulation to check and update the constraints, making it much faster, especially for larger values of n.