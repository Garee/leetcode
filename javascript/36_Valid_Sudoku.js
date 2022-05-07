/**
 * 36. Valid Soduku (Medium)
 *
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
 * to be validated according to the following rules:
 *
 * 1. Each row must contain the digits 1-9 without repetition.
 * 2. Each column must contain the digits 1-9 without repetition.
 * 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
 *    1-9 without repetition.
 *
 * Note:
 *
 * A Sudoku board (partially filled) could be valid but is not necessarily
 * solvable. Only the filled cells need to be validated according to the
 * mentioned rules.
 *
 * Constraints:
 *
 *   board.length == 9
 *   board[i].length == 9
 *   board[i][j] is a digit 1-9 or '.'.
 */

/**
 * Patterns: Arrays, Hashing, Sets
 * Time: O(n^2) where n in the dimension of the board
 * Space: O(n) where n is the dimension of the board.
 *
 * @param {character[][]} board the sudoku board.
 * @return {boolean} true if the board is valid; false otherwise.
 */
var isValidSudoku = function (board) {
    const rows = Array.from({ length: board.length }, (_) => new Set());
    const cols = Array.from({ length: board.length }, (_) => new Set());
    const cells = new Map();

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            if (board[i][j] === ".") {
                continue;
            }

            const n = parseInt(board[i][j]);
            if (rows[i].has(n) || cols[j].has(n)) {
                return false;
            }

            rows[i].add(n);
            cols[j].add(n);

            const key = `${Math.floor(i / 3)}${Math.floor(j / 3)}`;
            if (cells.has(key)) {
                if (cells.get(key).has(n)) {
                    return false;
                }

                cells.get(key).add(n);
            } else {
                cells.set(key, new Set([n]));
            }
        }
    }

    return true;
};

test("example 1", () => {
    const board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ];
    const ans = isValidSudoku(board);
    expect(ans).toBe(true);
});

test("example 2", () => {
    const board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ];
    const ans = isValidSudoku(board);
    expect(ans).toBe(false);
});
