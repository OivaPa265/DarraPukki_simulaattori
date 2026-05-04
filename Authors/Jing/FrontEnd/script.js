// 1. 基础数据 (The Core Data)
let board = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
];
let isFixed = [
    [false, false, false, false],
    [false, false, false, false],
    [false, false, false, false],
    [false, false, false, false]
];

// 记录当前选中的位置 (-1 表示未选中)
let selectedRow = -1;
let selectedCol = -1;

// 2. 初始化游戏 (Initialize)
function initGame() {
    shuffleBoard();
    generatePuzzle();
    renderBoard();
}

function shuffleBoard() {
    for (let i = 0; i < 10; i++) {
        let area = Math.floor(Math.random() * 2) * 2;
        let r1 = area + Math.floor(Math.random() * 2);
        let r2 = area + Math.floor(Math.random() * 2);
        [board[r1], board[r2]] = [board[r2], board[r1]];
    }
}

function generatePuzzle() {
    let holes = 8;
    while (holes > 0) {
        let r = Math.floor(Math.random() * 4);
        let c = Math.floor(Math.random() * 4);
        if (board[r][c] !== 0) {
            board[r][c] = 0;
            holes--;
        }
    }
    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            if (board[r][c] !== 0) isFixed[r][c] = true;
        }
    }
}

// 3. 渲染棋盘 (Render - Added Click Interaction)
function renderBoard() {
    const boardElement = document.getElementById('sudoku-board');
    boardElement.innerHTML = '';

    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');

            // 如果这个格子被选中了，加上 selected 样式
            if (r === selectedRow && c === selectedCol) {
                cell.classList.add('selected');
            }

            if (isFixed[r][c]) {
                cell.classList.add('fixed');
                cell.innerText = board[r][c];
            } else if (board[r][c] !== 0) {
                cell.classList.add('player-input');
                cell.innerText = board[r][c];
            }

            // 点击格子的监听器
            cell.addEventListener('click', () => {
                if (isFixed[r][c]) return; // 固定数字点不动
                selectedRow = r;
                selectedCol = c;
                renderBoard(); // 重新渲染以显示选中高亮
            });

            boardElement.appendChild(cell);
        }
    }
}

// 4. 校验逻辑 (Validation)
function isValid(row, col, num) {
    // 检查行
    for (let i = 0; i < 4; i++) {
        if (i !== col && board[row][i] === num) return false;
    }
    // 检查列
    for (let i = 0; i < 4; i++) {
        if (i !== row && board[i][col] === num) return false;
    }
    // 检查 2x2 宫
    let sr = Math.floor(row / 2) * 2;
    let sc = Math.floor(col / 2) * 2;
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            if ((sr + i !== row || sc + j !== col) && board[sr + i][sc + j] === num) return false;
        }
    }
    return true;
}

// 5. 核心填数动作 (Core Move Logic)
function handleMove(r, c, n) {
    const topMsg = document.getElementById('top-msg');
    const bottomMsg = document.getElementById('bottom-msg');
    topMsg.innerText = '';

    if (isValid(r, c, n)) {
        board[r][c] = n;
        topMsg.innerText = `[Success] Placed ${n} at (${r}, ${c})`;
        bottomMsg.innerText = '[Success]';
        renderBoard();

        if (isFinished()) {
            bottomMsg.innerText = 'CONGRATULATIONS! YOU WIN!';
        }
    } else {
        bottomMsg.innerText = '[Error] Invalid move! Conflict detected.';
    }
}

function isFinished() {
    for (let r = 0; r < 4; r++) {
        if (board[r].includes(0)) return false;
    }
    return true;
}

// 6. 键盘监听 (Keyboard Listener)
document.addEventListener('keydown', (event) => {
    if (selectedRow === -1 || selectedCol === -1) return;

    if (event.key >= '1' && event.key <= '4') {
        handleMove(selectedRow, selectedCol, parseInt(event.key));
    } else if (event.key === 'Backspace' || event.key === 'Delete') {
        board[selectedRow][selectedCol] = 0;
        renderBoard();
    }
});

// 7. 保留原本的按钮点击功能 (为了兼容你之前的界面)
document.getElementById('submit-btn').addEventListener('click', () => {
    const r = parseInt(document.getElementById('row-input').value);
    const c = parseInt(document.getElementById('col-input').value);
    const n = parseInt(document.getElementById('num-input').value);

    if (!isNaN(r) && !isNaN(c) && !isNaN(n)) {
        handleMove(r, c, n);
    }
});

initGame();