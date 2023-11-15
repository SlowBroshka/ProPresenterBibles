from abc import ABC, abstractmethod

from src.BibHelp.Parser.PartParser import PartParser


class IBiblePartParser(ABC):

    @abstractmethod
    def testament_parser(self) -> PartParser:
        pass

    @abstractmethod
    def book_parser(self) -> PartParser:
        pass

    @abstractmethod
    def chapter_parser(self) -> PartParser:
        pass

    @abstractmethod
    def verse_parser(self) -> PartParser:
        pass
