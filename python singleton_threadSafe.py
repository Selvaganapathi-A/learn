from threading import Lock, Thread


class NaiveSingleton(type):
    __naive_instances__ = {}
    __threadLock__ = Lock()

    def __call__(cls, *args, **kwargs):
        with cls.__threadLock__:
            if cls not in cls.__naive_instances__:
                cls.__naive_instances__[cls] = super().__call__(*args, **kwargs)
        return cls.__naive_instances__[cls]


class Entertainment(metaclass=NaiveSingleton):
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs


def test_singleton(*args, lock: Lock, **kwargs):
    with lock:
        device = Entertainment(*args, **kwargs)
        print(lock)
        print(device.args)
        print(device.kwargs)


if __name__ == "__main__":
    lock = Lock()
    t1 = Thread(
        target=test_singleton,
        args=("speaker", "play songs"),
        kwargs={"lock": lock, "device_id": 8979},
    )
    # t1.daemon = True
    t1.start()

    t2 = Thread(
        target=test_singleton,
        args=("mobile", "blood sucker"),
        kwargs={"lock": lock, "device_id": 4552},
    )
    # t2.daemon = True
    t2.start()
