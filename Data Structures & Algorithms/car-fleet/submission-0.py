class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: x[0], reverse=True)

        for position, speed in cars:
            time = (target - position) / speed

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

