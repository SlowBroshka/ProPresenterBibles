from src.BibHelp.Parser.BibleParser import BibleParser

class Parsers:

    @staticmethod
    def SYNParser():
        return BibleParser(testament=r'^((Новый Завет)|(Ветхий Завет))\n$',
                           book=r'^(\w(\w|-|\.|\s)+?)\n$',
                           chapter=r'^((Глава)|(Псалом))\s+(\d+?)\n$',
                           verse=r'^(\d+)\s(.+?)\n$')

    @staticmethod
    def IBSParser():
        return BibleParser(testament=r'^((Новый Завет)|(Ветхий Завет))\n$',
                           book=r'^(\w(\w|-|\.|\s)+?)\n$',
                           chapter=r'^Глава\s+(\d+?)\n$',
                           verse=r'^(\d+)\s{2,}(.+?)\n$')
