import logging


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s")
    try:
        print(1 / 0)
    except Exception as e:
        logging.exception(e)
    else:
        print("- else block -")
    finally:
        print("Any ways")

    print("-" * 80)
