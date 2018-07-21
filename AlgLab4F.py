# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:36:12 2017

@author: Danny

This lab defines 2 methods for finding the maximum sequential subarray
The first method perofrms in O(nlogn) while the second perrforms in O(n)
"""

def mssnlogn(a, start, end):
    if(end == start):
        return a[start]
    else:
        mid = int((end - start)/2) + start
        
        left= mid
        right = mid + 1
        lefttotal = a[left]
        righttotal = a[right]
        temp = a[left]
     
        for x in range(left-1,start-1,-1):

            temp = temp + a[x]
            #print("= ",temp)
            if (temp > lefttotal):
                lefttotal = temp

        
        temp = a[right]
      
        for x in range(right+1, end+1):
            
           
            temp = temp + a[x]
          
            if (temp > righttotal):
                righttotal = temp

          
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
        if(temp < a[x]):
            temp = a[x]
    return total
        
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
print("O(n):",mssn(mylist))
print("O(nlogn):", mssnlogn(mylist, 0,len(mylist)-1))