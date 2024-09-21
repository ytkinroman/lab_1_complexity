from typing import List
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def format_houses(houses: str) -> List[int]:
    """Преобразует строку, содержащую номера домов, в список целых чисел."""
    houses = houses.split()

    seen_houses = set()

    formatted_houses = []
    for house in houses:
        house_num = int(house)
        if house_num > 10 ** 9:
            raise ValueError("Номера домов не могут превосходить 10^9.")

        if house_num != 0 and house_num in seen_houses:
            raise ValueError("Номера домов должны быть уникальными.")

        seen_houses.add(house_num)
        formatted_houses.append(house_num)

    if 0 not in formatted_houses:
        raise ValueError("В последовательности должен быть хотя бы один ноль.")

    return formatted_houses


def format_distances(distances: List[int]) -> str:
    """Преобразует список расстояний в строку, где расстояния разделены пробелами."""
    result_array = ""

    for distance in distances:
        result_array += str(distance) + " "

    result_array = result_array.strip()

    return result_array


def calculate_distances(n: int, houses: str) -> str:
    """Вычисляет минимальные расстояния до ближайшего свободного участка для каждого дома."""
    if not (1 <= n <= 10 ** 6):
        raise ValueError("Переменная n должно быть в диапазоне от 1 до 10^6.")

    houses = format_houses(houses)

    distances = [n] * n
    left_distances = [n] * n
    right_distances = [n] * n

    for i in range(n):
        if houses[i] == 0:
            left_distances[i] = 0
        elif i > 0:
            if left_distances[i] > left_distances[i - 1] + 1:
                left_distances[i] = left_distances[i - 1] + 1

    for i in range(n - 1, -1, -1):
        if houses[i] == 0:
            right_distances[i] = 0
        elif i < n - 1:
            if right_distances[i] > right_distances[i + 1] + 1:
                right_distances[i] = right_distances[i + 1] + 1

    for i in range(n):
        if left_distances[i] < right_distances[i]:
            distances[i] = left_distances[i]
        else:
            distances[i] = right_distances[i]

    distances = format_distances(distances)

    return distances


def main() -> None:
    print(" ")

    n = int(input())
    houses = str(input())

    print(" ")

    start_time = time.perf_counter()

    distances = calculate_distances(n, houses)
    print(distances)

    print("")

    stop_time = time.perf_counter()

    print(f"Время выполнения: {stop_time - start_time:0.5f} секунд.")

    final_memory = get_memory_usage()
    print(f"Использовано памяти: {final_memory:.2f} Mb.")


if __name__ == "__main__":
    main()
