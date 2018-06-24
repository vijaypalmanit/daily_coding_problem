#Given a sorted array of integers containing duplicates, write a program #which returns the last index of an element.

#Example:
#Input:
#array = {0, 1, 2, 2, 4, 5, 5, 5, 8};
#num = 5;
#Output: 
#Element 5 found at index 7

def las_index(arr,num):
  return len(arr)-arr[::-1].index(num)-1


a=[0, 1, 2, 2, 4, 5, 5, 5, 8,5]
num=5
print(las_index(a,num))