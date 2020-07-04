# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class Game:
    def __init__(self, dress, color, height, speed):
        self.dress = dress
        self.color = color
        self.height = height
        self.speed = speed

    def properties(self):
        print('The dress code is ',self.dress)
        print('Color is ', self.color)
        print('Height is ',self.height)
        print('Speed is ', self.speed)

mario = Game('shirt', 'white', 'short', 'fast')
mario.properties()