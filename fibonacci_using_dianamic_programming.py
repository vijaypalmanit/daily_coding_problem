#fibonacci using dianamic programming

def fib_dianamic(n):
  fib=[0]*n
  fib[0]=fib[1]=1

  for i in range(2,n):
    fib[i]=fib[i-2]+fib[i-1]
  return fib[-1]  

num=5
print(fib_dianamic(num))