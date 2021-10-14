from random import uniform

from src.prisoners.prisoner import Prisoner
from src.tactics.probabilistic import DependentOnOpponent


class UnknownPrisoner(Prisoner):
    def __init__(self, name, number_of_future_arrests):
        tactic = DependentOnOpponent(tendency_to_defect=uniform(0.1, 0.6))
        super(UnknownPrisoner, self).__init__(name=name,
                                              number_of_future_arrests=number_of_future_arrests,
                                              tactic=tactic)
        self.forgetfulness_factor = 0.9

    def change_tendency_to_defect(self):
        anger = self.get_anger_at_the_opponent(self.forgetfulness_factor)
        self.tactic.change_tendency_to_defect(new_tendency=anger)
