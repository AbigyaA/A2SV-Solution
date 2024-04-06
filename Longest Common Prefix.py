class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        first=strs[0]
        status=True
        for i in range(len(first)):
            for st in strs:
                try:
                    if first[i] != st[i]:
                        return prefix
                except:
                    status=False
                    continue
            if status:        
                prefix += first[i]
        return prefix
                
