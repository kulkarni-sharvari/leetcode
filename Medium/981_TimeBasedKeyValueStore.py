# 981. Time based key-value store - https://leetcode.com/problems/time-based-key-value-store/description/

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"



class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].update({timestamp: value})

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            timestamps = list(self.timemap[key].keys())
            low = 0
            high = len(timestamps) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if timestamps[mid] == timestamp:
                    return self.timemap[key].get(timestamps[mid])
                elif timestamps[mid] < timestamp:
                    low = mid + 1
                else:
                    high = mid - 1
            if high >= 0:
                return self.timemap[key].get(timestamps[high])
            else:
                return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time Complexity:
# - set(): O(1)
# - get(): O(n)
#     - O(n) to create timestamps list
#     - O(log n) for binary search
#     - overall O(n)

# Space Complexity:
# - O(N), where N is the total number of timestamp-value pairs stored.

# Additional Space in get():
# - O(n) temporary space for timestamps list.