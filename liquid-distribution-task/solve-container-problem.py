def solve_problem_a(num_list: list):
    if (len(num_list)) == 1:
        return 0
    if num_list == sorted(num_list):
        copy_num_list = num_list[:]
        values = set(copy_num_list)
        if len(values) > 1:
            min_val, max_val = min(values), max(values)
            return max_val - min_val
        else:
            return -1
    else:
        return -1


arr_len = int(input())
arr = list(map(int, input().strip().split()))[:arr_len]
ans = solve_problem_a(arr)
print(ans)
