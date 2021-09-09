# T = int(input())
# for i in range(T):
#     pass

n, k = map(int,input().split())
result = 0

while n>=k:
    if n%k == 0:
        n//=k
        result += 1
    else:
        n-=1
        result += 1
    print(n)
while n>1:
    n -= 1
    result +=1
    print(n)
print(result)
