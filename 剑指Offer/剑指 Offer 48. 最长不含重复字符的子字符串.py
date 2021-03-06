class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        record = dict()
        max_length = 1
        cur_length = 0
        ind = 0
        while ind < len(s):
            char = s[ind]
            if char in record:
                max_length = max(ind - record[char], max_length)
                ind = record[char] + 1
                cur_length = 0
                record.clear()
                continue
            record[char] = ind
            print(char)
            cur_length += 1
            max_length = max(cur_length, max_length)
            ind += 1
        return max_length
