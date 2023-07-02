from typing import Self


class Hooman:
    __identity__: int = 0

    def __new__(cls, f_name: str) -> Self:
        cls.__identity__ += 1
        return object.__new__(cls)

    def __init__(self, f_name: str = "Korangu") -> None:
        self.f_name = f_name
        pass

    @property
    def objects_created(self):
        return self.__identity__

    @classmethod
    def instances(cls):
        return cls.__identity__


a1 = Hooman("pa")
print(a1, a1.objects_created)
a2 = Hooman("ka")
print(a2, a2.objects_created)
a3 = Hooman("pi")
a4 = Hooman("ko")

print(a3, a3.objects_created)
print(a4, a4.objects_created)

print()
print(a1.objects_created)
print(Hooman.instances())
