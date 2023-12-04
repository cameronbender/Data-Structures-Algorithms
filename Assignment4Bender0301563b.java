/*
# Course: COMP 2113 FA01, 2023
# Assignment 3
# Author: Cameron Bender
# Student ID: 0301563b
# email address: 0301563b@acadiau.ca
# Date: 2023/10/20
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty.
*/


import java.util.LinkedList;
import java.util.Queue;

//node class to represent node in the tree
class Node {
    int data;
    Node left, right;

    //constructor
    public Node(int value) {
        data = value;
        //Initialize both left and right child nodes to null
        left = right = null;
    }
}


public class BinarySearchTree {
    //variable representing the root node of the tree
    private Node root;
    //initialize tree
    public BinarySearchTree() {
        root = null;
    }

    //calls on insert method to insert the value into the tree
    public void insertValue(int value) {
        root = insert(root, value);
    }

    private Node insert(Node root, int value) {
        //if the current node is null, create a new node with the given value
        if (root == null) {
            root = new Node(value);
            return root;
        }
        if (value < root.data) {
            //if the value is less than the current node's data, insert into the left subtree
            root.left = insert(root.left, value);
        } else if (value > root.data) {
            //if not, then insert on the left
            root.right = insert(root.right, value);
        }

        return root;
    }

    //method for # of nodes
    public int size() {
        return size(root);
    }

    //to calculate size  of the tree
    private int size(Node node) {
        if (node == null) {
            //if there are no nodes, return 0
            return 0;
        } else {
            //if not, calculate size by taking current node and adding the left and right sides
            return 1 + size(node.left) + size(node.right);
        }
    }


    //method to find the depth of a particular node
    public int depth(Node node) {
        return depth(root, node, 0);
    }

    //method to calculate depth of a particular node
    private int depth(Node root, Node node, int level) {
        if (root == null) {
            //if node is null, return 0, to show that it is the end of the tree
            return 0;
        }
        //if data matches, return the level
        if (root.data == node.data) {
            return level;
        }

        //Iterate through left subtree to find node
        int leftDepth = depth(root.left, node, level + 1);
        if (leftDepth != 0) {
            //if node is found, return it
            return leftDepth;
        }

        //If it is not in the left subtree, go through the right subtree
        return depth(root.right, node, level + 1);
    }

    //method to perform a depth first traversal of the tree
    public void depthTraverse() {
        //calls private method to perform the search
        depthTraverse(root);
        System.out.println();
    }

    //method that performs the depth first traversal
    private void depthTraverse(Node node) {
        //if node is null, return since it is at the end of the branch
        if (node == null) {
            return;
        }
        //traverse left subtree
        depthTraverse(node.left);
        //print the data of the node
        System.out.print(node.data + " ");
        //traverse right subtree
        depthTraverse(node.right);
    }

    public void breadthTraverse() {
        if (root == null) {
            //if tree is empty, return
            return;
        }

        //Create queue for breadth first traversal and add the root node
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        //Iterate all the way through the queue
        while (!queue.isEmpty()) {
            //remove front node
            Node tempNode = queue.poll();
            //print removed node
            System.out.print(tempNode.data + " ");

            //if removed node has a child to the left, add to queue
            if (tempNode.left != null) {
                queue.add(tempNode.left);
            }
            //if removed node has a child to the right, add to queue
            if (tempNode.right != null) {
                queue.add(tempNode.right);
            }
        }

        System.out.println();
    }

    public static void main(String[] args) {
        //Create new binary search tree object
        BinarySearchTree tree = new BinarySearchTree();
        //add values
        tree.insertValue(50);
        tree.insertValue(30);
        tree.insertValue(70);
        tree.insertValue(20);
        tree.insertValue(40);
        tree.insertValue(60);
        tree.insertValue(80);

        System.out.println("Depth-First Traversal:");
        tree.depthTraverse();

        System.out.println("Breadth-First Traversal:");
        tree.breadthTraverse();

        //add a node to test the depth search
        Node nodeToFind = new Node(40);

        System.out.println("Depth of node " + nodeToFind.data + ": " + tree.depth(nodeToFind));
        System.out.println("Size of the tree: " + tree.size());
    }
}
