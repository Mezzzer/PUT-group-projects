import random

class Prisoner():
    def __init__(self) -> None:
        self.actions = ['cooperate', 'defect']

    def testify(self, number_of_future_arrests=None):
        #finite, not known number of arrests
        if number_of_future_arrests==None:
            return random.choice(self.actions)
        #infinite number of arrests
        if number_of_future_arrests=='infinite':
            return random.choice(self.actions)
        #finite but known
        else:
            return random.choice(self.actions)