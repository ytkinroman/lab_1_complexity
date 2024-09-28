import time
import os
import psutil
from typing import List


class QuickSort:
    def __init__(self, array: List[int]):
        self.array = array

    def __quick_sort(self, low: int, high: int) -> None:
        """Алгоритм быстрой сортировки."""
        if low < high:
            mid = self.__partition(low, high)
            self.__quick_sort(low, mid - 1)
            self.__quick_sort(mid + 1, high)

    def __partition(self, low: int, high: int) -> int:
        """Функция разделения массива."""
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def sort(self) -> List[int]:
        """Сортировка массива с помощью быстрой сортировки."""
        self.__quick_sort(0, len(self.array) - 1)
        return self.array


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def get_list_to_string(input_list: List[int]) -> str:
    """Преобразует список целых чисел в строку."""
    result = ""

    for distance in input_list:
        result += str(distance) + " "

    result_array = result.strip()

    return result_array


def string_to_list(input_str: str) -> List[int]:
    """Преобразует строку, содержащую числа, разделенные пробелами, в множество целых чисел."""
    input_str = input_str.split()

    result_list = []
    for i in input_str:
        result_list.append(int(i))

    return result_list


def find_symmetric_difference_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    """Нахождение симметрической разности."""
    sym_diff = []

    for item in list_a:
        if item not in list_b:
            sym_diff.append(item)

    for item in list_b:
        if item not in list_a:
            sym_diff.append(item)

    return sym_diff


def find_symmetric_difference(string_values: str):
    """Нахождение симметрической разности."""
    parts = string_values.split("0")

    list_a = string_to_list(parts[0].strip())
    list_b = string_to_list(parts[1].strip())

    sym_diff = find_symmetric_difference_lists(list_a, list_b)

    if not sym_diff:
        return "0"
    else:
        qs = QuickSort(sym_diff)
        sorted_array = qs.sort()

        return get_list_to_string(sorted_array)


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
