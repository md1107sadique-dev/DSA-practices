class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        longest = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            longest = max(longest, right - left + 1)

        return longest