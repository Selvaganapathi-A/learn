import datetime
import time

import pytz

if __name__ == "__main__":
    # unix timestamp
    print(time.time())
    # precision from jan-01, 1970
    print(time.time_ns())

    print(2**31)
    print(2**63)

    india = pytz.timezone("Asia/Kolkata")
    utc = pytz.timezone("UTC")

    date = datetime.datetime.fromtimestamp(2**31 - 1, india)
    print("32-bit max time :-", date)
    print("32-bit max time :-", date.astimezone(utc))

    # pprint.pprint(all_timezones)
    # pprint.pprint(common_timezones)

    #
    some_date = datetime.datetime.fromisoformat("2022-02-05T19:40:00")

    utc = pytz.timezone("UTC")
    india = pytz.timezone("Asia/Kolkata")
    alaska = pytz.timezone("US/Alaska")
    seattle = pytz.timezone("America/Los_Angeles")
    sydney = pytz.timezone("Australia/Sydney")

    print()
    print()
    print("              ", some_date)
    print("Universal Time", utc.localize(some_date))
    print("Alask     Time", alaska.localize(some_date))
    print("India     Time", india.localize(some_date))
    print("Seattle   Time", seattle.localize(some_date))
    print("Sydney    Time", sydney.localize(some_date))
    print()

    india_datetime = india.localize(some_date)
    print("time in India   :", india_datetime)
    print("time in Alaska  :", india_datetime.astimezone(alaska))
    print("time in Seattle :", india_datetime.astimezone(seattle))
    print("time in Sydney  :", india_datetime.astimezone(sydney))
    print("time in UTC     :", india_datetime.astimezone(utc))
    print()

    print("Travel in Flight...")
    print()
    alaska_datetime = alaska.localize(some_date)
    sydney_datetime = sydney.localize(some_date)

    print("Depart in india    :", india_datetime)
    print(
        "Arrive Sydney Time :",
        (india_datetime + datetime.timedelta(hours=21)).astimezone(sydney),
    )
    print()

    print("Depart in India   :", india_datetime)
    print(
        "Arrive in Alaska  :",
        (india_datetime + datetime.timedelta(hours=31, minutes=40)).astimezone(alaska),
    )
    print()

    pass
