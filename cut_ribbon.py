n, a, b, c = list(map(int, input().split()))
 
 
l = [-1e9] * (n + 1)
 
 
l[0] = 0
 
for i in range(n+1):
    if i-a >= 0:
        l[i] = max(l[i], l[i-a] + 1)
    if i-b >= 0:
        l[i] = max(l[i], l[i-b] + 1)
    if i-c >= 0:
        l[i] = max(l[i], l[i-c] + 1)
        
print(l[n])