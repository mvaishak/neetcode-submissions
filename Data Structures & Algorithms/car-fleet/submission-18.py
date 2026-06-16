import heapq
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If (target - position) / speed of car_i >= car_i-1 both are a fleet else separate fleets
        #Use a stack see if cars fleet up and if they do, leave the slower one in the stack
        def catchup(car_a,car_b):
            left_a = target - car_a[0]
            left_b = target - car_b[0]
            speed_a = car_a[1]
            speed_b = car_b[1]
            
            if left_a/speed_a  < left_b/speed_b:
                return True
            else:
                return False

        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        stack = []
        cars.sort(reverse=True)
  
        for i in range(len(position)):
    
            if not stack:
                stack.append(cars[i])
            elif catchup(stack[-1],cars[i]):
                stack.append(cars[i])

        return len(stack)
                
        
