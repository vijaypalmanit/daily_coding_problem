""" Find the element that occurs only once in a given set of integers while all the other numbers occur thrice.
Example -  
Input : 3 3 3 4
Output: 4

Input : 5 5 4 8 4 5 8 9 4 8
Output: 9 """


arr=[5,5, 4, 8, 4, 5, 8, 9, 4, 8]
num_freq = dict.fromkeys(arr,0 )

for i in arr:
  num_freq[i]=num_freq[i]+1

for key,values in num_freq.items():
  if values==1: 
      print("number is",key)