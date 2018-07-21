# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:36:12 2017

@author: Danny
"""
import random
def mssnlogn(a, start, end):
    if(end == start):
        return a[start]
    else:
        mid = int((end - start)/2) + start
        #print(mid)
        left= mid
        right = mid + 1
        lefttotal = a[left]
        righttotal = a[right]
        temp = a[left]
        for x in range(left-1,start-1,-1):
            #print("L:index is ", x, ", num is ", a[x])
            temp = temp + a[x]
            if (temp > lefttotal):
                lefttotal = temp

        #print("left total is ", lefttotal)
        temp = a[right]
        for x in range(right+1, end+1):
            #print("R:index is ", x, ", num is ", a[x])
            temp = temp + a[x]
            if (temp > righttotal):
                righttotal = temp

        #print("right total is ", righttotal)        
        total = lefttotal + righttotal
            
        leftmss = mssnlogn(a,start,left)
        rightmss = mssnlogn(a, right, end)
        mss = max(leftmss,rightmss)
        return(max(mss, total))
    
    
            
def mssn(a):
    total = a[0]
    temp =a[0]
    for x in range(1,len(a)):
        temp = temp + a[x]
        if (temp > total):
            total = temp
        if(temp < 0):
            temp = 0
    return total
        
#getting user input
number = input("Enter a number")
number = int(number)

#create an empty list
mylist = [-27, 14, -4, 61, -61, 73, 2, 77, -83, -71]
'''
limit = 100
#populate list with random numbers
for x in range(0,number):
    mylist.append(random.randint(-limit,limit))
    '''
print(mylist)
print(mssn(mylist))
print(mssnlogn(mylist, 0,len(mylist)-1))