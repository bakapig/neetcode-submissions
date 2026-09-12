class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        res = defaultdict(list)
        final = []


        for string in strs:
            check = ''.join(sorted(string))
            res[check].append(string) 

        return [value for value in res.values()]



        