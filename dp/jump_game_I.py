def can_jump(arr, curr_index, end_index, cache):
    if curr_index >= end_index:
        return True

    if cache[curr_index] != -1:
        return cache[curr_index]

    curr_step = arr[curr_index]
    for i in range(curr_step, 0, -1):
        next_index = curr_index + i
        result = can_jump(arr, next_index, end_index, cache)
        cache[next_index] = result
        if result:
            return True

    cache[curr_index] = False
    return False

    # def canJump(self, nums: List[int]) -> bool:
    #
    #     last_good = len(nums) - 1
    #
    #     for i in range(last_good - 1, -1, -1):
    #         if i + nums[i] >= last_good:
    #             last_good = i
    #
    #     return last_good == 0

# arr = [1, 2, 3, 1, 1, 4]
arr = [3, 2, 1, 0, 4]
cache = [-1] * len(arr)
print(can_jump(arr, 0, len(arr) - 1, cache))
