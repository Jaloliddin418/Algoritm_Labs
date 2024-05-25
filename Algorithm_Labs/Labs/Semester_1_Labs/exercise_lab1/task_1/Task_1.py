def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    if n < 1 or n > 10 ** 3:
        raise ValueError("n должно быть в диапазоне от 1 до 10^3.")
    array = list(map(int, file.readline().split()))

    if len(array) != n:
        raise ValueError("Количество элементов массива не соответствует значению n.")
    if any(abs(x) > 10 ** 9 for x in array):  # Проверяем ограничения для абсолютного значения элементов массива
        raise ValueError("Абсолютное значение элементов массива не должно превышать 10^9.")
insertion_sort(array)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, array)))
