import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def read_file(filename: str) -> tuple:
    """Чтение данных из файла."""
    with open(filename, "r") as file:
        line = file.readline().strip()
        a, b = map(int, line.split())

    return a, b


def save_file(result_num: int) -> None:
    """Запись данных в файл."""
    with open("output.txt", "w") as file:
        result_value = str(result_num)
        file.write(result_value)


def is_safe(board: list, row: int, col: int) -> bool:
    """Проверка, можно ли поставить магараджу на позицию."""
    for i in range(len(board)):
        if board[i][col] == 1 or board[row][i] == 1:
            return False

    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < len(board) and 0 <= new_col < len(board):
            if board[new_row][new_col] == 1:
                return False

    return True


def place_mag(board: list, row: int, col: int, count: int, K: int) -> int:
    """Рекурсивная функция для размещения магарадж на доске."""
    if count == K:
        return 1

    total = 0
    for i in range(row, len(board)):
        for j in range(len(board)):
            if is_safe(board, i, j):
                board[i][j] = 1
                total += place_mag(board, i, j, count + 1, K)
                board[i][j] = 0

    return total


def count_mag(N: int, K: int) -> int:
    """Функция для подсчета количества способов разместить магарадж на доске."""
    board = [[0] * N for _ in range(N)]
    return place_mag(board, 0, 0, 0, K)


def main() -> None:
    start_time = time.perf_counter()
    filename = "input.txt"
    N, K = read_file(filename)
    # print(N, K)

    result = count_mag(N, K)
    # print(result)
    save_file(result)

    stop_time = time.perf_counter()

    print(f"Время выполнения: {stop_time - start_time:0.5f} секунд.")

    final_memory = get_memory_usage()
    print(f"Использовано памяти: {final_memory:.2f} Mb.")


if __name__ == "__main__":
    main()
