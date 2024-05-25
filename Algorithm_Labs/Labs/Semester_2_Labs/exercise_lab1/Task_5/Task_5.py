def count_almost_palindromes(N, K, S):
    dp = [[0] * N for _ in range(N)]

    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i + 1][j - 1] + 1

    count = 0
    for i in range(N):
        for j in range(i, N):
            if dp[i][j] <= K:
                count += 1

    return count


with open('input.txt', 'r') as file:
    N, K = map(int, file.readline().strip().split())
    S = file.readline().strip()

result = count_almost_palindromes(N, K, S)

with open('output.txt', 'w') as file:
    file.write(str(result))
