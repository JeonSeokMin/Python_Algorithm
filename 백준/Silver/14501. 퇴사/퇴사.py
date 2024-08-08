N = int(input())

T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0 for _ in range(N+1)]

for i in range(len(dp)-1, -1, -1):

    if i == N:
        continue
    else:
        if i + T[i] > N:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], dp[i + T[i]] + P[i])

print(dp[0])




