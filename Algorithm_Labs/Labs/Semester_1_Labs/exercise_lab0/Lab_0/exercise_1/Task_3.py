while True:
    try:
        values = input("Введите два значения через пробел: ")
        a, b = map(int, values.split())

        if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
            break
        else:
            print("Значение должно быть в диапозоне -10^9 до 10^9");

    except ValueError:
        print("Введено некорректное значение, попробуйте заново")

with open('input.txt', 'w') as file:
    file.write(values)

result = a + b
with open('output.txt', 'w') as file:
    file.write(str(result))
