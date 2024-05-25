class Queue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def add_patient_middle(self, patient):
        mid = len(self.queue) // 2
        if len(self.queue) % 2 == 0:
            self.queue.insert(mid, patient)
        else:
            self.queue.insert(mid + 1, patient)

    def remove_patient(self):
        return self.queue.pop(0)


def process_queue(queries):
    queue = Queue()
    result = []

    for query in queries:
        if query[0] == '+':
            queue.add_patient(int(query[1]))
        elif query[0] == '*':
            queue.add_patient_middle(int(query[1]))
        elif query[0] == '-':
            result.append(queue.remove_patient())

    return result


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        queries = [f.readline().strip().split() for _ in range(n)]  # Splitting the query string

    result = process_queue(queries)

    with open('output.txt', 'w') as f:
        for item in result:
            f.write(str(item) + '\n')



if __name__ == '__main__':
    main()
