class Pacman:
    def __init__(self, speed):
        self.speed = speed

    # Movement of pacman
    def movement(self):
        pass

    # Make a sound
    def sound(self):
        pass

    # Eat the balls
    def eat(self):
        pass

    # If pacman hits the ghost
    def hit(self):
        pass

    # If the ghost hits pacman
    def got_hit(self):
        pass

    # Respawns pacman
    def respawn(self):
        pass


class Ghost:
    def __init__(self, speed, color, aggression, behaviour):
        self.speed = speed
        self.color = color
        self.aggression = aggression # If the ghost attacks or run away
        self.behaviour = behaviour # How the ghost gets to pacman

    # Movement of the ghost
    def movement(self):
        pass

    # If the ghost hits pacman
    def hit(self):
        pass

    # If pacman hits the ghost
    def got_hit(self):
        pass

    # Respawns the ghost
    def respawn(self):
        pass


pacman = Pacman(20)
pinky = Ghost(15, "pink", True, "suprise")
blinky = Ghost(20, "red", True, "follow")