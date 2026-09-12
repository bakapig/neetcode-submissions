class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_substring = []
        max_length = 0
        

        

        for right in range(len(s)):

            if s[right] in max_substring:


                max_substring = max_substring[max_substring.index(s[right])+1:]

            max_substring += s[right]
            max_length = max(len(max_substring), max_length)

             


            # print(max_substring)

        return max_length


            
        