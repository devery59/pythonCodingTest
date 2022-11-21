import math

def solution(monsters, bullets):
    answer = 0

    for index,value in enumerate(monsters):
        gcd = math.gcd(value[0], value[1])
        monsters[index] = [value[0]/gcd,value[1]/gcd]

    for index,value in enumerate(bullets):
        gcd = math.gcd(value[0], value[1])
        bullets[index] = [value[0]/gcd,value[1]/gcd]

    for bullet in bullets:
        if bullet in monsters:
            answer+=1
            monsters.remove(bullet)
    if answer ==0:
        return -1
    else:
        return answer


# print(solution([[-4,4],[-2,2],[6,2],[0,-2]],[[3,1],[-1,1],[-1,1],[0,-4],[2,-3]]))
print(solution([[1,2],[-2,-1],[1,-2],[3,-1]],[[1,0],[2,1]]))

