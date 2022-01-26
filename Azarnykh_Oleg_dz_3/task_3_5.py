from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    counter = 0
    list_out = []
    while counter < count:
        some_joke = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}']
        list_out += some_joke
        counter += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, **kwargs: bool) -> list:
    """Возвращает список оригинальных шуток в количестве count"""
    no_repeats = kwargs.get('no_repeats', False)
    if no_repeats is False:
        return get_jokes(count)
    else:
        counter = 0
        list_out = []
        while counter < count and len(nouns) != 0 and len(adverbs) != 0 and len(adjectives) != 0:
            some_joke = [
                f'{nouns.pop(randrange(len(nouns)))} '
                f'{adverbs.pop(randrange(len(adverbs)))} '
                f'{adjectives.pop(randrange(len(adjectives)))}']
            list_out += some_joke
            counter += 1
        return list_out


print(get_jokes_adv(8))
print(get_jokes_adv(5, no_repeats=True))
