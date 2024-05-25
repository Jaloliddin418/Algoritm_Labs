def main():
    with open('input.txt', 'r') as file:
        # Читаем первую строку, которая содержит K и n
        K, n = map(int, file.readline().strip().split())
        # Читаем вторую строку, которая содержит времена t1...tn
        repair_times = list(map(int, file.readline().strip().split()))

    # Сортируем времена по возрастанию
    repair_times.sort()

    # Подсчитываем максимальное количество сапог, которые можно починить
    total_time = 0
    count = 0
    for time in repair_times:
        if total_time + time <= K:
            total_time += time
            count += 1
        else:
            break

    # Записываем результат в файл
    with open('output.txt', 'w') as file:
        file.write(str(count))


if __name__ == '__main__':
    main()
