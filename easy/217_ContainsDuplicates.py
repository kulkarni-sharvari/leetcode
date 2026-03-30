class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            count = num_dict.get(num, 0)
            if count>0:
                return True
            else:
                num_dict[num] = count+1
        return False

# Time complexity: O(n)
# Space Complexity: O(n)