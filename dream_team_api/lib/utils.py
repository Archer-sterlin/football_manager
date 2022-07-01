import random

import names

from .country_list import COUNTRIES


class Util:
    # Generate age
    @staticmethod
    def generate_age() -> int:
        age: int = random.randrange(18, 41)
        return age

    # Generate player name
    @staticmethod
    def generate_player_name() -> str:
        full_name: str = names.get_full_name(
            gender="male"
        )  # (names.get_full_name(gender='male') for i in range(0, 20))
        return full_name.split(" ")

    # Generate player country
    @staticmethod
    def get_country() -> str:
        country: str = random.choice(COUNTRIES)
        return country[1]

    # Generate shirt number
    @staticmethod
    def generate_shirt_no() -> int:
        shirt_no: int = random.randrange(1, 100)
        return shirt_no

    # incease player value by 10% - 100%
    @staticmethod
    def player_value(value: float) -> float:
        value: float = round((value + (random.uniform(10, 100) / 100 * value)), 2)
        return value
