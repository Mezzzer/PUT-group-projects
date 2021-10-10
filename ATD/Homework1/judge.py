from collections import defaultdict

class Judge:
    def __init__(self) -> None:
        self.law = defaultdict(dict)
        self.law['cooperate']['cooperate'] = [-1,-1]
        self.law['defect']['cooperate'] = [0,-3]
        self.law['cooperate']['defect'] = [-3,0]
        self.law['defect']['defect'] = [-2,-2]

    def sentence(self, response_A, response_B):
        return self.law[response_A][response_B]
