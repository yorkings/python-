from heapq import merge
from os import times_result
import time
from time import perf_counter


def merge_sort(arr):
    if len(arr) <=1:
        return arr

    midpoint=len(arr)//2
    left_list=arr[:midpoint]
    right_list=arr[midpoint:]
    
    left_list=merge_sort(left_list)
    right_list=merge_sort(right_list)
    
    return list(merge(left_list,right_list)) 
 
def merge(left,right):
    result=[]
    while len(left) !=0 and len(right) !=0:
        if left[0]< right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) ==0:
        result=result + right
    else:
        result=result+ left
    
    
    return result

et=perf_counter()
time_elapsed=et-et
    

array=[] 

x=int(input("Enter the number of elments in your array: "))
for i in range(x):
    z=int(input())
    
    array.append(z)
   
answer=merge_sort(array)

print(f"The sorted array: {answer}")
e_time=f"{time_elapsed:9f}"
print(f"The  time taken to sort was {e_time} seconds  ")
    