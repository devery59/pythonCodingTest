n,c = map(int,input().split())
wifi_list = list()
for _ in range(n):
    wifi_list.append(int(input()))

wifi_list.sort()

start = 1
end = wifi_list[-1] - wifi_list[0]
result = 0

while (start <=end):
    mid = (start+end)//2
    value = wifi_list[0]
    count = 1
    for i in range(1,n):
        if wifi_list[i] >= value+mid:
            value = wifi_list[i]
            count+=1
    if count>=c:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)