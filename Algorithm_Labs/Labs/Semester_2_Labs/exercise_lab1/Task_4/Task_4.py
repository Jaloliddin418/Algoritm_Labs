def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
        (opening == '[' and closing == ']') or \
        (opening == '{' and closing == '}')

def longest_valid_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if is_matching(s[i], s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

    result = []
    i, j = 0, n - 1
    while i <= j:
        if i < n - 1 and dp[i][j] == dp[i + 1][j]:
            i += 1
        elif j > 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif is_matching(s[i], s[j]) and dp[i][j] == dp[i + 1][j - 1] + 2:
            result.append(s[i])
            result.append(s[j])
            i += 1
            j -= 1
        else:
            for k in range(i, j):
                if dp[i][j] == dp[i][k] + dp[k + 1][j]:
                    j = k
                    break
    return ''.join(result)


# Чтение входных данных
with open('input.txt', 'r') as file:
    input_str = file.readline().strip()

# Вычисление результата
result = longest_valid_subsequence(input_str)

# Запись результата
with open('output.txt', 'w') as file:
    file.write(result)
