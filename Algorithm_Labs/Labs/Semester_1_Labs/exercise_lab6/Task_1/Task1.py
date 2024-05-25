def phone_book_manager(queries):
    phone_book = {}
    results = []

    for query in queries:
        command = query.split()
        if command[0] == "add":
            phone_book[command[1]] = command[2]
        elif command[0] == "del":
            if command[1] in phone_book:
                del phone_book[command[1]]
        elif command[0] == "find":
            if command[1] in phone_book:
                results.append(phone_book[command[1]])
            else:
                results.append("not found")

    return results

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        queries = [f.readline().strip() for _ in range(n)]

    results = phone_book_manager(queries)

    with open('output.txt', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
