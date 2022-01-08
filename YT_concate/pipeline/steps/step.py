from abc import ABC
from abc import abstractmethod
# abstract base class


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
