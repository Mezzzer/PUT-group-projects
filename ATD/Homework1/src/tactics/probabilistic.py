import random
from abc import abstractmethod

from utils import Actions


class BasicTactic:
    def __init__(self, tendency_to_defect):
        self.tendency_to_defect = tendency_to_defect

    @abstractmethod
    def get_action(self):
        pass

    @abstractmethod
    def change_tendency_to_defect(self, **kwargs):
        pass

    @property
    def actions_with_prob(self):
        return {
            Actions.DEFECT: self.tendency_to_defect,
            Actions.COOPERATE: 1 - self.tendency_to_defect
        }

    @property
    def actions(self):
        return list(self.actions_with_prob.keys())

    @property
    def actions_weights(self):
        return tuple(self.actions_with_prob.values())


class DependentOnOpponent(BasicTactic):
    def __init__(self, tendency_to_defect):
        super(DependentOnOpponent, self).__init__(tendency_to_defect)

    def get_action(self):
        return random.choices(self.actions, weights=self.actions_weights, k=1)[0]

    def change_tendency_to_defect(self, new_tendency):
        if new_tendency > 0.0:
            weight = 1.5
            temp = (weight * self.tendency_to_defect) + new_tendency
            denominator = weight + 1
            temp /= denominator
            self.tendency_to_defect = temp


class DependOnKnownHorizon(BasicTactic):
    def __init__(self, tendency_to_defect, before_end_threshold, tendency_noise):
        super(DependOnKnownHorizon, self).__init__(tendency_to_defect)
        self.before_end_threshold = before_end_threshold
        self.tendency_noise = tendency_noise

    def change_tendency_to_defect(self, number_to_end):
        if number_to_end < self.before_end_threshold:
            self.tendency_to_defect = (self.before_end_threshold - number_to_end) / self.before_end_threshold
            self.tendency_to_defect -= random.uniform(*self.tendency_noise)

    def get_action(self):
        return random.choices(self.actions, weights=self.actions_weights, k=1)[0]



