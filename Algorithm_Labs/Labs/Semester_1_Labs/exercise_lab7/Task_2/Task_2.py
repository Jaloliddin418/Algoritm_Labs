import re

def pattern_matching(pattern, s):
    # Создаем регулярное выражение на основе шаблона
    regex = pattern.replace(".", r"\.").replace("?", ".").replace("*", ".*")
    # Добавляем начало и конец строки для точного соответствия всей строки
    regex = "^" + regex + "$"

    # Используем регулярное выражение для проверки соответствия строки шаблону
    if re.match(regex, s):
        return "YES"
    else:
        return "NO"

def main():
    with open('input.txt', 'r') as f:
        pattern = f.readline().strip()
        s = f.readline().strip()

    result = pattern_matching(pattern, s)

    with open('output.txt', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
