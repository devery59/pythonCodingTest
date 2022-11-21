import numpy as np
grid = np.array([[2,1,1,0,1],[1,2,0,3,0],[0,1,5,1,2],[0,0,1,3,1],[1,2,0,1,1]])

def solution(grid, K):
    grid = np.array(grid)
    answer = 0

    for _ in range(K):
        sum_of_customer = 0
        for i in range(0, len(grid)-K+1):
            for j in range(0, len(grid[i])-K+1):
                if (-1 not in grid[i:i+K,j:j+K] ) and sum(sum(grid[i:i+K,j:j+K])) > sum_of_customer:
                    sum_of_customer = sum(sum(grid[i:i+K,j:j+K]))
                    max_i = i
                    max_j = j

        grid[max_i:max_i+K,max_j:max_j+K] = -1
        answer+= int(sum_of_customer)

    return answer


print(solution([[3,4,5],[2,3,4],[1,2,3]],1))
# print(solution([[2,1,1,0,1],[1,2,0,3,0],[0,1,5,1,2],[0,0,1,3,1],[1,2,0,1,1]],2))