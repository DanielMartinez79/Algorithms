"""
This lab modifies the quicksort algorithm in order to find
the kth least element in a list of numbers.
k is given by the user
""" 

import random

#finds the k smallest element in the given collection of numbers
def kleast(a,start,end, k):
    
    #if the size of subarray is greater than 2, it must be sorted
    if (end - start > 1):
        #Getting the 3 pivots
        mid = int((end-start)/2)+start
        pivs = []
        pivs.append(a[start])
        pivs.append(a[end])
        pivs.append(a[mid])
        
        #Getting the median of the pivots
        low = min(pivs)
        high = max(pivs)
        pivot = sum(pivs) - (high + low)
        
        #Swapping pivot into last element
        temp = a[end]
        a[end] = pivot
        if (pivot == a[start]):
            a[start] = temp
        elif (a[mid] == pivot):
            a[mid] = temp
       
        #left is the leftmost element in the subarray
        #right is the rightmost element in the subarray
        left = start
        right = end-1
        
        #Comparing the left and right elements 
        while (left < right):


            #if left element is less than pivot, move left to next element
            if a[left]<=pivot:
                left = left + 1
            #if right element is greater than pivot, move right to next element
            if a[right]>=pivot:
                right = right-1
            #if left is greater than pivot and right is less than pivot, swap
            if a[right] < pivot and  pivot < a[left] and left < right:
                temp = a[right]
                a[right] = a[left]
                a[left] = temp 
                        
        #Inserting the pivot into its final position   
        if a[left] > pivot:
            temp = a[end]
            a[end] = a[left]
            a[left] = temp
        else:
            temp = a[end]
            a[end] = a[left+1]
            a[left+1] = temp
      
        
        #recursive calls to each side of pivot
        if (left >= k-1):
            return kleast(a,start, left,k)
        elif (k-1 >= right):
            return kleast(a,right+1, end, k)

        
    #if size of subarray is 2 or less, compare the elements and swap if needed
    elif(end-start <= 1):
        #print("start = ", start, " end = ", end, "k = ", k)
        if(a[start] > a[end]):
            temp = a[end]
            a[end] = a[start]
            a[start] = temp 

        if ((k-1) == start):
            return (a[start])
        elif ((k-1) == end):
            return (a[end])
            

#getting user input
number = input("Enter a number")
number = int(number)

#create an empty list
mylist = []
limit = 100
#populate list with random numbers
for x in range(0,number):
    mylist.append(random.randint(-limit,limit))
print(mylist)

#ask for user input
least = input("Enter k for kth least element ")
least = int(least)
print(kleast(mylist, 0, len(mylist)-1, least))

#Checking to see if the algorithm works correctly
mylistdupe = sorted(mylist)
print("Check: ", mylistdupe[least-1])

