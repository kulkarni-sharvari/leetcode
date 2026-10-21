# 211. Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

################################### Examples ###################################

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

################################### Solution ###################################

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(local_root, startIdx):
            node = local_root
            for i in range(startIdx, len(word)):
                if word[i] == ".":
                    if node.children.values():
                        for child in node.children.values():
                            if dfs(child, i+1):
                                return True
                        return False
                    else:
                        return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]] 
            return node.is_end

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

################################## Complexity ##################################
# addword()
# Time complexity: Θ(len(word))
# space complexity: Θ(len(word))

# search()
# Time complexity: O(B^W*L) where b i sbranching factor, w is number of wildcards and L is len of word.
# Space complexity: O(1)