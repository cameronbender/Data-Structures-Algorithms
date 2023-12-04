/*
# Course: COMP 2113 FA01, 2023
# Assignment 2
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/10/04
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty.
*/

public class PriorityQueue {
    private int[] queue;
    private int size;

    //Setting the default capacity for the priority queue to be 5
    private static final int DEFAULT_CAPACITY = 5;

    //creating the constructor
    public PriorityQueue() {
        //initializing queue variable using default capacity of 5
        queue = new int[DEFAULT_CAPACITY];
        size = 0;
    }

    //This method adds an item to the priority queue
    public void addItem(int item) {
        ensureCapacity();
        queue[size++] = item;
    }

    public int removeItem(int index) {
        //If index is less than 0 or >= to current size of the queue, the index is invalid
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        //Retrieves element and stores it in removedItem
        int removedItem = queue[index];
        for (int i = index; i < size - 1; i++) {
            queue[i] = queue[i + 1];
        }
        //decrease size variable by 1 after removing item
        size--;
        return removedItem;
    }

    //push is implemented by calling addItem
    public void push(int item) {
        addItem(item);
    }

    public int pop() {
        //First we check if queue is empty
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        //remove and return the item at the last index (top of the queue).
        return removeItem(size - 1);
    }

    private void ensureCapacity() {
        //Check if #of elements = size of array
        if (size == queue.length) {
            //If queue is full, double the size of the array
            queue = increaseCapacity(queue);
            //Show that size has increased
            System.out.println("Increased the size of the backing array to: " + queue.length);
        }
    }

    private int[] increaseCapacity(int[] array) {
        //double size of the array
        int newCapacity = array.length * 2;
        //Create new array with new capacity
        int[] newArray = new int[newCapacity];
        //Copy elemetns over to the new array
        System.arraycopy(array, 0, newArray, 0, array.length);
        //Return with increased capacity
        return newArray;
    }

    //To check if array is empty
    public boolean isEmpty() {
        return size == 0;
    }

    public static void main(String[] args) {
        PriorityQueue priorityQueue = new PriorityQueue();
        priorityQueue.addItem(5);
        priorityQueue.addItem(3);
        priorityQueue.addItem(7);
        priorityQueue.push(2);
        priorityQueue.push(10);
        priorityQueue.removeItem(2);
        priorityQueue.pop();

        //Iterate through the elements stored in the 'queue' array of the 'priorityQueue' object.
        for (int i = 0; i < priorityQueue.size; i++) {
            //Print element at the current index 'i' of the queue
            System.out.print(priorityQueue.queue[i] + " ");
        }

    }
}



