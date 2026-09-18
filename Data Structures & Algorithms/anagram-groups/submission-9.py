class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        # res = defaultdict(list)
        # for string in strs:
        #     check = ''.join(sorted(string))
        #     res[check].append(string) 

        # return [value for value in res.values()]

        groups = defaultdict(list)

        for string in strs:

            count = [0]*26

            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)
            groups[key].append(string)

        return list(groups.values())


        