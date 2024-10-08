import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def poly_value(coefficients: list, x: int, mod: int, power_of_x: int = 1) -> int:
    """Вычисляет значение полинома для заданного значения с использованием рекурсии."""
    if not coefficients:
        return 0
    else:
        return (coefficients[-1] * power_of_x + poly_value(coefficients[:-1], x, mod, (power_of_x * x) % mod)) % mod


def polynomial_values(coefficients: list, x_values: list, mod: int) -> list:
    """Вычисляет значения полинома для списка значений."""
    if not x_values:
        return []
    else:
        return [poly_value(coefficients, x_values[0], mod)] + polynomial_values(coefficients, x_values[1:], mod)


def get_result(results: list) -> None:
    """Выводит результаты из списка."""
    for result in results:
        print(result)


def main() -> None:
    input_line = input().split()

    N = int(input_line[0])
    M = int(input_line[1])
    MOD = int(input_line[2])

    coefficients = []
    for i in range(N + 1):
        cuff = int(input())
        coefficients.append(cuff)

    x_values = []
    for i in range(M):
        x = int(input())
        x_values.append(x)

    start_time = time.perf_counter()

    results = polynomial_values(coefficients, x_values, MOD)

    get_result(results)

    stop_time = time.perf_counter()

    print(f"Время выполнения: {stop_time - start_time:0.5f} секунд.")

    final_memory = get_memory_usage()
    print(f"Использовано памяти: {final_memory:.2f} Mb.")


if __name__ == "__main__":
    main()
