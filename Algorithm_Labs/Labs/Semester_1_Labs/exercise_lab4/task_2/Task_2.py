def is_valid_sequence(s):
    stack = []
    for char in s:
        if char in '([':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

def main():
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        sequences = [file.readline().strip() for _ in range(n)]

    results = []
    for sequence in sequences:
        if is_valid_sequence(sequence):
            results.append("YES")
        else:
            results.append("NO")

    with open("output.txt", "w") as file:
        file.write("\n".join(results))

if __name__ == "__main__":
    main()
