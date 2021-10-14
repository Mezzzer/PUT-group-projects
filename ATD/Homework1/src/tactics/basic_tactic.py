from abc import abstractmethod


class BasicTactic:
    @abstractmethod
    def get_action(self, **kwargs):
        pass
