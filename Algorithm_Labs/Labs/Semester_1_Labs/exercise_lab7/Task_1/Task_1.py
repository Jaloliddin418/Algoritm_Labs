def longest_increasing_subsequence(n, sequence):
    # Инициализируем массив dp, где dp[i] содержит длину наибольшей
    # возрастающей подпоследовательности, заканчивающейся на элементе i
    dp = [1] * n
    # Инициализируем массив для отслеживания предыдущих элементов
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Находим максимальное значение в dp
    max_length = max(dp)
    # Находим индекс элемента с максимальной длиной подпоследовательности
    max_index = dp.index(max_length)

    # Строим саму подпоследовательность
    lis = []
    while max_index != -1:
        lis.append(sequence[max_index])
        max_index = prev[max_index]

    # Переворачиваем lis, так как мы построили ее с конца
    lis.reverse()

    return max_length, lis

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        sequence = list(map(int, f.readline().strip().split()))

    length, lis = longest_increasing_subsequence(n, sequence)

    with open('output.txt', 'w') as f:
        f.write(f"{length}\n")
        f.write(" ".join(map(str, lis)))

if __name__ == "__main__":
    main()
