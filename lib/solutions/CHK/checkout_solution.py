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
}

def apply_free_item(free_item: FreeItem, item_quantity: int, required_item_basket_quantity: int) -> int:
    """Remove free items from total quantity"""
    if not required_item_basket_quantity or required_item_basket_quantity < free_item.required_item_quantity:
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
            item_quantity -= discount.quantity
        else:
            continue

    if item_quantity > 0:
        # apply standard price for remainder
        total_price += item_quantity * item_price
    return total_price


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
            apply_multiple_discounts(
                discount_list=item.offers,
                item_quantity=item_quantity,
                item_price=item.price,
            )
    return total_price




