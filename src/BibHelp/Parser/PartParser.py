import re
from src.BibHelp.BookStructure.BiblePart import BiblePart


class PartParser:

    def __init__(self, pattern: str, match_func):
        self.__pattern = re.compile(pattern)
        self.__match_func = match_func

    def match(self, line: str) -> re.Match:
        return self.__pattern.match(line)

    def from_reg_match(self, match: re.Match) -> BiblePart:
        return self.__match_func(match)