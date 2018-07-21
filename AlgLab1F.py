# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:02:37 2017

@author: Danny

This lab compares the average and worst case performance of linear and binary search
"""
import random
import time
import math

#linear search
def linear(arr, key):
    for x in range(0, len(arr)):
        if (arr[x] == key):
            #print("Found!")
            return
    #print ("Not found!")
    return

#binary search    
def bins(start,end,key,arr):
    #gets middle element
    mid = (end - start)/2 + start
    mid = int(mid)
    
    #subarray is larger than 1 
    if (end > start):
        #middle element is key
        if (key == arr[mid]):
            #print("Found!")
            return
        #key is larger than middle element
        elif (key > arr[mid]):
            #search 2nd half of array
            bins(mid +1, end, key, arr)
        #key is smaller than middle element, so search 1st half of array
        else: bins (start, mid-1, key, arr)
    #subarray is size 1    
    else:
        #single element is the key
        if (arr[start] == key):
            #print("Found!")
            return
        #else: print("Not in the array!")
    
    
mylist =[] #new list
number = input("Enter a number: ") #number of elements in the list
number = int(number) #casting to int
for x in range(0,number):
    mylist.append(random.randint(-1000,1001)) # adding random numbers to list

mylist = sorted(mylist) #sort list

              
print("Part A: Calculating average time of linear and binary search")
loop = 500 #number of times to execute loop
start = time.time()
for x in range(0,loop):#perform linear search 500 times
    linear(mylist,random.randint(-1000,1001)) #search for a random element
end = time.time()
timer1 = (end-start)/loop #average time it took for 1 linear search
print("Average running time of linear search: ", timer1)
avg1 = timer1/number #time of 1 instruction

#same process as above with binary search
start = time.time()
for x in range(0,loop):
    bins(0, len(mylist)-1,random.randint(-1000,1001),mylist)  
end = time.time()
timer2 = (end - start)/loop #average time of 1 binary search
print("Average running time of binary search: ", timer2)
avg2 = timer2/math.log(number, 2) #time of 1 instruction

avg = (avg1+ avg2)/2 #average time of 1 instruction

print("\nPart B: Calcutlating worst case time of linear and binary search")  
mylist =[] #clearing list
notInList = 50000 # a number that is not in the list
for x in range(0,10000): #inserting 10000 elements into list
    mylist.append(random.randint(-1000,1001))

mylist = sorted(mylist) #sort list

print("Worst case linear when n = 10^5")
start = time.time()
for x in range(0,loop):
    linear(mylist,notInList)#searching for a number that is not in the list
end = time.time()
print((end - start)/loop) #average time of 1 worst case linear search

#same process as above with binary search
print("Worst case binary when n = 10^5")
start = time.time()
for x in range(0,loop):
    bins(0, len(mylist)-1,notInList,mylist)  
end = time.time()
print((end - start)/loop)

count = 1000000 #number of elements in list
wclin = (avg*count) #worst case linear search with 10^6 elements
print("\nEstimated worst-case linear when n = 10^6: ", wclin)
wcbin = (avg*math.log(count,2)) #worst case binary search with 10^6 elements
print("Estimated worst-case binary when n = 10^6: ", wcbin)

mylist = [] #clear list
for x in range(0,count):
    mylist.append(random.randint(-1000,1001))

mylist = sorted(mylist)

#same process as before with 10^6 elements 
print("\nWorst case linear when n = 10^6")
start = time.time()
for x in range(0,loop):
    linear(mylist,notInList)  
end = time.time()
print((end - start)/loop)

print("Worst case binary when n = 10^6")
start = time.time()
for x in range(0,loop):
    bins(0, len(mylist)-1,notInList,mylist)  
end = time.time()
print((end - start)/loop)