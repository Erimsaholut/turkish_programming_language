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

def girdi(input_value=None):
    if input_value is not None:
        return input(input_value)

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
    return max(iterable)


def enKucuk(iterable):
    return min(iterable)


def oldukca(iterable, islem):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            islem(item)
        except StopIteration:
            break


def ac(file, mode):
    if mode == "y":
        mode = "w"
    elif mode == "o":
        mode = "r"
    elif mode == "e":
        mode = "a"
    return open(file, mode)


def kapat(file):
    file.close()


def oku(file):
    return file.read()


def dene(condition, exception_handler=None):
    def func():
        try:
            condition()
        except Exception as err:
            if exception_handler is None:
                yazdir("Hata yakalandı:" + str(err))
            elif exception_handler == 0:
                pass
            else:
                exception_handler()

    func()

