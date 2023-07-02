class NaiveSingleton(type):
    __naive_instances__ = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__naive_instances__:
            cls.__naive_instances__[cls] = super().__call__(*args, **kwargs)
        return cls.__naive_instances__[cls]


class Food(metaclass=NaiveSingleton):
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs


if __name__ == "__main__":
    idli: Food = Food("idli", "hospital food.")
    burger: Food = Food("burger", "mc donalds.")

    print(idli.args)
    print(burger.args)
    pass
