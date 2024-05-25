def calc_fib(n):
    fib = [0, 1]
    if 0 <= n <= 45:
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    else:
        print("Значение должно быть в диапозоне 0 до 45")

try:
    with open('input.txt', 'r') as file:
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
    result = calc_fib(n)
except NameError:
    print("Значение не найдено")

try:
    with open('output.txt', 'w') as file:
        file.write(str(result))
except NameError:
    print("Запись в файл не удалась")
