class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = s.replace(" ", "")

        cleaned_text = list("".join([char.lower() for char in text if char.isalnum()]))
        print(cleaned_text)

        if cleaned_text == cleaned_text[::-1]:
            return True
        else:
            return False

        