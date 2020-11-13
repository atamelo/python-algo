REACHABLE = 1
NON_REACHABLE = 0
IN_PROGRESS = 2
NONE = -1


def can_reach(arr, curr_index, cache):
    if curr_index < 0 or curr_index >= len(arr):
        return NON_REACHABLE

    if arr[curr_index] == 0:
        return REACHABLE

    if cache[curr_index] == REACHABLE or cache[curr_index] == NON_REACHABLE:
        return cache[curr_index]

    if cache[curr_index] == IN_PROGRESS:
        return NON_REACHABLE

    cache[curr_index] = IN_PROGRESS

    cache[curr_index] = \
        can_reach(arr, curr_index + arr[curr_index], cache) or \
        can_reach(arr, curr_index - arr[curr_index], cache)

    return cache[curr_index]


arr = [3, 0, 2, 1, 2]
cache = [NONE] * len(arr)
result = can_reach(arr, 2, cache)
print(result)
