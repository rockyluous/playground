# Two Sum

This folder contains a solution for the [Two Sum](https://leetcode.com/problems/two-sum/) problem on LeetCode.

## Problem statement

Given an array of integers `nums` and an integer `target`, find two numbers such that they add up to `target` and return their indices. Each input has exactly one solution, and you may not use the same element twice. Return the answer in any order.

## Solution approach

The algorithm uses a hash map to store numbers we've seen so far along with their indices. For each element in the array, we compute its complement (`target - nums[i]`). If the complement is already in the map, we return the pair of indices. Otherwise we store the current number and its index in the map and continue. This approach runs in O(n) time and uses O(n) additional space.

## Files

- `solution.py` &ndash; Python implementation of the above approach.
- `TwoSum.java` &ndash; Java implementation with a small example.
