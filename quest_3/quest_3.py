from typing import Set
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def get_list_to_string(input_list: list) -> str:
    """Преобразует список целых чисел в строку."""
    result = ""

    for distance in input_list:
        result += str(distance) + " "

    result_array = result.strip()

    return result_array


def string_to_set(input_str: str) -> Set[int]:
    """Преобразует строку, содержащую числа, разделенные пробелами, в множество целых чисел."""
    input_str = input_str.split()

    result_set = set()
    for i in input_str:
        result_set.add(int(i))

    return result_set


def qick_sort_symmetric_difference(arr: list) -> list:
    """Алгоритм быстрой сортировки."""
    if len(arr) <= 1:
        return arr
    else:
        element = arr[0]

        left = []
        for x in arr:
            if x < element:
                left.append(x)

        middle = []
        for x in arr:
            if x == element:
                middle.append(x)

        right = []
        for x in arr:
            if x > element:
                right.append(x)

        return qick_sort_symmetric_difference(left) + middle + qick_sort_symmetric_difference(right)


def find_symmetric_difference(string_values: str):
    """Нахождение симметрической разности множеств."""

    parts = string_values.split("0")

    set_a = string_to_set(parts[0].strip())
    set_b = string_to_set(parts[1].strip())

    sym_diff = set_a.symmetric_difference(set_b)
    sym_diff = list(sym_diff)

    if not sym_diff:
        return "0"
    else:
        sort_diff = qick_sort_symmetric_difference(sym_diff)

        result = get_list_to_string(sort_diff)

        return result


def main() -> None:
    input_str = input()

    start_time = time.perf_counter()

    sym_diff = find_symmetric_difference(input_str)
    print(sym_diff)

    print("")

    stop_time = time.perf_counter()

    print(f"Время выполнения: {stop_time - start_time:0.5f} секунд.")

    final_memory = get_memory_usage()
    print(f"Использовано памяти: {final_memory:.2f} Mb.")


if __name__ == "__main__":
    main()
