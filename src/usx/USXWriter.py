from abc import ABC, abstractmethod

class AbstractUSXWriter(ABC):
    USX_EXTENSION = '.usx'

    def __init__(self, current_work_dir: str):
        self.code_to_name_map = {}
        self.cwd = current_work_dir

    @abstractmethod
    def start_book(self, alias: str, name: str) -> str:
        return ""

    @abstractmethod
    def end_book(self, alias: str, name: str) -> str:
        return ""

    @abstractmethod
    def start_chapter(self, number: int) -> str:
        return ""

    @abstractmethod
    def end_chapter(self, number: int) -> str:
        return ""

    @abstractmethod
    def start_verse(self, number: int, content: str) -> str:
        return ""

    @abstractmethod
    def end_verse(self, number: int, content: str) -> str:
        return ""

    @abstractmethod
    def generate_metadata(self) -> str:
        pass

    def add_book(self, code: str, name: str):
        self.code_to_name_map[code] = name
