######################### 
# Course: COMP 2113 FA01, 2023
# Assignment 7 - Hash Tables
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/11/16
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

import sys

# Linked list for seperate chaining
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#Function to create an empty hash table
#Nov 16
def createHashTable(size):
    return [None] * size

# Hash function to determine the index where word should be stored
#Nov 16
def hashFunction(word, size):
    return sum(ord(char) for char in word) % size

# Function to fill the hash table with words and their frequencies using separate chaining
#Nov 17
def fillTable(filename, size):
    hashTable = createHashTable(size)
    
    #Reading in external file
    with open(filename, 'r') as file:
        for line in file:
            #remove spaces and split up words
            words = line.strip().split()
            for word in words:
                #take out punctuation and set all to lower case
                word = word.strip('.,?!').lower()
                #calculate hash value
                hashVal = hashFunction(word, len(hashTable))

                # If the bucket is empty, create a new node
                if hashTable[hashVal] is None:
                    hashTable[hashVal] = Node(word, 1)
                else:
                    # If the bucket is not empty, traverse the linked list and update the node if the word exists
                    current = hashTable[hashVal]
                    while current.next is not None:
                        if current.key == word:
                            current.value += 1
                            break
                        current = current.next
                    else:
                        # If the word is not found in the linked list, add a new node at the end
                        current.next = Node(word, 1)
    
    #Return the table after the edits
    return hashTable

# Function to look up the frequency of a word in the hash table
#Nov 18
def lookup(hashTable, word):
    hashValue = hashFunction(word, len(hashTable))
    current = hashTable[hashValue]

    while current is not None:
        if current.key == word:
            return current.value
        current = current.next

    return "Sorry, word not found"

# Function to print the contents of the hash table, including the linked lists in each bucket
#Nov 19
def printTable(hashTable):
    for i, current in enumerate(hashTable):
        print(f"Bucket {i}: ", end="")
        while current is not None:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")

#Nov 19
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python your_script.py filename.txt")
        sys.exit(1)

    # Get the filename from the command-line arguments
    filename = sys.argv[1]
    # Set the size of the hash table
    tableSize = 100
    # Fill the hash table with data from the file
    hashTable = fillTable(filename, tableSize)
    # Print the contents of the hash table
    printTable(hashTable)
