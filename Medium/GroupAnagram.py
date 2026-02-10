class Solution:
    def evalAnagramHash(self, string: str) -> dict:
        hash_dict = {}
        for char in string:
            if char in hash_dict:
                hash_dict[char] += 1
            else:
                hash_dict[char] = 1
        return hash_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_anagram = []
        for i in range(len(strs)-1):
            anagrams = [strs[i]]
            for j in range(i+1, len(strs)):
                isAnagram = True
                hash_dict = self.evalAnagramHash(strs[i])
                for char in strs[j]:
                    if char in hash_dict:
                        hash_dict[char] -= 1
                    else:
                        break
                for value in hash_dict.values():
                    if value != 0:
                        isAnagram - False
                        break
                print(isAnagram)
                if(isAnagram):
                    anagrams.append(strs[j])
            final_anagram.append(anagrams)
        return final_anagram
