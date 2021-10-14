from src.prisoners.prisoner import Prisoner
from src.tactics.probabilistic import DependOnKnownHorizon


class KnownPrisoner(Prisoner):
    def __init__(self, name, number_of_future_arrests):
        tactic = DependOnKnownHorizon(tendency_to_defect=0.05,
                                      before_end_threshold=min(3, number_of_future_arrests),
                                      tendency_noise=(0.0, 0.2))
        super(KnownPrisoner, self).__init__(name=name, tactic=tactic, number_of_future_arrests=number_of_future_arrests)

    def change_tendency_to_defect(self):
        number_to_end = self.get_number_to_end()
        self.tactic.change_tendency_to_defect(number_to_end=number_to_end)
