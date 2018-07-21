# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:23:34 2017

@author: Danny

This lab compares the average performance of quicksort and insertion sort
"""

import random
import time

#quick sort using median of 3 pivot
#a is the list to be sorted
#start is the starting index of what section to sort
#end is the last index of the section to be sorted
def quick_sort(a,start,end):
    #if the section is larger than 2 elements, perform quick sort
    if (end - start > 1):

        mid = int((end-start)/2)+start #getting middle element
        pivotList = []
        pivotList.append(a[start]) #first element
        pivotList.append(a[end])#last element 
        pivotList.append(a[mid]) #middle element
        
        #sorting pivot lsit to get median
        insertion_sort(pivotList)
                         
        pivot = pivotList[1] #storing pivot in new variable
        
        #Swapping pivot into last element
        temp = a[end]
        a[end] = pivot
        if (pivot == a[start]):
            a[start] = temp
        elif (a[mid] == pivot):
            a[mid] = temp
        
        
        left = start #left keeps track of left element being compared
        right = end-1 #right keeps track of right element being compared
        
        #this loop compared two elements with each other and swaps them if they on the incorrect side of the pivot
        while (left < right):

            #if the left element is smaller than the pivot, it is on the correct side so move on to next element
            if a[left]<=pivot: 
                left = left + 1
            #if the right element is bigger than the pivot, it is on the correct side so move on to next element
            if a[right]>=pivot:
                right = right-1
                
            #if the left element is bigger and the right element is smaller than the pivot, swap them
            if a[right] < pivot and  pivot < a[left] and left < right:
                temp = a[right]
                a[right] = a[left]
                a[left] = temp 
        
        #swaps the pivot into its correct spot
        if a[left] > pivot:
            temp = a[end]
            a[end] = a[left]
            a[left] = temp
        else:
            temp = a[end]
            a[end] = a[left+1]
            a[left+1] = temp
             
        #calling quicksort on the sides of the pivot
        quick_sort(a,start, left)
        quick_sort(a,left+1, end)
    #if the section is 2 elements or less, swap them in the correct order    
    elif(end-start <= 1):
        if(a[start] > a[end]):
            temp = a[end]
            a[end] = a[start]
            a[start] = temp
   
        
#insertion sort
#a is the list to be sorted
def insertion_sort(a):
    for x in range(0, len(a)):
        for y in range(0, x):
            if (a[x] <= a[y] ):
                temp = a[y]
                a[y] = a[x]
                a[x] = temp
                
#adding a list of  random numbers to the lists of lists
#arr is the list of lists
#loop is the number of lists to add to the list
#numOfElements is the number of random numbers to add to each list
def populateLists(arr, loop, numOfElements):
    for x in range(0,loop):
        mylist = [] #clearing mylist
        for y in range(0,numOfElements): #adding 100 random numbers to a list
            mylist.append(random.randint(-7000,7001)) 
        arr.append(mylist) #adding list of random numbers to list of lists
            
mylist = []
for y in range(0,25): #adding 100 random numbers to a list
    mylist.append(random.randint(0, 300)) 
quick_sort(mylist, 0, len(mylist)-1)
print(mylist)

lists = [] #list of lists
loop = 100 #number of times to execute loops
elements = 10000 #number of elements we want in lists
populateLists(lists, loop, elements)    

print("Average running time of quick sort: ")
start = time.time ()   
for x in range(0,loop):
    quick_sort(lists[x],0,len(lists[x])-1)
end = time.time() 
print((end - start)/loop)  

lists = [] #clearing list of lists
populateLists(lists, loop, elements)    
    
print("Average running time of insertion sort: ")
start = time.time()    
for x in range(0,loop):    
    insertion_sort(lists[x])
end = time.time()
print((end - start)/loop)

