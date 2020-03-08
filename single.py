
class Single(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls.__new__(*args, **kwargs)
        return cls.__instance


class mysingel(Single):
    A=1


def singleton(cls):

    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance
    return wrapper
