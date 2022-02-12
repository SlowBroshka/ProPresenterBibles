class BookName:

    def __init__(self, aliases: list, ntc_ru_long: str, ntc_en_long: str, en_abbr: str):
        self.aliases = aliases
        self.ntc_ru_long = ntc_ru_long
        self.ntc_en_long = ntc_en_long
        self.en_abbr = en_abbr

    def has_alias(self, alias: str) -> bool:
        return alias in self.aliases or alias == self.ntc_en_long

    def to_str(self):
        return f'{self.ntc_ru_long}: {self.en_abbr}'


class BookInBible:

    def __init__(self, book: BookName, index: int):
        self.book = book
        self.index = index


class BookNameManager:

    @staticmethod
    def book_name(name: str) -> BookName:
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return bookName
        raise NameError(f'[ERROR]: Can\'t map book: [{name}]')

    @staticmethod
    def index_in_bible(name: str) -> int:
        index = 1
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return index
            index += 1
        raise NameError(f'[ERROR]: Can\'t find book by name: [{name}]')

    @staticmethod
    def book_in_bible(name: str) -> BookInBible:
        index = 1
        for bookName in BookNameManager.all_books:
            if bookName.has_alias(name):
                return BookInBible(bookName, index)
            index += 1
        raise NameError(f'[ERROR]: Can\'t map book: [{name}]')

    all_books = [
        BookName(['Бытие'], 'Бытие', 'Genesis', 'GEN'),
        BookName(['Исход'], 'Исход', 'Exodus', 'EXO'),
        BookName(['Левит'], 'Левит', 'Leviticus', 'LEV'),
        BookName(['Числа'], 'Числа', 'Numbers', 'NUM'),
        BookName(['Второзаконие'], 'Второзаконие', 'Deuteronomy', 'DEU'),
        BookName(['Иисус Навин', 'Книга Иисуса Навина'], 'Иисус Навин', 'Joshua', 'JOS'),
        BookName(['Судьи', 'Книга Судей израилевых'], 'Судьи', 'Judges', 'JDG'),
        BookName(['Руфь', 'Книга Руфи'], 'Руфь', 'Ruth', 'RUT'),
        BookName(['1 Царств', '1-я Царств', 'Первая книга Царств [Первая Самуила]'], '1 Царств', '1 Samuel',
                 '1SA'),
        BookName(['2 Царств', '2-я Царств', 'Вторая книга Царств [Вторая Самуила]'], '2 Царств', '2 Samuel',
                 '2SA'),
        BookName(['3 Царств', '3-я Царств', 'Третья книга Царств [Первая Царей]'], '3 Царств', '1 Kings',
                 '1KI'),
        BookName(['4 Царств', '4-я Царств', 'Четвертая книга Царств [Вторая Царей]'], '4 Царств', '2 Kings',
                 '2KI'),
        BookName(['1 Паралипоменон', '1-я Паралипоменон', 'Первая книга Паралипоменон'],
                 '1 Паралипоменон', '1 Chronicles', '1CH'),
        BookName(['2 Паралипоменон', '2-я Паралипоменон', 'Вторая книга Паралипоменон'],
                 '2 Паралипоменон', '2 Chronicles', '2CH'),
        BookName(['Ездра', 'Первая книга Ездры'], 'Ездра', 'Ezra', 'EZR'),
        BookName(['Неемия', 'Книга Неемии'], 'Неемия', 'Nehemiah', 'NEH'),
        BookName(['Есфирь', 'Книга Есфири'], 'Есфирь', 'Esther', 'EST'),
        BookName(['Иов', 'Книга Иова'], 'Иов', 'Job', 'JOB'),
        BookName(['Псалтирь', 'Psalm'], 'Псалтирь', 'Psalms', 'PSA'),
        BookName(['Притчи', 'Притчи Соломона'], 'Притчи', 'Proverbs', 'PRO'),
        BookName(['Екклесиаст', 'Книга Екклезиаста, или Проповедника'], 'Екклесиаст', 'Ecclesiastes', 'ECC'),
        BookName(['Песня Песней', 'Песнь песней Соломона'], 'Песня Песней', 'Song of Songs', 'SNG'),
        BookName(['Исаия', 'Книга пророка Исаии'], 'Исаия', 'Isaiah', 'ISA'),
        BookName(['Иеремия', 'Книга пророка Иеремии'], 'Иеремия', 'Jeremiah', 'JER'),
        BookName(['Плач Иеремии'], 'Плач Иеремии', 'Lamentations', 'LAM'),
        BookName(['Иезекииль', 'Книга пророка Иезекииля'], 'Иезекииль', 'Ezekiel', 'EZK'),
        BookName(['Даниил', 'Книга пророка Даниила'], 'Даниил', 'Daniel', 'DAN'),
        BookName(['Осия', 'Книга пророка Осии'], 'Осия', 'Hosea', 'HOS'),
        BookName(['Иоиль', 'Книга пророка Иоиля'], 'Иоиль', 'Joel', 'JOL'),
        BookName(['Амос', 'Книга пророка Амоса'], 'Амос', 'Amos', 'AMO'),
        BookName(['Авдий', 'Книга пророка Авдия'], 'Авдий', 'Obadiah', 'OBA'),
        BookName(['Иона', 'Книга пророка Ионы'], 'Иона', 'Jonah', 'JON'),
        BookName(['Михей', 'Книга пророка Михея'], 'Михей', 'Micah', 'MIC'),
        BookName(['Наум', 'Книга пророка Наума'], 'Наум', 'Nahum', 'NAM'),
        BookName(['Аввакум', 'Книга пророка Аввакума'], 'Аввакум', 'Habakkuk', 'HAB'),
        BookName(['Софония', 'Книга пророка Софонии'], 'Софония', 'Zephaniah', 'ZEP'),
        BookName(['Аггей', 'Книга пророка Аггея'], 'Аггей', 'Haggai', 'HAG'),
        BookName(['Захария', 'Книга пророка Захарии'], 'Захария', 'Zechariah', 'ZEC'),
        BookName(['Малахия', 'Книга пророка Малахии'], 'Малахия', 'Malachi', 'MAL'),
        BookName(['От Матфея', 'От Матфея святое благовествование'], 'От Матфея', 'Matthew', 'MAT'),
        BookName(['От Марка', 'От Марка святое благовествование'], 'От Марка', 'Mark', 'MRK'),
        BookName(['От Луки', 'От Луки святое благовествование'], 'От Луки', 'Luke', 'LUK'),
        BookName(['От Иоанна', 'От Иоанна святое благовествование'], 'От Иоанна', 'John', 'JHN'),
        BookName(['Деяния', 'Деяния святых апостолов'], 'Деяния', 'Acts', 'ACT'),
        BookName(['К Римлянам', 'Послание к Римлянам святого апостола Павла'], 'К Римлянам', 'Romans', 'ROM'),
        BookName(['1 Коринфянам', '1-е Коринфянам', 'Первое послание к Коринфянам святого апостола Павла'],
                 '1 Коринфянам', '1 Corinthians',
                 '1CO'),
        BookName(['2 Коринфянам', '2-е Коринфянам', 'Второе послание к Коринфянам святого апостола Павла'],
                 '2 Коринфянам', '2 Corinthians',
                 '2CO'),
        BookName(['К Галатам', 'Послание к Галатам святого апостоля Павла'], 'К Галатам', 'Galatians', 'GAL'),
        BookName(['К Ефесянам', 'Послание к Ефесянам святого апостола Павла'], 'К Ефесянам', 'Ephesians', 'EPH'),
        BookName(['К Филиппийцам', 'Послание к Филиппийцам святого апостола Павла'], 'К Филиппийцам', 'Philippians',
                 'PHP'),
        BookName(['К Колоссянам', 'Послание к Колоссянам святого апостола Павла'], 'К Колоссянам', 'Colossians', 'COL'),
        BookName(['1 Фессалоникийцам', '1-е Фессалоникийцам',
                  'Первое послание к Фессалоникийцам (Солунянам) святого апостола Павла'], '1 Фессалоникийцам',
                 '1 Thessalonians', '1TH'),
        BookName(['2 Фессалоникийцам', '2-е Фессалоникийцам',
                  'Второе послание к Фессалоникийцам (Солунянам) святого апостола Павла'], '2 Фессалоникийцам',
                 '2 Thessalonians', '2TH'),
        BookName(['1 Тимофею', '1-е Тимофею', 'Первое послание к Тимофею святого апостола Павла'], '1 Тимофею',
                 '1 Timothy', '1TI'),
        BookName(['2 Тимофею', '2-е Тимофею', 'Второе послание к Тимофею святого апостола Павла'], '2 Тимофею',
                 '2 Timothy', '2TI'),
        BookName(['К Титу', 'Послание к Титу святого апостола Павла'], 'К Титу', 'Titus', 'TIT'),
        BookName(['К Филимону', 'Послание к Филимону святого апостола Павла'], 'К Филимону', 'Philemon', 'PHM'),
        BookName(['К Евреям', 'Послание к Евреям святого апостола Павла'], 'К Евреям', 'Hebrews', 'HEB'),
        BookName(['Иакова', 'Соборное послание святого апостола Иакова'], 'Иакова', 'James', 'JAS'),
        BookName(['1 Петра', '1-е Петра', 'Первое соборное послание святого апостола Петра'], '1 Петра', '1 Peter',
                 '1PE'),
        BookName(['2 Петра', '2-е Петра', 'Второе соборное послание святого апостола Петра'], '2 Петра', '2 Peter',
                 '2PE'),
        BookName(['1 Иоанна', '1-е Иоанна', 'Первое соборное послание святого апостола Иоанна'], '1 Иоанна', '1 John',
                 '1JN'),
        BookName(['2 Иоанна', '2-е Иоанна', 'Второе соборное послание святого апостола Иоанна'], '2 Иоанна', '2 John',
                 '2JN'),
        BookName(['3 Иоанна', '3-е Иоанна', 'Третье соборное послание святого апостола Иоанна'], '3 Иоанна', '3 John',
                 '3JN'),
        BookName(['Иуды', 'Соборное послание святого апостола Иуды'], 'Иуды', 'Jude', 'JUD'),
        BookName(['Откровение', 'Откровение святого Иоанна Богослова (Апокалипсис)'], 'Откровение', 'Revelation', 'REV')
    ]
