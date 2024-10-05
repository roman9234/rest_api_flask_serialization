import uuid
from typing import List, Optional

from eshop.model.order import Order
from eshop.data_access.order_repo import save, get_by_id, get_many
from eshop.data_access.product_repo import get_by_id as product_get_by_id

# Создаёт Order со сгенерированным uuid4
# product_ids - id продуктов. Могут быть несколько одинаковых
# total - сумма цен продуктов
# Возвращет созданный Order
def order_create(product_ids: List[str]) -> Order:
    products = []
    for id in product_ids:
        product = product_get_by_id(id)
        if product is None:
            raise Exception(f'Could not create order: Product with id {id} not exists')

        products.append(product)

    total = sum([p.price for p in products])

    order = Order(
        id=str(uuid.uuid4()),
        product_ids=product_ids,
        total=total,
    )
    save(order)

    return order

# Возвращает Order,если он есть в БД, инаце возвращает None
def order_get_by_id(id: str) -> Optional[Order]:
    return get_by_id(id)


def order_get_many(page: int, limit: int) -> List[Order]:
    return get_many(page=page, limit=limit)
