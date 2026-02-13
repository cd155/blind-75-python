# Blind 75 Python Solutions

A collection of solutions to the famous "Blind 75" LeetCode problems in Python.

## 📚 Overview

This repository contains Python solutions to the Blind 75 list - a curated list of 75 LeetCode problems that cover the most important patterns and concepts for technical interviews.

## 🗂️ Structure

Solutions are organized by problem category:

```
src/
├── array/              # Array problems (10)
├── binary/             # Binary/Bit Manipulation problems (5)
├── dynamic_programming/ # Dynamic Programming problems (11)
├── graph/              # Graph problems (8)
├── heap/               # Heap problems (2)
├── interval/           # Interval problems (5)
├── linked_list/        # Linked List problems (6)
├── matrix/             # Matrix problems (4)
├── string/             # String problems (10)
└── tree/               # Tree problems (14)
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
python src/array/two_sum.py
```

## 📝 Problem Categories

### Array (10 problems)
- Two Sum
- Best Time to Buy and Sell Stock
- Contains Duplicate
- Product of Array Except Self
- Maximum Subarray
- Maximum Product Subarray
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array
- 3Sum
- Container With Most Water

### Binary (5 problems)
- Sum of Two Integers
- Number of 1 Bits
- Counting Bits
- Missing Number
- Reverse Bits

### Dynamic Programming (11 problems)
- Climbing Stairs
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence
- Word Break
- Combination Sum
- House Robber
- House Robber II
- Decode Ways
- Unique Paths
- Jump Game

### Graph (8 problems)
- Clone Graph
- Course Schedule
- Pacific Atlantic Water Flow
- Number of Islands
- Longest Consecutive Sequence
- Alien Dictionary
- Graph Valid Tree
- Number of Connected Components in an Undirected Graph

### Heap (2 problems)
- Top K Frequent Elements
- Find Median from Data Stream

### Interval (5 problems)
- Insert Interval
- Merge Intervals
- Non-overlapping Intervals
- Meeting Rooms
- Meeting Rooms II

### Linked List (6 problems)
- Reverse Linked List
- Linked List Cycle
- Merge Two Sorted Lists
- Merge k Sorted Lists
- Remove Nth Node From End of List
- Reorder List

### Matrix (4 problems)
- Set Matrix Zeroes
- Spiral Matrix
- Rotate Image
- Word Search

### String (10 problems)
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Minimum Window Substring
- Valid Anagram
- Group Anagrams
- Valid Parentheses
- Valid Palindrome
- Longest Palindromic Substring
- Palindromic Substrings
- Encode and Decode Strings

### Tree (14 problems)
- Maximum Depth of Binary Tree
- Same Tree
- Invert Binary Tree
- Binary Tree Maximum Path Sum
- Binary Tree Level Order Traversal
- Serialize and Deserialize Binary Tree
- Subtree of Another Tree
- Construct Binary Tree from Preorder and Inorder Traversal
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Lowest Common Ancestor of a BST
- Implement Trie (Prefix Tree)
- Add and Search Word
- Word Search II

## 🔗 Resources

- [Original Blind 75 List](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
- [LeetCode](https://leetcode.com/)
- [NeetCode](https://neetcode.io/) - Video explanations for Blind 75

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!