import random

class RunningAverage:
  def __init__(self):
    self.data = []
    self.denominator = 0

  def add(self, datum):
    self.data.append(datum)
    self.denominator += 1

  def value(self):
    if self.denominator == 0:
      return None
    return sum(self.data) / self.denominator

LOWEST_RATING = 1
HIGHEST_RATING = 10
def get_desired_rating():
  # return random.choice([7, 9])
  return random.choice([3, 6, 7])

def do_vote(average):
  """ Mutates its *average* argument."""
  current_rating = average.value()
  desired_rating = get_desired_rating()

  if current_rating is None:
    # If you're the first voter, vote honestly.
    average.add(desired_rating)
  elif desired_rating < current_rating:
    average.add(LOWEST_RATING)
  elif desired_rating > current_rating:
    average.add(HIGHEST_RATING)
  else:
    # If the desired_rating is exactly what we've already got, vote honestly.
    average.add(desired_rating)

if __name__ == "__main__":
  average = RunningAverage()
  for _ in range(10**3):
    do_vote(average)

  print(average.value())
