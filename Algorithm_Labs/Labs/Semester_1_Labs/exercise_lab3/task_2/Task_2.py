def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Чтение данных из файла
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    A = list(map(int, f.readline().split()))
    B = list(map(int, f.readline().split()))

# Перемножение массивов и сортировка полученной последовательности
C = sorted([a * b for a in A for b in B])

# Вычисление суммы каждого десятого элемента последовательности
result = sum(C[::10])

# Запись результата в файл
with open('output.txt', 'w') as f:
    f.write(str(result))
