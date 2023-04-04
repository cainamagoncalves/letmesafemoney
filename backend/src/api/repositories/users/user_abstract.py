from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    def __init__(self): ...

    @abstractmethod
    def select(): ...
