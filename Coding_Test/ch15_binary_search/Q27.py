from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
num_list = list(map(int, input().split()))


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


return_value = count_by_range(num_list, x, x)

if return_value == 0:
    print(-1)
else:
    print(return_value)
