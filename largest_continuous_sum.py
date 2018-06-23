def sum(n):
  current_sum=0
  max_sum=0
  for i in n:
    current_sum=current_sum+i
    max_sum=max(current_sum,max_sum)
    if i < 0:
      current_sum=0
  return max_sum  



arr=[1, 2, 3, 4, -6, 7, 7, 7]
#[25,34,38,-12,34,23,10]

print(sum(arr))

