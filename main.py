n=int(input())
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))
dp=[data[0] for _ in range(n)]

for i in range(1,n):
  dp[i][0]=data[i][0]+min(dp[i-1][1],dp[i-1][2])
  print(data[i],dp)
  dp[i][1]=data[i][1]+min(dp[i-1][0],dp[i-1][2])
  dp[i][2]=data[i][2]+min(dp[i-1][0],dp[i-1][1])

print(dp)
print(min(dp[n-1]))