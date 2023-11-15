import abc


class BiblePart(abc.ABC):

    @abc.abstractmethod
    def print(self):
        pass

    @staticmethod
    def clean_content(patterns: dict, content: str) -> str:
        """
        Some string in translate has double spaces,
        and maybe other not good readable parts
        Use regexp patterns to fix it.
        :param patterns: dict{regex -> replaced str}
        :param content:
        :return:
        """
        for pattern, replaced in patterns.items():
            content = pattern.sub(replaced, content)
        return content
