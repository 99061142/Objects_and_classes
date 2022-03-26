import core
import random

class MyCreature(core.Creature):

  def act(self, nearCreatures, nearItems):
    if len(nearCreatures) > 0 and self.attack > 0 and \
      nearCreatures[0].x == self.x and nearCreatures[0].y == self.y:
      self.hit(nearCreatures[0])
    else:
      for i in range(10):
        self.moveLeft()
      
      for i in range(10):
        self.moveRight()

  def __str__(self):
    return f'{self._name} ({self.x} {self.y})'