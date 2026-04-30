import random


class Sudoku4x4:
    def __init__(self):
        self.board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        self.is_fixed = [[False for _ in range(4)] for _ in range(4)]
        self.generate_puzzle()

    def shuffle_board(self):
        for _ in range(10):
            area = random.randint(0, 1) * 2
            r1, r2 = area + random.randint(0, 1), area + random.randint(0, 1)
            self.board[r1], self.board[r2] = self.board[r2], self.board[r1]

    def generate_puzzle(self):
        self.shuffle_board()
        holes = 8
        while holes > 0:
            r, c = random.randint(0, 3), random.randint(0, 3)
            if self.board[r][c] != 0:
                self.board[r][c] = 0
                holes -= 1
        for r in range(4):
            for c in range(4):
                if self.board[r][c] != 0: self.is_fixed[r][c] = True

    def print_board(self):
        print("\n    0 1   2 3 (Col)")
        print("  " + "-" * 13)
        for r in range(4):
            if r % 2 == 0 and r != 0: print("  " + "-" * 13)
            print(f"{r} |", end=" ")
            for c in range(4):
                if c % 2 == 0 and c != 0: print("| ", end="")
                val = self.board[r][c]
                print((str(val) if val != 0 else ".") + " ", end="")
            print("|")
        print("  " + "-" * 13)

    def is_valid(self, row, col, num):
        if num in self.board[row]: return False
        if num in [self.board[i][col] for i in range(4)]: return False
        sr, sc = (row // 2) * 2, (col // 2) * 2
        for i in range(2):
            for j in range(2):
                if self.board[sr + i][sc + j] == num: return False
        return True

    def is_finished(self):
        for r in range(4):
            if 0 in self.board[r]: return False
        return True

    def place_number(self, r, c, n):
        if self.is_fixed[r][c]: return "FIXED"
        if self.is_valid(r, c, n):
            self.board[r][c] = n
            return "SUCCESS"
        return "CONFLICT"


def main():
    game = Sudoku4x4()
    top_msg = ""  # 放在棋盘上面的消息
    bottom_msg = ""  # 专门放在四宫格下面的消息

    print("=" * 30)
    print("   MINI SUDOKU 4x4")
    print("=" * 30)

    while True:
        # 1. 先打印上面的详细信息
        if top_msg:
            print(top_msg)

        # 2. 打印棋盘
        game.print_board()

        # 3. 打印底部的简短信息 [Success]
        if bottom_msg:
            print(bottom_msg)
            # 每一轮刷新消息，防止堆积
            top_msg = ""
            bottom_msg = ""

        if game.is_finished():
            print("\n" + "*" * 30)
            print("CONGRATULATIONS! YOU WIN!")
            print("*" * 30)
            break

        user_input = input("\nEnter 'Row Col Num' or 'q' to quit: ").lower()
        if user_input == 'q': break

        try:
            r, c, n = map(int, user_input.split())
            if 0 <= r <= 3 and 0 <= c <= 3 and 1 <= n <= 4:
                result = game.place_number(r, c, n)
                if result == "SUCCESS":
                    top_msg = f"Placed {n} at ({r}, {c})"
                    bottom_msg = "[Success]"  # 这一行会跑到底部
                elif result == "FIXED":
                    bottom_msg = "[Error] Cannot modify fixed numbers!"
                else:
                    bottom_msg = "[Error] Conflict detected!"
            else:
                bottom_msg = "[Warning] Range: 0-3, Num: 1-4."
        except:
            bottom_msg = "[Warning] Format: Row Col Num"


if __name__ == "__main__":
    main()