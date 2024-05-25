import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)

# Пример использования для считывания из файла и записи отсортированного массива
def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    return arr

def write_output(filename, arr):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, arr)))

# Тестирование сортировки на разных типах входных данных
def test_sorting():
    for case in ["worst_case.txt", "best_case.txt", "average_case.txt"]:
        arr = read_input(case)
        quick_sort(arr)
        write_output(f"output_{case}", arr)

# Создание тестовых файлов для наихудшего, наилучшего и среднего случая
def generate_test_files():
    # Наихудший случай: массив отсортированных чисел в обратном порядке
    with open("worst_case.txt", "w") as file:
        file.write("1000\n")
        file.write(" ".join(map(str, range(1000, 0, -1))))
    # Наилучший случай: уже отсортированный массив
    with open("best_case.txt", "w") as file:
        file.write("1000\n")
        file.write(" ".join(map(str, range(1, 1001))))
    # Средний случай: случайный массив
    with open("average_case.txt", "w") as file:
        file.write("1000\n")
        file.write(" ".join(map(str, random.sample(range(1, 1001), 1000))))

# Создание тестовых файлов
generate_test_files()

# Тестирование сортировки
test_sorting()
