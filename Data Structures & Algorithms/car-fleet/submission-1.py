class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        stack = []
        car = []
        for i in range(len(position)):
            car.append((position[i],speed[i]))

        car.sort(key = lambda x:x[0], reverse = True)

        for i in range(len(car)):

            time = (target-car[i][0])/car[i][1]

            if stack and stack[-1] >= time:
                pass

            elif stack and stack[-1] < time:
                fleet += 1
                stack.append(time)

            if not stack:
                stack.append(time)
                fleet += 1
        
        return fleet