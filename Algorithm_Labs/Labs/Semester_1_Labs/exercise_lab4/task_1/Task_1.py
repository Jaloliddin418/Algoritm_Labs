def main():
    with open("input.txt", "r") as file:
        commands = file.read().strip().split("\n")

    stack = []
    output = []

    for command in commands[1:]:
        if command == "-":
            removed_element = stack.pop()
            output.append(removed_element)
        else:
            _, number = command.split()
            stack.append(int(number))

    with open("output.txt", "w") as file:
        for element in output:
            file.write(str(element) + "\n")

if __name__ == "__main__":
    main()
