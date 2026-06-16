class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = [] 
        for i in range(len(position)):
            current_time = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(current_time)
            elif current_time > stack[-1]:
                stack.append(current_time)
        return len(stack)