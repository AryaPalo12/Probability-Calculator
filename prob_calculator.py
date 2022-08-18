import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []

    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self,number):
    if number <= len(self.contents):
      removedBall = []
      for i in range (number):
        removedBall.append(self.contents.pop(random.randrange(len(self.contents))))
      return removedBall
    else:
      return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match = 0
  for i in range (num_experiments):
    yes = True
    test_hat = copy.deepcopy(hat)
    balls_out = test_hat.draw(num_balls_drawn)
    for x in expected_balls :
      if balls_out.count(x) >= expected_balls[x]:
        continue
      else:
        yes = False
    if yes :
      match +=1
  print(match)
  return match / num_experiments
