import dataclasses
from typing import Optional


@dataclasses.dataclass
class Offers:
    quantity: int
    total_price: int

@dataclasses.dataclass
class Item:
    price: int
    offers: Optional[Offers] = None

PRICE_CONFIGS = {
    "A": Item(price=50, offers=Offers(quantity=3, total_price=130)),
    "B": Item(price=30, offers=Offers(quantity=2, total_price=45)),
    "C": Item(price=20),
    "D": Item(price=15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    list_of_items = skus.split()
    if (x not in list(PRICE_CONFIGS.keys()) for x in list_of_items):
        return -1


