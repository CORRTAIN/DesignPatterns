

class Person(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    print(p1)
    print(p2)