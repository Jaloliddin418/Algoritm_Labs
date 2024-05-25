class DataStructure:
    def __init__(self):
        self.elements = set()
        self.sorted_list = []

    def add(self, value):
        if value not in self.elements:
            self.elements.add(value)
            self.sorted_list.append(value)
            self.sorted_list.sort()

    def delete(self, value):
        if value in self.elements:
            self.elements.remove(value)
            self.sorted_list.remove(value)

    def find(self, value):
        return value in self.elements

    def range_sum(self, left, right):
        return sum(v for v in self.sorted_list if left <= v <= right)

# Чтение входных данных
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    operations = [file.readline().strip() for _ in range(n)]

M = 1000000001
x = 0  # результат последней операции sum или 0

ds = DataStructure()
results = []

for operation in operations:
    if operation[0] == '+':
        _, i = operation.split()
        i = int(i)
        value = (i + x) % M
        ds.add(value)
    elif operation[0] == '-':
        _, i = operation.split()
        i = int(i)
        value = (i + x) % M
        ds.delete(value)
    elif operation[0] == '?':
        _, i = operation.split()
        i = int(i)
        value = (i + x) % M
        if ds.find(value):
            results.append("Found")
        else:
            results.append("Not found")
    elif operation[0] == 's':
        _, l, r = operation.split()
        l = int(l)
        r = int(r)
        left = (l + x) % M
        right = (r + x) % M
        if left <= right:
            x = ds.range_sum(left, right)
        else:
            x = ds.range_sum(left, M - 1) + ds.range_sum(0, right)
        results.append(str(x))

# Запись результатов
with open('output.txt', 'w') as file:
    for result in results:
        file.write(result + "\n")
