class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse = True)
        stack = []
        for car in cars:
            p = car[0]
            s = car[1]
            if not stack:
                stack.append((target - p) / s)
            elif (target - p) / s > stack[-1]:
                stack.append((target - p) / s)
        return len(stack)
