from typing import List, Optional

from eshop.businsess_logic.order import Order

_orders: List[Order] = []


def save(order: Order):
    print(_orders)
    for i in range(len(_orders)):
        existed_order = _orders[i]
        if existed_order.id == order.id:
            _orders[i] = order
            break
    else:
        _orders.append(order)


def get_by_id(id: str) -> Optional[Order]:
    print(_orders)
    return next((o for o in _orders if o.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    print(_orders)
    start = page * limit
    end = start + limit
    print(_orders[start:end])
    return _orders[start:end]