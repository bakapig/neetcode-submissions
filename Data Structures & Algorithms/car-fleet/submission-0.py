class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        previous_time = 0

        for pos, spd in cars:
            current_time = (target-pos)/spd

            if current_time > previous_time:
                fleets += 1
                previous_time = current_time


        return fleets

       



        

        