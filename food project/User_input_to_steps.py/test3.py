v = [3,2,0,1,5]
sum = 0
i = 1
while i <= len(v):
    sum = sum + abs(v[i-1])
    i = i + 1

print(sum)