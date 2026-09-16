class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window_size = len(s1)
        if window_size > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:window_size])
        print(target)
        print(window)

        if window == target:
            return True

        for right in range(window_size, len(s2)):
            # Add new right character 
            window[s2[right]] += 1
            # Remove the old left character
            left = right - window_size
            window[s2[left]] -= 1
            # Remove characters whose count becomes zero
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            if window == target:
                return True

        return False


        

        
        