S = input()
S = list(map(lambda x: int(x), S))
result = S[0]
for i in S[1:]:
    if result<=1 or i<=1:
        result += i
    else:
        result *=i
print(result)
