import sys
sys.stdin = open("in1.txt","r")
N = int(input())
conference = []
for i in range(N):
    start, end = map(int, input().split())
    conference.append((start, end))
conference.sort(key = lambda x : (x[1], x[0])) # end의 값을 기준으로 정렬을 하고 값이 같다면 start의 값을 기준으로 정렬하라
end_time = 0
cnt=0
for s,e in conference:
    if s >= end_time:
        end_time = e
        cnt +=1
print(cnt)