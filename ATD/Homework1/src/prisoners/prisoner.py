from abc import abstractmethod

from utils import Penalty


class Prisoner:
    def __init__(self, name, tactic, number_of_future_arrests=None):
        self.name = name
        self.tactic = tactic
        self.number_of_future_arrests = number_of_future_arrests
        self.performed_judgement = 0
        self.list_of_sentences = list()

    def serve_sentence(self, penalty_amount):
        self.list_of_sentences.append(penalty_amount)

    def testify(self):
        self.performed_judgement += 1
        self.change_tendency_to_defect()
        print(f'Prisoner {self.name} has a tendency defeat score: {self.tactic.tendency_to_defect}')
        return self.tactic.get_action()

    @abstractmethod
    def change_tendency_to_defect(self):
        pass

    def get_anger_at_the_opponent(self, gamma):
        anger = 0.0
        for factor, sentence in enumerate(self.list_of_sentences[::-1]):
            anger += sentence.value * (gamma ** factor)

        return self.normalize_anger(anger)

    def normalize_anger(self, anger):
        if self.list_of_sentences:
            return anger / (len(self.list_of_sentences) * Penalty.HIGH.value)
        else:
            return 0.0

    def get_number_to_end(self):
        return self.number_of_future_arrests - self.performed_judgement

    @property
    def number_of_low_penalties(self):
        return self.list_of_sentences.count(Penalty.LOW)

    @property
    def number_of_medium_penalties(self):
        return self.list_of_sentences.count(Penalty.MEDIUM)

    @property
    def number_of_high_penalties(self):
        return self.list_of_sentences.count(Penalty.HIGH)

    @property
    def number_without_penalties(self):
        return self.list_of_sentences.count(Penalty.NO_PENALTY)
