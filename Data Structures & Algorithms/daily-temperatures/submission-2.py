class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        for current_day, current_temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < current_temp:
                previous_day = stack.pop()
                answer[previous_day] = current_day - previous_day 

            stack.append(current_day)

        
        return answer

        
     