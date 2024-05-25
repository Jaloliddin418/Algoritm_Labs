def rabin_karp(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    prime = 101  # Простое число для вычисления хэша

    # Функция для вычисления хэша строки
    def calc_hash(string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * prime + ord(char)) % prime
        return hash_value

    # Вычисляем хэш для паттерна и для первого окна текста
    pattern_hash = calc_hash(pattern)
    text_hash = calc_hash(text[:pattern_len])

    occurrences = []
    # Проходим по тексту, сравнивая хэши
    for i in range(text_len - pattern_len + 1):
        if text_hash == pattern_hash and text[i:i+pattern_len] == pattern:
            occurrences.append(i + 1)  # Начало вхождения, индексация с 1
        if i < text_len - pattern_len:
            # Пересчитываем хэш для следующего окна текста
            text_hash = (text_hash - ord(text[i]) * pow(prime, pattern_len - 1, prime)) % prime
            text_hash = (text_hash * prime + ord(text[i + pattern_len])) % prime
            text_hash = (text_hash + prime) % prime

    return occurrences

# Считываем вводные данные из файла input.txt
with open('input.txt', 'r') as f:
    pattern = f.readline().strip()
    text = f.readline().strip()

# Ищем вхождения паттерна в тексте
result = rabin_karp(pattern, text)

# Записываем результаты в файл output.txt
with open('output.txt', 'w') as f:
    f.write(str(len(result)) + '\n')
    f.write(' '.join(map(str, result)))
