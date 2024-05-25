def merge_sort_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = merge_sort_count_inversions(arr[:mid])
    right, right_inversions = merge_sort_count_inversions(arr[mid:])
    merged, split_inversions = merge_and_count_split_inversions(left, right)

    return merged, left_inversions + right_inversions + split_inversions


def merge_and_count_split_inversions(left, right):
    merged = []
    split_inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, split_inversions


def count_inversions(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))

    sorted_arr, inversions = merge_sort_count_inversions(arr)

    return inversions


# Пример использования:
inversions_count = count_inversions('input.txt')
with open('output.txt', 'w') as file:
    file.write(str(inversions_count))
