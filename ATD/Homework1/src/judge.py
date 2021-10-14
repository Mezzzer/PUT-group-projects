from collections import defaultdict

from utils import Penalty, Actions


class Judge:
    def __init__(self) -> None:
        self.law = defaultdict(dict)
        self.law[Actions.COOPERATE][Actions.COOPERATE] = [Penalty.LOW, Penalty.LOW]
        self.law[Actions.DEFECT][Actions.COOPERATE] = [Penalty.NO_PENALTY, Penalty.HIGH]
        self.law[Actions.COOPERATE][Actions.DEFECT] = [Penalty.HIGH, Penalty.NO_PENALTY]
        self.law[Actions.DEFECT][Actions.DEFECT] = [Penalty.MEDIUM, Penalty.MEDIUM]

    def sentence(self, response_a, response_b):
        return {
            'prisoner_a': self.law[response_a][response_b][0],
            'prisoner_b': self.law[response_a][response_b][1]
        }
