def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

# Считываем вводные данные из файла input.txt
with open('input.txt', 'r') as f:
    s = f.readline().strip()

# Строим Z-функцию для строки s
z_values = z_function(s)

# Записываем результаты в файл output.txt
with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, z_values)))
