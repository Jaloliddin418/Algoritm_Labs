def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())  # Число интервалов
        intervals = []
        for _ in range(n):
            a, b = map(int, file.readline().strip().split())
            intervals.append((a, b))

    # Сортировка интервалов по правому концу, в случае равенства по левому
    intervals.sort(key=lambda x: (x[1], x[0]))

    # Жадный выбор точек
    points = []
    current_end = -1

    for a, b in intervals:
        if current_end < a:  # Если текущий конец не покрывает новый интервал
            current_end = b  # Выбираем новую точку
            points.append(current_end)

    # Запись результата в файл
    with open('output.txt', 'w') as file:
        file.write(f"{len(points)}\n")
        file.write(" ".join(map(str, points)) + "\n")


if __name__ == '__main__':
    main()
