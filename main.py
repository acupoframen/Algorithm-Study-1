def fib(n):
  if n==0:
    global zero
    zero+=1
    return 0
  elif n==1:
    global one
    one+=1
    return 1
  else:
    return fib(n-1)+fib(n-2)

zero=0
one=0
n=int(input())
for i in range(n):
  inp=int(input())
  fib(inp)
  print(zero, one)
  zero=0
  one=0