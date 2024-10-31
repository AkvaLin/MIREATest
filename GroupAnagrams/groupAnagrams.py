from collections import defaultdict
import doctest


def group_anagrams(strs):
    """Return grouped anagrams.

    Usage examples:
    >>> group_anagrams(['eat','tea','tan','ate','nat','bat'])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    >>> group_anagrams([])
    []
    >>> group_anagrams([''])
    [['']]
    >>> group_anagrams(['a'])
    [['a']]
    >>> group_anagrams(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g']]
    >>> group_anagrams(['ade', 'ead', 'eda'])
    [['ade', 'ead', 'eda']]
    >>> group_anagrams(['123', '321', '213'])
    [['123', '321', '213']]
    """

    if not isinstance(strs, list):
        raise ValueError("Не список")
    for current in strs:
        if not isinstance(current, str):
            raise ValueError("Неверный тип")

    temp = defaultdict(list)

    for string in strs:
        letters = list(string)
        letters.sort()
        temp[tuple(letters)].append(string)

    return list(temp.values())

if __name__ == '__main__':
    doctest.testmod()
    
    assert group_anagrams([]) == [], 'Функция работает не верно'
    assert group_anagrams(['']) == [['']], 'Функция работает не верно'
    assert group_anagrams(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g']], 'Функция работает не верно'
    assert group_anagrams(['ade', 'ead', 'eda']) == [['ade', 'ead', 'eda']], 'Функция работает не верно'
    assert group_anagrams(['123', '321', '213']) == [['123', '321', '213']], 'Функция работает не верно'
