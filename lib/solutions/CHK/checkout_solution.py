import dataclasses
from collections import Counter
from typing import Optional


@dataclasses.dataclass
class Offers:
    quantity: int
    total_price: int

    def apply_discount(self, total_items: int) -> tuple[int, int]:
        bundled_sets, remainder = divmod(total_items, self.quantity)
        discounted_price = bundled_sets * self.total_price
        return discounted_price, remainder


@dataclasses.dataclass
class Item:
    price: int
    offers: Optional[list[Offers]] = None


PRICE_CONFIGS = {
    "A": Item(price=50, offers=[Offers(quantity=3, total_price=130),
                                Offers(quantity=5, total_price=200)]),
    "B": Item(price=30, offers=[Offers(quantity=2, total_price=45)]),
    "C": Item(price=20),
    "D": Item(price=15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = list(skus)
    if any(x not in list(PRICE_CONFIGS.keys()) for x in item_list):
        return -1

    total_price = 0
    item_counter = dict(Counter(item_list))
    for basket_item in list(item_counter.keys()):
        item = PRICE_CONFIGS.get(basket_item)
        item_quantity = item_counter[basket_item]

        if item.offers is None:
            total_price += item.price * item_quantity
        else:
            discounted_price, remainder = item.offers.apply_discount(total_items=item_quantity)
            total_price += discounted_price
            total_price += item.price * remainder
    return total_price

