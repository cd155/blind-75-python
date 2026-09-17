# Blind 75 Python Solutions

A collection of solutions to the famous "Blind 75" LeetCode problems in Python.

## 📚 Overview

This repository contains Python solutions to the Blind 75 list - a curated list of 75 LeetCode problems that cover the most important patterns and concepts for technical interviews.

## 🗂️ Structure

Solutions are organized by the [NeetCode Blind 75](https://neetcode.io/practice/practice/blind75) categories:

```
src/
├── arrays_and_hashing/  # Arrays & Hashing (8)
├── two_pointers/        # Two Pointers (3)
├── sliding_window/      # Sliding Window (4)
├── stack/               # Stack (1)
├── binary_search/       # Binary Search (2)
├── linked_list/         # Linked List (6)
├── trees/               # Trees (11)
├── heap_priority_queue/ # Heap / Priority Queue (1)
├── backtracking/        # Backtracking (2)
├── tries/               # Tries (3)
├── graphs/              # Graphs (6)
├── advanced_graphs/     # Advanced Graphs (1)
├── dp_1d/               # 1-D Dynamic Programming (10)
├── dp_2d/               # 2-D Dynamic Programming (2)
├── greedy/              # Greedy (2)
├── intervals/           # Intervals (5)
├── math_and_geometry/   # Math & Geometry (3)
└── bit_manipulation/    # Bit Manipulation (5)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/cd155/blind-75-python.git
cd blind-75-python

# Create python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific category
pytest tests/test_two_sum.py

# Run with verbose output
pytest -v
```

### Running Individual Solutions

Each solution file can be run independently:

```bash
python src/arrays_and_hashing/two_sum.py
```

## 📝 Problem Categories

### Arrays & Hashing (8 problems)
- Contains Duplicate
- Valid Anagram
- Two Sum
- Group Anagrams
- Top K Frequent Elements
- Encode and Decode Strings
- Product of Array Except Self
- Longest Consecutive Sequence

### Two Pointers (3 problems)
- Valid Palindrome
- 3Sum
- Container With Most Water

### Sliding Window (4 problems)
- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Minimum Window Substring

### Stack (1 problem)
- Valid Parentheses

### Binary Search (2 problems)
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array

### Linked List (6 problems)
- Reverse Linked List
- Merge Two Sorted Lists
- Reorder List
- Remove Nth Node From End of List
- Linked List Cycle
- Merge k Sorted Lists

### Trees (11 problems)
- Invert Binary Tree
- Maximum Depth of Binary Tree
- Same Tree
- Subtree of Another Tree
- Lowest Common Ancestor of a Binary Search Tree
- Binary Tree Level Order Traversal
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Construct Binary Tree from Preorder and Inorder Traversal
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree

### Heap / Priority Queue (1 problem)
- Find Median from Data Stream

### Backtracking (2 problems)
- Combination Sum
- Word Search

### Tries (3 problems)
- Implement Trie (Prefix Tree)
- Design Add and Search Words Data Structure
- Word Search II

### Graphs (6 problems)
- Number of Islands
- Clone Graph
- Pacific Atlantic Water Flow
- Course Schedule
- Graph Valid Tree
- Number of Connected Components in an Undirected Graph

### Advanced Graphs (1 problem)
- Alien Dictionary

### 1-D Dynamic Programming (10 problems)
- Climbing Stairs
- House Robber
- House Robber II
- Longest Palindromic Substring
- Palindromic Substrings
- Decode Ways
- Coin Change
- Maximum Product Subarray
- Word Break
- Longest Increasing Subsequence

### 2-D Dynamic Programming (2 problems)
- Unique Paths
- Longest Common Subsequence

### Greedy (2 problems)
- Maximum Subarray
- Jump Game

### Intervals (5 problems)
- Insert Interval
- Merge Intervals
- Non-overlapping Intervals
- Meeting Rooms
- Meeting Rooms II

### Math & Geometry (3 problems)
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes

### Bit Manipulation (5 problems)
- Number of 1 Bits
- Counting Bits
- Reverse Bits
- Missing Number
- Sum of Two Integers

## 🔗 Resources

- [Original Blind 75 List](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
- [LeetCode](https://leetcode.com/)
- [NeetCode Blind 75](https://neetcode.io/practice/practice/blind75) - Category roadmap and video explanations

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!