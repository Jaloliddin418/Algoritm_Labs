def find_majority_element(nums):
    def majority_element_helper(start, end):
        if start == end:
            return nums[start]

        mid = (start + end) // 2
        left_majority = majority_element_helper(start, mid)
        right_majority = majority_element_helper(mid + 1, end)

        if left_majority == right_majority:
            return left_majority

        left_count = sum(1 for i in range(start, end + 1) if nums[i] == left_majority)
        right_count = sum(1 for i in range(start, end + 1) if nums[i] == right_majority)

        return left_majority if left_count > (end - start + 1) // 2 else right_majority

    majority_candidate = majority_element_helper(0, len(nums) - 1)
    count = sum(1 for num in nums if num == majority_candidate)

    return 1 if count > len(nums) // 2 else 0

# Чтение входных данных
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    nums = list(map(int, file.readline().strip().split()))

# Поиск и вывод результата
result = find_majority_element(nums)
with open('output.txt', 'w') as file:
    file.write(str(result))
