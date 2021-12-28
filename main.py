import sys
n=int(sys.stdin.readline())
data=[]
for i in range(41):
  if i==0:
    data.append([1,0])
  elif i==1:
    data.append([0,1])
  else:
    data.append([data[i-1][0]+data[i-2][0],data[i-1][1]+data[i-2][1]])

for i in range(n):
  num=int(sys.stdin.readline())
  print(data[num][0],data[num[1]])
