# Add Two Numbers

This folder contains a Java solution for the [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) problem on LeetCode.

## Problem statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## Solution approach

The algorithm iterates through both lists simultaneously, adding corresponding digits along with any carry from the previous step. A dummy node is used to simplify list construction. The loop continues while there are nodes in either list or a remaining carry. This runs in O(n) time and uses O(1) additional space besides the output list.

## Files

- `AddTwoNumbers.java` &ndash; Java implementation with a short example in `main`.
