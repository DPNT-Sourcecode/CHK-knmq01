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
class FreeItem:
    required_item: str
    required_item_quantity: int


@dataclasses.dataclass
class Item:
    price: int
    offers: Optional[list[Offers]] = None
    free_item: Optional[FreeItem] = None



PRICE_CONFIGS = {
    "A": Item(price=50, offers=[Offers(quantity=3, total_price=130),
                                Offers(quantity=5, total_price=200)]),
    "B": Item(price=30,
              offers=[Offers(quantity=2, total_price=45)],
              free_item=FreeItem(required_item="E", required_item_quantity=2)),
    "C": Item(price=20),
    "D": Item(price=15),
    "E": Item(price=40),
    "F": Item(price=10, offers=[Offers(quantity=3, total_price=20)]),
    "G": Item(price=20),
    "H": Item(price=10, offers=[Offers(quantity=5, total_price=45),
                                Offers(quantity=10, total_price=80)]),
    "I": Item(price=35),
    "J": Item(price=60),
    "K": Item(price=70, offers=[Offers(quantity=2, total_price=120)]),
    "L": Item(price=90),
    "M": Item(price=15, free_item=FreeItem(required_item="N", required_item_quantity=3)),
    "N": Item(price=40),
    "O": Item(price=10),
    "P": Item(price=50, offers=[Offers(quantity=5, total_price=200)]),
    "Q": Item(price=30,
              offers=[Offers(quantity=3, total_price=80)],
              free_item=FreeItem(required_item="R", required_item_quantity=3)),
    "R": Item(price=50),
    "S": Item(price=20),
    "T": Item(price=20),
    "U": Item(price=40, offers=[Offers(quantity=4, total_price=120)]),
    "V": Item(price=50, offers=[Offers(quantity=2, total_price=90),
                                Offers(quantity=3, total_price=130)]),
    "W": Item(price=20),
    "X": Item(price=17),
    "Y": Item(price=20),
    "Z": Item(price=21),
}


def apply_free_item(free_item: FreeItem, item_quantity: int, required_item_basket_quantity: int) -> int:
    """Remove free items from total quantity"""
    if not required_item_basket_quantity or required_item_basket_quantity < free_item.required_item_quantity:
        return item_quantity
    free_items, remainder = divmod(required_item_basket_quantity, free_item.required_item_quantity)
    item_quantity -= free_items

    if item_quantity <= 0:
        return 0
    return item_quantity


def apply_multiple_discounts(discount_list: list[Offers],
                             item_quantity: int,
                             item_price: int):
    sorted_discounts = sorted(discount_list, key=lambda x: x.quantity, reverse=True)

    total_price = 0

    for discount in sorted_discounts:
        if item_quantity >= discount.quantity:
            discounted_price, remainder = discount.apply_discount(total_items=item_quantity)
            total_price += discounted_price
            item_quantity -= (discounted_price // discount.total_price) * discount.quantity
        else:
            continue

    if item_quantity > 0:
        # apply standard price for remainder
        total_price += item_quantity * item_price
    return total_price

def apply_group_buy_discount():



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = list(skus)
    if any(x not in list(PRICE_CONFIGS.keys()) for x in item_list):
        return -1

    total_price = 0

    group_buy_items = ["S","T", "X", "Y", "Z"]


    group_buy_item_list = [x for x in item_list if (x in group_buy_items)]
    non_group_buy_item_list = [x for x in item_list if (x not in group_buy_items)]

    apply_group_buy_discount()


    # Non group buy items
    item_counter = dict(Counter(non_group_buy_item_list))

    for basket_item in list(item_counter.keys()):
        item = PRICE_CONFIGS.get(basket_item)
        item_quantity = item_counter[basket_item]

        if item.free_item is not None:
            item_quantity = apply_free_item(
                free_item=item.free_item,
                item_quantity=item_quantity,
                required_item_basket_quantity=item_counter.get(item.free_item.required_item),
            )
        if item.offers is None:
            total_price += item.price * item_quantity
        else:
            total_price += apply_multiple_discounts(
                discount_list=item.offers,
                item_quantity=item_quantity,
                item_price=item.price,
            )
    return total_price




