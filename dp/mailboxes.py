def find_min_distance(houses, index_first, index_last, mailbox_count, cache):
    if mailbox_count == 1:
        median = index_first + (index_last - index_first) // 2
        dist = 0
        for house_index in range(index_first, index_last + 1):
            dist += abs(houses[house_index] - houses[median])

        cache[index_first][index_last][mailbox_count] = dist
        return dist

    house_count = index_last - index_first + 1

    if house_count == mailbox_count:
        return 0

    if house_count < mailbox_count:
        return float('inf')

    if cache[index_first][index_last][mailbox_count] != -1:
        return cache[index_first][index_last][mailbox_count]

    min_dist = float('inf')
    for i in range(index_first, index_last):
        min_dist = min(min_dist, find_min_distance(houses, index_first, i, 1, cache) +
                       find_min_distance(houses, i + 1, index_last, mailbox_count - 1, cache))

    cache[index_first][index_last][mailbox_count] = min_dist
    return min_dist


houses = [12, 3, 5, 6]
k = 2
houses.sort()
cache = [[[-1 for _ in range(len(houses) + 1)] for _ in range(len(houses) + 1)] for _ in range(k + 2)]
find_min_distance(houses, 0, len(houses) - 1, k, cache)
