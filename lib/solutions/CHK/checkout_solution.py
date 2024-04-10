import dataclasses
from collections import Counter
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
    item_list = skus.split()
    if any(x not in list(PRICE_CONFIGS.keys()) for x in item_list):
        return -1

    total_price = 0
    item_counter = dict(Counter(item_list))
    for basket_item in list(item_counter.keys()):
        item = PRICE_CONFIGS.get(basket_item)
        item_quantity = item_counter[basket_item]

        




