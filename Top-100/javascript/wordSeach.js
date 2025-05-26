/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    if (!board || board.length === 0) return false;
    const ROWS = board.length;
    const COLS = board[0].length;
    const dfs = (r, c, k) => {
        if (k === word.length) {
            return true;
        }
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] !== word[k]) {
            return false;
        }
        const tempChar = board[r][c];
        board[r][c] = '#';

        const found = dfs(r + 1, c, k + 1) ||
                      dfs(r - 1, c, k + 1) ||
                      dfs(r, c + 1, k + 1) ||
                      dfs(r, c - 1, k + 1);
        board[r][c] = tempChar;

        return found;
    };

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (dfs(r, c, 0)) {
                return true;
            }
        }
    }

    return false;
};