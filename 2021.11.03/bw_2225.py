import sys

n,k = map(int,sys.stdin.readline().split())

dp = [[0]*(n+1) for _ in range(k)]          # k*(n+1) 배열 생성

for i in range(n+1):                        # 1번째 행, 열에 1로 채움
    dp[0][i] = 1
for i in range(k):
    dp[i][0] = 1
#print(dp)

for i in range(1,k):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])           # 배열의 제일마지막 원소 출력
