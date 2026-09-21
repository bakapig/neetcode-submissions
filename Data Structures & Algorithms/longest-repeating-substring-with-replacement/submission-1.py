class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import Counter

        left = 0
        max_length = 0
        count = Counter()

        for right in range(len(s)):
            count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # right - left + 1 = current window length
            # max(count.values()) the frequency of most common character
            # replacements_needed = window_length - highest_frequency
            # Do we need more replacements than k allows?
#             count = Counter()
# left = 0

# for right in range(len(s)):
#     count[s[right]] += 1

#     while window_length - highest_frequency > k:
#         remove s[left]
#         left += 1

#     update longest

            max_length = max(max_length, right-left+1)
        
        return max_length