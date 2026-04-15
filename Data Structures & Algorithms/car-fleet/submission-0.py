class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append(position[i]*10 + speed[i])
        cars.sort()
        stack = []
        for car in cars:
            if len(str(car)) == 1:
                car = '0' + str(car)
            else:
                car = str(car)
            stack.append([int(car[0]), int(car[1])])
        cars_to_target_prev = 0
        fleet = 0
        while True:
            print(stack)
            cars_to_target_now = 0
            
            for i in range(len(stack) - 1, -1, -1):
                if i != len(stack) - 1 and stack[i][0] >= stack[i+1][0]:
                    stack[i][1] = stack[i+1][1]
                if stack[i][0] < target:
                    stack[i][0] = stack[i][0] + stack[i][1]
                elif stack[i][0] >= target:
                    cars_to_target_now += 1
            print(cars_to_target_prev)
            print(cars_to_target_now)
            if cars_to_target_now != cars_to_target_prev:
                fleet += 1
                cars_to_target_prev = cars_to_target_now
            if cars_to_target_prev == len(cars):
                return fleet