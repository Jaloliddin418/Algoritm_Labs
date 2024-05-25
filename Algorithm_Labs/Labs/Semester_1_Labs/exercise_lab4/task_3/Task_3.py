class MinQueue:
    def __init__(self):
        self.stack_main = []  # Основной стек
        self.stack_min = []   # Стек минимальных элементов

    def enqueue(self, x):
        self.stack_main.append(x)
        if not self.stack_min or x <= self.stack_min[-1]:
            self.stack_min.append(x)

    def dequeue(self):
        if not self.stack_main:
            return None
        x = self.stack_main.pop(0)
        if self.stack_min and x == self.stack_min[0]:
            self.stack_min.pop(0)
        return x

    def get_min(self):
        if not self.stack_min:
            return None
        return self.stack_min[0]

# Чтение входных данных из файла
with open('input.txt', 'r') as f:
    M = int(f.readline().strip())
    commands = [f.readline().strip().split() for _ in range(M)]

# Обработка команд и запись результатов в файл
min_queue = MinQueue()
results = []
for command in commands:
    if command[0] == '+':
        x = int(command[1])
        min_queue.enqueue(x)
    elif command[0] == '-':
        min_queue.dequeue()
    elif command[0] == '?':
        results.append(str(min_queue.get_min()))

# Запись результатов в файл
with open('output.txt', 'w') as f:
    f.write('\n'.join(results))
