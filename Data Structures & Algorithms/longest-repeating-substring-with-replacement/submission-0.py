class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import Counter

        left = 0
        max_length = 0
        count = Counter()

        for right in range(len(s)):
            count[s[right]] += 1

            # Number of characters that must be replaced
            # max(count.values()is the highest frequency
            replacements = (
                (right-left+1)-max(count.values())
            )


            while replacements>k:
                count[s[left]]-=1
                left+=1

                replacements = (
                    (right - left + 1) - max(count.values())
                )



            max_length = max(max_length, right-left+1)
        
        return max_length