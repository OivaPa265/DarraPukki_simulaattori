// 1. 标准底盘（绝对正确）
let solution = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
];

let board = [];
let isFixed = [];
let selR = -1, selC = -1, mistakes = 0;

// 音效引擎
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playSound(type) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain); gain.connect(audioCtx.destination);
    if (type === 'click') {
        osc.frequency.setValueAtTime(600, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
        osc.start(); osc.stop(audioCtx.currentTime + 0.1);
    } else if (type === 'success') {
        osc.frequency.setValueAtTime(500, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(1000, audioCtx.currentTime + 0.2);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
        osc.start(); osc.stop(audioCtx.currentTime + 0.3);
    } else if (type === 'fail') {
        osc.frequency.setValueAtTime(200, audioCtx.currentTime);
        osc.frequency.linearRampToValueAtTime(50, audioCtx.currentTime + 0.5);
        gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
        osc.start(); osc.stop(audioCtx.currentTime + 0.5);
    }
}

// 初始化游戏
function initGame() {
    // A. 随机置换数字 (1-4 随机映射)
    let mapping = [1, 2, 3, 4].sort(() => Math.random() - 0.5);

    // B. 生成当前关卡的完整答案
    board = solution.map(row => row.map(val => mapping[val - 1]));

    // C. 深度克隆一份答案用来校验
    const finalAnswers = board.map(row => [...row]);

    // D. 挖洞 (移除8个数字)
    let holes = 0;
    isFixed = Array(4).fill().map(() => Array(4).fill(false));

    while(holes < 8) {
        let r = Math.floor(Math.random() * 4);
        let c = Math.floor(Math.random() * 4);
        if(board[r][c] !== 0) {
            board[r][c] = 0;
            holes++;
        }
    }

    // E. 标记固定数字
    for(let r=0; r<4; r++) {
        for(let c=0; c<4; c++) {
            if(board[r][c] !== 0) isFixed[r][c] = true;
        }
    }

    // 将正确答案挂载到全局方便校验
    window.correctSolution = finalAnswers;
    render();
}

function render() {
    const container = document.getElementById('sudoku-board');
    container.innerHTML = '';
    for(let r=0; r<4; r++) {
        for(let c=0; c<4; c++) {
            const div = document.createElement('div');
            div.className = 'cell' + (isFixed[r][c] ? ' fixed' : '') +
                            (r === selR && c === selC ? ' selected' : '') +
                            (board[r][c] !== 0 && !isFixed[r][c] ? ' player-input' : '');
            div.innerText = board[r][c] === 0 ? '' : board[r][c];
            div.onclick = () => { if(!isFixed[r][c]) handleSelect(r, c); };
            container.appendChild(div);
        }
    }
}

function handleSelect(r, c) {
    playSound('click');
    selR = r; selC = c;
    const panel = document.getElementById('input-panel');
    panel.classList.add('active');
    document.getElementById('pos-info').innerText = `Row ${r+1}, Col ${c+1}`;
    document.getElementById('num-input').value = board[r][c] === 0 ? '' : board[r][c];
    render();
}

function submitMove() {
    const val = parseInt(document.getElementById('num-input').value);
    if(isNaN(val) || val < 1 || val > 4) return;

    // 校验：填入的数字必须和我们预设的正确答案一致
    if(val === window.correctSolution[selR][selC]) {
        playSound('success');
        board[selR][selC] = val;
        render();
        if(!board.flat().includes(0)) {
            confetti({ particleCount: 200, spread: 80, origin: { y: 0.6 } });
            document.getElementById('win-overlay').style.display = 'flex';
        }
    } else {
        playSound('fail');
        mistakes++;
        document.getElementById('mistake-display').innerText = `Mistakes: ${mistakes} / 2`;
        if(mistakes >= 2) document.getElementById('lose-overlay').style.display = 'flex';
    }
}

function eraseCell() {
    playSound('click');
    board[selR][selC] = 0;
    document.getElementById('num-input').value = '';
    render();
}

initGame();