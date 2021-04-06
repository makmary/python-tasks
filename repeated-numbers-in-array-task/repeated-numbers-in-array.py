def count_repeated_numbers(nums: []):
    found = []
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i != j:
                new_tup = (i, j)[::-1]
                if new_tup not in found:
                    found.append((i, j))
    return len(found)


array1 = [1, 2, 3, 1, 1, 3]
print("Example 1: ", count_repeated_numbers(array1))
array2 = [1, 1, 1, 1]
print("Example 2: ", count_repeated_numbers(array2))
