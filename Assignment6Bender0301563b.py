######################### 
# Course: COMP 2113 FA01, 2023
# Assignment 6 - Heaps
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/11/08
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

def readNumsFromFile(filePath):
    #Read i fcuntion similar to the one from last assignment, this time as a function
    try:
        #Will first try and read in the numbers as a list
        with open(filePath, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            return numbers
    except FileNotFoundError:
        #If there is no file, print an error message (returns empty list)
        print(f"Error: File '{filePath}' not found.")
        return []
    except Exception as e:
        #Catch any other error (returns empty list)
        print(f"An error occurred: {e}")
        return []
    
def heapify(arr):
    #Turn the previously read in array into a heap
    n = len(arr)
    #Will start from closest root to bottom, then call on pushDown
    for i in range(n // 2 - 1, -1, -1):
        pushDown(arr, i, n)
        
def pushDown(arr, index, size):
    
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2
    largest = index
    
    #Compare element at given index and swap if it is necessary
    #Repeat until the structure of heap is restored
    if leftChild < size and arr[leftChild] > arr[largest]:
        largest = leftChild
    if rightChild < size and arr[rightChild] > arr[largest]:
        largest = rightChild

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        pushDown(arr, largest, size)
        

def bubbleUp(arr, i):
    #Compare element at index 'i' to parent, and swaps if larger, there for bubbling 'i' up to the top
    #Process is repeateed until heap format is correct using a while loop
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break
        
def addValue(arr, value):
    #Appends the list with given value
    #Calls bubble up in case it is larger than parent, so heap format can remain maintained
    arr.append(value)
    bubbleUp(arr, len(arr) - 1)
    
def getMax(arr):
    #Grabs index 0, so, if bubbleUp() worked correctly, it should be the largest value
    if arr:
        return arr[0]
    else:
        #If there is no list, no return
        return None
    
def removeMax(arr):
    #If no list, no return
    if not arr:
        return None
    max_val = arr[0]
    #Replace root
    last_val = arr.pop()
    if arr:
        #If list not empty, call pushDown() to maintain the heap
        arr[0] = last_val
        pushDown(arr, 0, len(arr))
    #Return removed value
    return max_val

#Test case

filePathNums = 'numbers.txt'

arr = readNumsFromFile(filePathNums)
print(arr) 
print("\n")
heapify(arr)
print("\n")
print(arr)
print("\n")
addValue(arr, 8)
print("\n")
print(arr) 
print("\n")
maxVal = removeMax(arr)
print("\n")
print("Removed val: "+str(maxVal))
print("\n")
print(arr) 





