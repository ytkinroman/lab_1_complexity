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
        first_line = file.readline().strip()
        parts = first_line.split()

        N = int(parts[0])  # Общее число зарегистрированных участников.
        K = int(parts[1])  # Требуемое количество человек в первой команде.

        M = int(parts[2])  # Количество пар участников, знакомых друг с другом.

        edges = []
        for i in range(M):
            line = file.readline().strip()
            parts = line.split()

            a = int(parts[0])
            b = int(parts[1])
            edge = (a, b)

            edges.append(edge)

        return N, K, M, edges


def get_matrix(party: int, edges: list) -> list:
    """Создание матрицы смежности."""
    matrix = []

    for i in range(party):
        row = [0] * party
        matrix.append(row)

    for edge in edges:
        u = edge[0] - 1
        v = edge[1] - 1
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix


def calculate_cohesion(team_list: list, matrix: list) -> int:
    """Вычисляет связность команды путем подсчета количества пар участников в команде."""
    team_length = len(team_list)
    ties = 0
    for i in range(team_length):
        for j in range(i + 1, team_length):
            if matrix[team_list[i] - 1][team_list[j] - 1] == 1:
                ties += 1
    return ties


def generate_combinations(current_combination: list, remaining_participants: list, k: int, matrix: list, best_combination: list, best_cohesion: list) -> None:
    """Генерирует комбинации участников и находит лучшую комбинацию на основе связности."""
    if len(current_combination) == k:
        cohesion = calculate_cohesion(current_combination, matrix)
        if cohesion > best_cohesion[0]:
            best_cohesion[0] = cohesion
            best_combination[0] = current_combination
        return

    for i in range(len(remaining_participants)):
        generate_combinations(current_combination + [remaining_participants[i]], remaining_participants[i+1:], k, matrix, best_combination, best_cohesion)


def find_best_combination(N: int, K: int, matrix: list) -> str:
    """Находит лучшую комбинацию участников."""
    participants = list(range(1, N + 1))
    best_combination = [[]]

    generate_combinations([], participants, K, matrix, best_combination, [0])

    return get_result_string(best_combination[0])


def get_result_string(result_list: list) -> str:
    """Преобразует список целых чисел в строку."""
    return " ".join(map(str, result_list))


def main() -> None:
    start_time = time.perf_counter()
    filename = "input.txt"
    N, K, M, edges = read_file(filename)

    matrix = get_matrix(N, edges)

    best_combination = find_best_combination(N, K, matrix)

    with open("output.txt", "w") as file:
        file.write(best_combination)

    stop_time = time.perf_counter()

    print(f"Время выполнения: {stop_time - start_time:0.5f} секунд.")

    final_memory = get_memory_usage()
    print(f"Использовано памяти: {final_memory:.2f} Mb.")


if __name__ == "__main__":
    main()
