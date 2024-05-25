def tally_votes(votes):
    results = {}

    for vote in votes:
        candidate, count = vote.split()
        count = int(count)
        if candidate in results:
            results[candidate] += count
        else:
            results[candidate] = count

    return results


def main():
    with open('input.txt', 'r') as f:
        votes = [line.strip() for line in f.readlines()]

    results = tally_votes(votes)

    # Вывод результатов в лексикографическом порядке по фамилиям кандидатов
    sorted_results = sorted(results.items(), key=lambda x: x[0])

    with open('output.txt', 'w') as f:
        for candidate, count in sorted_results:
            f.write(f"{candidate} {count}\n")


if __name__ == "__main__":
    main()
