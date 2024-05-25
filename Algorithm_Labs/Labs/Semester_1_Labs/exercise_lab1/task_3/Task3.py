def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)

'''Доказательство завершаемости:
Каждый проход внешнего цикла (от i=1 до n-1) "выталкивает" наименьший элемент в правильное положение в конец массива. 
После n-1 таких проходов все элементы будут расположены в правильном порядке. Таким образом, алгоритм завершается.

Доказательство корректности:
На каждом шаге внутреннего цикла происходит сравнение соседних элементов и, 
если они находятся в неправильном порядке, они меняются местами. 
Это означает, что после каждого прохода внутреннего цикла наибольший из оставшихся элементов будет перемещен в конец массива. 
После n-1 проходов внешнего цикла массив будет отсортирован.

Сложность времени:
В наихудшем случае время работы пузырьковой сортировки составляет O(n^2), когда массив уже отсортирован в обратном порядке.
В среднем случае также O(n^2). Это связано с тем, 
что независимо от начального порядка элементов, алгоритм всегда выполняет одинаковое количество сравнений и обменов.'''