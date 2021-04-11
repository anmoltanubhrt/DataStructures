# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 20:26:32 2021

@author: avantika.joshi
"""

#This code is used to rotate the array in iterative manner

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)

def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
        


def printArray(arr,n):
    for i in range(0,n):
        print(arr[i],end = " ")
        
arr = [1,2,3,4,5,6,7]
leftRotate(arr,2,7)
printArray(arr,7)
