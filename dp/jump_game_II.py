import sys


def jump_count(arr, curr_index, end_index, cache):

    if cache[curr_index] != -1:
        return cache[curr_index]

    furthest_index = min(curr_index + arr[curr_index], end_index)
    min_count = sys.maxsize
    for next_index in range(curr_index + 1, furthest_index + 1):
        min_count = min(min_count, 1 + jump_count(arr, next_index, end_index, cache))

    cache[curr_index] = min_count
    return min_count


# arr = [2, 3, 1, 1, 4]
# arr = [2, 3, 1, 0, 4]
arr = [2, 3, 0, 1, 4]
end_index = len(arr) - 1
cache = [-1] * len(arr)
cache[end_index] = 0
count = jump_count(arr, 0, end_index, cache)
print(count)
