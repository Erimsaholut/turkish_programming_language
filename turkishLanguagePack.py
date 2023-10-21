def tamSayi(input_value):
    try:
        return int(input_value)
    except ValueError:
        return None


def ondalikliSayi(input_value):
    try:
        return float(input_value)
    except ValueError:
        return None


def dizgi(input_value):
    try:
        return str(input_value)
    except ValueError:
        return None


def dogrulukDegeri(input_value):
    if isinstance(input_value, bool):
        return input_value
    if isinstance(input_value, str):
        input_value = input_value.lower()
        if input_value == "true":
            return True
        elif input_value == "false":
            return False
    return None


def yazdir(input_value=None):
    if input_value is not None:
        print(input_value)


def aralik(start, stop, step=1):
    if step == 0:
        raise ValueError("Adım (step) sıfır olamaz.")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


def her(iterable, islem):
    for item in iterable:
        islem(item)


def eger(koşul, işlem, else_işlem=None):
    if koşul:
        işlem()
    elif else_işlem:
        else_işlem()


def enBuyuk(iterable):
    if len(iterable) == 0:
        raise ValueError("Iterable boş olamaz.")
    max_value = iterable[0]
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value


def enKucuk(iterable):
    if len(iterable) == 0:
        raise ValueError("Iterable boş olamaz.")
    min_value = iterable[0]
    for item in iterable:
        if item < min_value:
            min_value = item
    return min_value


def oldukca(iterable, islem):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            islem(item)
        except StopIteration:
            break
