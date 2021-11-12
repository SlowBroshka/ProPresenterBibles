from abc import ABC, abstractmethod

from src.BibHelp.Bible import Bible


class AbstractDump(ABC):

    def __init__(self, bible: Bible):
        self.bible = bible

    @abstractmethod
    def dump(self, path: str):
        pass
