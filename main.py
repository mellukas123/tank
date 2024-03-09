from random import randint
import main_functions as fns

directions = {'w':'up', 's':'down', 'a':'right', 'd':'left'}

class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'up'

    def __str__(self):
        return f"Current tank position is [{self.x}, {self.y}] and it is facing {self.direction}"

    def move(self, direction):
        if direction in directions.values():
            if direction == 'up':
                if self.y < 5:
                    self.y += 1
                else:
                    print("Coordinate can not be over 5!")
            elif direction == 'down':
                if self.y > -5:
                    self.y -= 1
                else:
                    print("Coordinate can not be over 5!")
            elif direction == 'left':
                if self.x > -5:
                    self.x -= 1
                else:
                    print("Coordinate can not be over 5!")
            elif direction == 'right':
                if self.x < 5:
                    self.x += 1
                else:
                    print("Coordinate can not be over 5!")
            self.direction = direction
        else:
            print("Not present :(")

    def shoot(self, targetX, targetY):
        return True


class Target:
    def __init__(self):
        self.x = randint(-5, 5)
        self.y = randint(-5, 5)

    def __str__(self):
        return f'Target position is {self.x}, {self.y}'
    def reset(self):
        self.x = randint(-5, 5)
        self.y = randint(-5,5)


tank = Tank()
target = Target()
# Making sure if tank and target are not in the same place
while tank.x == target.x and target.y == target.y:
    target.reset()

while True:
    main_action = fns.initial_user_input()
    if main_action == '1':
        print("Welcome to the tanks game, let's GOOO!")
        while True:
            tank_move = fns.tm_input()
            if tank_move == "t":
                if tank.shoot(target.x, target.y):
                    while tank.x == target.x and target.y == target.y:
                        target.reset()
                    else:
                        print("Missed the target :P")
            tank.move(directions[tank_move])
            print(tank)
            print(target)
    elif main_action == '2':
        print("The previous results:")
    elif main_action == '3':
        print("Getting a username")
        print("Saving the username and the score")