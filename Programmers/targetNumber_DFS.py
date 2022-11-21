# def solution(numbers,target):
#     answer = 0
#     queue = [[numbers[0],0], [-1*numbers[0],0]]
#     n = len(numbers)
#     while queue:
#         temp,idx = queue.pop()
#         idx +=1
#         if idx < n:
#             queue.append([temp+numbers[idx],idx])
#             print(numbers[idx])
#             queue.append([temp-numbers[idx],idx])
#         else:
#             if temp == target:
#                 answer+=1
#     return answer

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer


print(solution([4, 1, 2, 1],4))