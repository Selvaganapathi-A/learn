from dataclasses import dataclass


class PositiveNumber:
    def __set_name__(self, owner: type, name: str):
        print(owner, name)
        self.owner = owner
        self.name = name

    def __get__(self, instance, object_type: type):
        print("called get")
        return instance.__dict__[self.name] if self.name in instance.__dict__ else None

    def __set__(self, instance: object, value):
        if value < 1:
            raise ValueError("Must be Positive Integer", value)
        print("called set with value", value)
        instance.__dict__[self.name] = value


@dataclass
class Apple:
    sold_apples: int = PositiveNumber()  # type: ignore

    def __init__(self, value) -> None:
        self.sold_apples = value
        pass


if __name__ == "__main__":
    a = Apple(109)
    print(a.sold_apples)

    for x in range(4, 8):
        a.sold_apples = x
        print(a.sold_apples)
    pass
