import sys

NO_SOLUTION = sys.maxsize


def calc_skip_path(arr, curr_position, jump_table, prev_steps):
    if curr_position > len(arr) - 1:
        return NO_SOLUTION

    if arr[curr_position] == 0:
        return curr_position

    if curr_position in prev_steps:
        return NO_SOLUTION

    if jump_table[curr_position] != -1:
        return jump_table[curr_position]

    prev_steps.add(curr_position)
    skip_to = calc_skip_path(arr, curr_position + arr[curr_position], jump_table, prev_steps)
    jump_table[curr_position] = skip_to

    return skip_to


def min_moves(arr, curr_position, k, prev_steps, curr_path, all_paths, jump_table, cache):

    if curr_position == len(arr) - 1:
        all_paths.append((list(curr_path)))
        return 0

    if curr_position > len(arr) - 1:
        return NO_SOLUTION

    if curr_position in prev_steps:
        return NO_SOLUTION

    if cache[curr_position] != -1:
        return cache[curr_position]

    curr_min = NO_SOLUTION

    if arr[curr_position] != 0:
        if jump_table[curr_position] == -1:
            calc_skip_path(arr, curr_position, jump_table, set())

        next_position = jump_table[curr_position]
        if next_position == -1 or next_position == NO_SOLUTION:
            return NO_SOLUTION

        curr_min = min_moves(arr, next_position, k, prev_steps, curr_path, all_paths, jump_table, cache)
    else:
        for step in range(1, k + 1):
            prev_steps.add(curr_position)
            curr_path.append(step)
            curr_min = min(curr_min, 1 + min_moves(arr, curr_position + step, k, prev_steps, curr_path, all_paths,
                                                   jump_table, cache))
            curr_path.pop()

    cache[curr_position] = curr_min

    return curr_min


# a = [0, 1, -1, 0]
# jump_table = [-1] * len(a)
# calc_skip_path(a, 1, jump_table, set())
# print(a)
# print(jump_table)

arr = [0, -1, -2, 0, 4, 1, 2, -1, 0]
# arr = [0, 1, -2, 0, 4, -1, -2, 0, -1, 0]
# arr = [0, 2, -1, 0]
# arr = [0, 1, -1, 0]

prev_steps = set()
all_paths = []
cache = [-1] * len(arr)
jump_table = [-1] * len(arr)
mm = min_moves(arr, 0, 3, prev_steps, [], all_paths, jump_table, cache)
if mm == NO_SOLUTION:
    print("NO")
else:
    print(mm)
    for path in all_paths:
        print(path)

