def process_operations(operations):
    result = []

    # Инициализируем пустое множество
    my_set = set()

    for op in operations:
        operation, key = op.split()
        key = int(key)

        if operation == "A":
            my_set.add(key)
        elif operation == "D":
            if key in my_set:
                my_set.remove(key)
        elif operation == "?":
            if key in my_set:
                result.append("Y")
            else:
                result.append("N")

    return result

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        operations = [f.readline().strip() for _ in range(n)]

    results = process_operations(operations)

    with open('output.txt', 'w') as f:
        for res in results:
            f.write(f"{res}\n")

if __name__ == "__main__":
    main()
