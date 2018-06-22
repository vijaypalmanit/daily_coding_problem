# Let's say our Fibonacci series is 0-indexed and starts with 0. So:

#   fib(0)  # => 0
# fib(1)  # => 1
# fib(2)  # => 1
# fib(3)  # => 2
# fib(4)  # => 3
# ...


def fib(n):
  if n < 2:
    return n
  return fib(n-2) + fib(n-1)  
  
print(fib(3))