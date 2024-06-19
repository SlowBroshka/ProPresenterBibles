import re
from src.BibHelp.BookStructure.BiblePart import BiblePart


class Verse(BiblePart):
    __clean_patterns = {re.compile(r' {2,}'): ' ', re.compile(r'<pb/>'): '', re.compile(r'</t>'): '',
                        re.compile(r'<t>'): '', re.compile(r'<i>'): '', re.compile(r'</i>'): '',
                        re.compile(r'<j>'): '', re.compile(r'</j>'): '',
                        re.compile(r'<e>'): '', re.compile(r'</e>'): '', re.compile(r'<f>.+?</f>'): ''}

    def __init__(self, number: int, content: str):
        self.number = number
        self.content = BiblePart.clean_content(Verse.__clean_patterns, content)

    @classmethod
    def from_reg_exp(self, match: re.Match):
        verse_num = int(match.group(1))
        verse_content = match.group(2)
        return self(verse_num, verse_content)

    def print(self):
        print(f'[Verse] {self.number} {self.content}')

    def __eq__(self, item):
        if isinstance(item, Verse):
            return self.number == item.number and self.content == item.content
        raise TypeError(f'Invalid type')
