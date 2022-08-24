import random


class TypingToolsError(BaseException):
    def __init__(self, *info):
        self.info = ''.join(str(x) for x in info)
    def __str__(self):
        return self.info


def Int(min_val, max_val):
    if not (isinstance(min_val, int) and isinstance(max_val, int)):
        raise (
            TypingToolsError('Expected (int, int), got (', type(min_val).__name__, ', ', type(max_val).__name__, ')'))
    if min_val >= max_val:
        raise (
            TypingToolsError(min_val, ' >= ', max_val, ' - cannot generate random integer'))
    while True:
        yield random.randint(min_val, max_val)


def Str(chars, length):
    if not hasattr(chars, '__iter__'):
        raise (
            TypingToolsError('Expected Iterable for chars argument, got ', type(chars).__name__))
    if not chars:
        raise (
            TypingToolsError('chars cannot be empty'))
    for i, c in enumerate(chars):
        if not isinstance(c, str):
            raise (
                TypingToolsError('Sequence item ', i, ': expected str, got ', type(c).__name__))
    if not isinstance(length, int):
        raise (
            TypingToolsError('Expected int for length argument, got ', type(length).__name__))
    while True:
        s = ''
        for _ in range(length):
            s += random.choice(chars)
        yield s


def List(items, length):
    if not isinstance(length, int):
        raise (
            TypingToolsError('Expected int for length argument, got ', type(length).__name__))
    while True:
        l = []
        for _ in range(length):
            if hasattr(items, '__next__'):
                l.append(next(items))
            else:
                l.append(items)
        yield l
