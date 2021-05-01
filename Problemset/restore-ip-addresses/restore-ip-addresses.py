
# @Title: 复原 IP 地址 (Restore IP Addresses)
# @Author: 18015528893
# @Date: 2021-02-12 12:39:55
# @Runtime: 64 ms
# @Memory: 15 MB

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if not 4 <= len(s) <= 12:
            return result

        def backtrack(path, split_times, begin):
            if split_times == 4 and begin == len(s):
                result.append('.'.join(path))
                return

            for i in range(1, 4):
                part = s[begin: begin+i]
                if len(part) == 0 or (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                begin += i
                backtrack(path, split_times+1, begin)
                path.pop()
                begin -= i

        backtrack([], 0, 0)
        return result 
