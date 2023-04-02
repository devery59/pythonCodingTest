import sys

N = int(sys.stdin.readline().rstrip())
part_list = list(map(int, input().split()))
M = int(sys.stdin.readline().rstrip())
want_list = list(map(int, input().split()))


def part(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


for i in want_list:
    result = part(part_list, i, 0, N - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
