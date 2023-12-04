######################### 
# Course: COMP 2113 FA01, 2023
# Assignment 5
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/10/27
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

#Code for command line
import sys 

for number, arg in enumerate(sys.argv):

    print(number, arg)


#Selection Sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

#Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for k in range(n):
        for l in range(0, n-k-1):
            if arr[l] > arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
    
    return arr

#Insertion Sort
def insertionSort(arr):
    n = len(arr)
    for q in range(1, n):
        key = arr[q]
        p = q - 1
        while p >= 0 and key < arr[p]:
            arr[p + 1] = arr[p]
            p -= 1
        arr[p + 1] = key
        
    return arr


#Main
if __name__ == "__main__":
    # Code to read command line, using provided code from assignment details
    if len(sys.argv) != 3:
        print("Usage: python t1.py <sorting_algorithm_number> <filename>")
        sys.exit(1)
    
    sortingAlgorithm= int(sys.argv[1])
    fileName = sys.argv[2]
    
    # Code to read the text files used to test using try/except
    try:
        with open(fileName, 'r') as file:
            unsortedNumbers = [int(line.strip()) for line in file]
    #If there is no file
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    
    
    # Choose sorting algorithm based on user input on the command line
    if sortingAlgorithm == 1:
        selectionSort(unsortedNumbers)
    elif sortingAlgorithm == 2:
        bubbleSort(unsortedNumbers)
    elif sortingAlgorithm == 3:
        insertionSort(unsortedNumbers)
    else:
        sys.exit(1)
    
    
    print(unsortedNumbers)

