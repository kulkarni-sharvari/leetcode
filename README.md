# LeetCode Solutions

A collection of my LeetCode problem solutions implemented in Python, featuring detailed time and space complexity analysis.

## About

This repository contains my solutions to various LeetCode problems. Each solution includes:
- Clean, readable Python code
- Time complexity analysis
- Space complexity analysis
- Explanatory comments where helpful

## Structure
```
.
├── Helper/     # Shared data structures (e.g. TreeNode) used across solutions
├── easy/
├── medium/
├── hard/
├── todo/       # Problems in progress / not yet finalized
└── README.md
```

## Problems Solved (56)

### Easy (20)

| # | Title | Topics | Solution |
|---|-------|--------|----------|
| 1 | Two Sum | Array, Hash Table | [Link](./easy/1_TwoSum.py) |
| 20 | Valid Parentheses | Stack, String | [Link](./easy/20_ValidParentheses.py) |
| 21 | Merge Two Sorted Lists | Linked List | [Link](./easy/21_MergeSortedList.py) |
| 100 | Same Tree | Tree, DFS | [Link](./easy/100_SameTree.py) |
| 101 | Symmetric Tree | Tree, DFS | [Link](./easy/SymmetricTree.py) |
| 104 | Maximum Depth of Binary Tree | Tree, DFS | [Link](./easy/104_MaxDepthBT.py) |
| 110 | Balanced Binary Tree | Tree, DFS | [Link](./easy/110_BalancedBT.py) |
| 111 | Minimum Depth of Binary Tree | Tree, BFS/DFS | [Link](./easy/111_MinimumDepthBT.py) |
| 112 | Path Sum | Tree, DFS | [Link](./easy/112_PathSUm.py) |
| 125 | Valid Palindrome | Two Pointers, String | [Link](./easy/125_ValidPalindrome.py) |
| 141 | Linked List Cycle | Linked List, Two Pointers | [Link](./easy/141_LinkedListCycle.py) |
| 206 | Reverse Linked List | Linked List | [Link](./easy/206_ReverseLinkedList.py) |
| 217 | Contains Duplicate | Array, Hash Table | [Link](./easy/217_ContainsDuplicates.py) |
| 226 | Invert Binary Tree | Tree, DFS | [Link](./easy/226_InvertBinaryTree.py) |
| 242 | Valid Anagram | String, Hash Table | [Link](./easy/242_Anagram.py) |
| 543 | Diameter of Binary Tree | Tree, DFS | [Link](./easy/543_diameterOfBT.py) |
| 572 | Subtree of Another Tree | Tree, DFS | [Link](./easy/572_SubtreeOfAnotherTree.py) |
| 617 | Merge Two Binary Trees | Tree, DFS | [Link](./easy/MergeBinaryTrees.py) |
| 704 | Binary Search | Binary Search | [Link](./easy/704_BinarySearch.py) |
| 3238 | Find the Number of Winning Players | Array, Hash Table | [Link](./easy/3238_FindTheNumberOfWinningPlayers.py) |

### Medium (29)

