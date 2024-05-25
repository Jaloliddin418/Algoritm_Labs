from memory_profiler import profile
import time
t_start = time.perf_counter()
@profile
def last_digit_of_fib(n):
    if 0 <= n <= 10**7:
        a, b = 0, 1
        for _ in range(n):
            a, b = b % 10, (a + b) % 10
        return a
    else:
        print()

try:
    with open('input_ex_3.txt', 'r') as file:
        first_line = file.readline().strip()
        if first_line:
            n = int(first_line)
        else:
            raise ValueError("Файл пустой")
except FileNotFoundError:
    print("Файл не найден")
except ValueError as e:
    print("Ошибка:", e)
try:
    result = last_digit_of_fib(n)
except NameError:
    print("Значение не найдено")

try:
    with open('output_ex_3.txt', 'w') as file:
        file.write(str(result))
except NameError:
    print("Запись в файл не удалась")
print("Время рвботы: %s секунд " % (time.perf_counter() - t_start))
