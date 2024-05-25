def main():
    with open('input.txt', 'r') as file:
        W, n = map(int, file.readline().strip().split())
        weights = list(map(int, file.readline().strip().split()))

    # Инициализируем dp массив нулями, размером (W+1)
    dp = [0] * (W + 1)

    # Проходим по каждому слитку
    for weight in weights:
        # Обновляем dp массив справа налево
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + weight)

    # Результатом будет максимальное значение в dp[W]
    with open('output.txt', 'w') as file:
        file.write(str(dp[W]))


if __name__ == '__main__':
    main()