| # | Title | Topics | Solution |
|---|-------|--------|----------|
| 2 | Add Two Numbers | Linked List, Math | [Link](./medium/2_AddTwoNumbers.py) |
| 3 | Longest Substring Without Repeating Characters | Sliding Window, Hash Table | [Link](./medium/3_LongestSubstringWithoutRepeatingCharacters.py) |
| 11 | Container With Most Water | Two Pointers, Array | [Link](./medium/11_ContainerWithMostWater.py) |
| 15 | 3Sum | Two Pointers, Array | [Link](./medium/15_3Sum.py) |
| 19 | Remove Nth Node From End of List | Linked List, Two Pointers | [Link](./medium/19_RemoveNthNode.py) |
| 36 | Valid Sudoku | Array, Hash Table | [Link](./medium/36_ValidSudoku.py) |
| 49 | Group Anagrams | Array, Hash Table | [Link](./medium/49_GroupAnagram.py) |
| 74 | Search a 2D Matrix | Binary Search | [Link](./medium/74_Search2DMatrix.py) |
| 98 | Validate Binary Search Tree | Tree, DFS | [Link](./medium/98_ValidateBST.py) |
| 102 | Binary Tree Level Order Traversal | Tree, BFS | [Link](./medium/102_BTLevelOrderTraversal.py) |
| 106 | Construct Binary Tree from Inorder and Postorder Traversal | Tree, DFS | [Link](./medium/106_ConstructBTInorderAndPostorder.py) |
| 128 | Longest Consecutive Sequence | Array, Hash Table | [Link](./medium/128_Longest_ConsecutiveSequence.py) |
| 138 | Copy List with Random Pointer | Linked List, Hash Table | [Link](./medium/138_CopyListWithRandomPointer.py) |
| 143 | Reorder List | Linked List, Two Pointers | [Link](./medium/143_ReorderList.py) |
| 146 | LRU Cache | Design, Hash Table, Linked List | [Link](./medium/146_LRUCache.py) |
| 150 | Evaluate Reverse Polish Notation | Stack, Array | [Link](./medium/150_EvaluateReversePolishNotation.py) |
| 155 | Min Stack | Stack, Design | [Link](./medium/155_MinStack.py) |
| 167 | Two Sum II - Input Array Is Sorted | Two Pointers, Array | [Link](./medium/167_TwoSumII.py) |
| 199 | Binary Tree Right Side View | Tree, BFS | [Link](./medium/199_BTRightSideView.py) |
| 236 | Lowest Common Ancestor of a Binary Tree | Tree, DFS | [Link](./medium/236_LowerstCommonAncestorBT.py) |
| 238 | Product of Array Except Self | Array, Prefix Sum | [Link](./medium/238_ProductArrayExceptSelf.py) |
| 287 | Find the Duplicate Number | Array, Two Pointers | [Link](./medium/287_FindDuplicateNumber.py) |
| 347 | Top K Frequent Elements | Array, Hash Table | [Link](./medium/347_TopKFrequentElements.py) |
| 560 | Subarray Sum Equals K | Array, Hash Table, Prefix Sum | [Link](./medium/560_SubArraySumEqualsK.py) |
| 739 | Daily Temperatures | Stack, Array | [Link](./medium/739_DailyTemperatures.py) |
| 853 | Car Fleet | Stack, Array | [Link](./medium/853_CarFleet.py) |
| 875 | Koko Eating Bananas | Binary Search | [Link](./medium/875_KokoEatsBanana.py) |
| 981 | Time Based Key-Value Store | Design, Hash Table | [Link](./medium/981_TimeBasedKeyValueStore.py) |
| 1448 | Count Good Nodes in Binary Tree | Tree, DFS | [Link](./medium/1448_CountGoodNodesBT.py) |

### Hard (7)

| # | Title | Topics | Solution |
|---|-------|--------|----------|
| 4 | Median of Two Sorted Arrays | Binary Search, Array | [Link](./hard/4_MedianOfTwoArrays.py) |
| 23 | Merge k Sorted Lists | Linked List, Heap | [Link](./hard/23_MergeKSortedLists.py) |
| 25 | Reverse Nodes in k-Group | Linked List | [Link](./hard/25_ReverseInKGroups.py) |
| 42 | Trapping Rain Water | Two Pointers, Stack | [Link](./hard/42_TrappingRainWater.py) |
| 76 | Minimum Window Substring | Sliding Window, Hash Table | [Link](./hard/76_MinWindow.py) |
| 84 | Largest Rectangle in Histogram | Stack, Array | [Link](./hard/84_LargestRectangleHistogram.py) |
| 239 | Sliding Window Maximum | Sliding Window, Deque | [Link](./hard/239_SlidingWindowMaximum.py) |

## In Progress

Problems being worked through in [`todo/`](./todo/), not yet finalized with complexity analysis:
- Determine the Winner of a Bowling Game
- Find Winning Player in Coin Game
- Longest Repeating Character Replacement
- Minimum Hours of Training to Win a Competition
- Minimum Window Substring
- Permutations in String
- Sliding Window Maximum
- Winner of Tic Tac Toe

## Usage

Each solution file is self-contained and can be run independently:
```python
python medium/49_GroupAnagram.py
```

## Complexity Notation

- **Time Complexity**: Expressed using Big O notation (e.g., O(n), O(log n))
- **Space Complexity**: Includes auxiliary space used by the algorithm

## Topics Covered

- Arrays
- Strings
- Hash Tables
- Two Pointers
- Sliding Window
- Stacks
- Binary Search
- Trees (DFS/BFS)
- Linked Lists
- Prefix Sum
- Design (LRU Cache, Min Stack, Time-based KV Store)
- Backtracking

## Contributing

This is a personal learning repository, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## License

MIT License - feel free to use these solutions for learning purposes.

## Connect

- LeetCode Profile: [sharvarikulkarni](https://leetcode.com/u/sharvarikulkarni)
- LinkedIn: [sharvarikulkarni43](https://linkedin.com/in/sharvarikulkarni43)
