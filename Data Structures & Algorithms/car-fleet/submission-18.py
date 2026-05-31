import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine_positions = sorted(zip(position, speed), reverse=True)

        min_time = (target - combine_positions[0][0]) / combine_positions[0][1]

        max_fleet = 1

        for i in range(1, len(combine_positions)):
            current_time = (target - combine_positions[i][0]) / combine_positions[i][1]
            if current_time > min_time:
                min_time = current_time
                max_fleet += 1

        return max_fleet



        

        
        

       

