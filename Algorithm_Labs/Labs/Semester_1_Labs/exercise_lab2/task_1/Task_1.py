import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Функция для чтения входных данных из файла
def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    return n, arr

# Функция для записи отсортированного массива в файл
def write_output(filename, arr):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, arr)))

# Генерация наихудшего случая: массив отсортированных чисел в обратном порядке
def generate_worst_case(n):
    return list(range(n, 0, -1))

# Генерация наилучшего случая: уже отсортированный массив
def generate_best_case(n):
    return list(range(1, n + 1))

# Генерация среднего случая: случайный массив
def generate_average_case(n):
    return random.sample(range(1, n + 1), n)

# Проверка сортировки на различных входных данных
def test_sorting():
    cases = {
        "Worst Case (Reversed)": generate_worst_case(1000),
        "Best Case (Sorted)": generate_best_case(1000),
        "Average Case (Random)": generate_average_case(1000)
    }

    for case, data in cases.items():
        arr = data.copy()
        merge_sort(arr)
        print(f"{case}: Sorted correctly - {arr == sorted(data)}")

# Проверка сортировки
test_sorting()
