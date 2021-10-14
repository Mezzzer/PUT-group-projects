from enum import Enum


class Actions(Enum):
    COOPERATE = 'cooperate'
    DEFECT = 'defect'


class Penalty(Enum):
    NO_PENALTY = 0
    LOW = -1
    MEDIUM = -2
    HIGH = -3
