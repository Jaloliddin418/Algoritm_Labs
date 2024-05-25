def compress(s):
    n = len(s)
    dp = ["" for _ in range(n + 1)]
    dp[0] = ""

    def get_repeats(sub):
        sub_len = len(sub)
        for i in range(1, sub_len + 1):
            repeat = sub[:i]
            if sub == repeat * (sub_len // i):
                return repeat, sub_len // i
        return sub, 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + s[i - 1]

        for j in range(i):
            substring = s[j:i]
            repeat_str, repeat_count = get_repeats(substring)
            if repeat_count > 1:
                new_representation = dp[j] + repeat_str + "*" + str(repeat_count)
            else:
                new_representation = dp[j] + substring

            if len(new_representation) < len(dp[i]):
                dp[i] = new_representation

    compressed_string = dp[n]

    # Разделяем на части и форматируем с "+", если это необходимо
    result = []
    i = 0
    while i < len(compressed_string):
        if '*' in compressed_string[i:]:
            j = compressed_string.find('*', i)
            result.append(compressed_string[i:j+2])
            i = j + 2
            while i < len(compressed_string) and compressed_string[i].isdigit():
                result[-1] += compressed_string[i]
                i += 1
        else:
            result.append(compressed_string[i:])
            break

    return '+'.join(result)

# Чтение из файла
with open('input.txt', 'r') as file:
    input_string = file.read().strip()

# Обработка строки
compressed_string = compress(input_string)

# Запись в файл
with open('output.txt', 'w') as file:
    file.write(compressed_string)
