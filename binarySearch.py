# -*- coding: utf-8 -*-
"""binarySearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G55ggF-ZXJhSC5jnCzKbNtQt0J_615nd
"""

def binarySearch(A,l,r,x):
  if (r >= l):
    mid = int((l + (r-l))/2)
    if (A[mid] == x):
      return mid
    elif (A[mid] > x):
      r = mid - 1
      return binarySearch(A,l,r,x)
    else:
      l = mid + 1
      return binarySearch(A,l,r,x)

A = [1,2,3,4,5,6,7,8,9]
print(binarySearch(A,0,len(A)-1,8))