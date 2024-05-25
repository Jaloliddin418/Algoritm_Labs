import heapq

class Task:
    def __init__(self, index, time):
        self.index = index
        self.time = time

    def __lt__(self, other):
        # Определяем порядок в очереди: сначала задания с меньшим временем
        # Для заданий с одинаковым временем сравниваем по индексу
        return (self.time, self.index) < (other.time, other.index)

def process_tasks(n, m, times):
    # Инициализируем список потоков с их текущим временем
    threads = [(i, 0) for i in range(n)]
    # Инициализируем очередь с приоритетами для отслеживания доступных потоков
    available_threads = [(0, i) for i in range(n)]
    heapq.heapify(available_threads)
    # Инициализируем список результатов
    results = []

    # Проходим по каждому заданию
    for i in range(m):
        # Получаем доступный поток с наименьшим временем завершения задачи
        start_time, thread_index = heapq.heappop(available_threads)
        # Вычисляем время окончания задания
        end_time = max(start_time, threads[thread_index][1]) + times[i]
        # Обновляем время выполнения текущего потока
        threads[thread_index] = (thread_index, end_time)
        # Добавляем текущий поток обратно в список доступных с новым временем окончания
        heapq.heappush(available_threads, (end_time, thread_index))
        # Добавляем результат выполнения задания в список результатов
        results.append((thread_index, start_time))

    return results

def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().strip().split())
        times = list(map(int, f.readline().strip().split()))

    results = process_tasks(n, m, times)

    with open('output.txt', 'w') as f:
        for result in results:
            f.write(f"{result[0]} {result[1]}\n")

if __name__ == "__main__":
    main()
