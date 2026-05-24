class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_ps = sorted(zip(position, speed), reverse=True)

        times = [(target - pos) / spd for pos, spd in sorted_ps]
        max_fleet = 1
        max_time = times[0]

        for i in range(1, len(times)):
            if times[i] > max_time:
                max_fleet += 1
                max_time = times[i]

        return max_fleet
       

