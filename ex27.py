"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    l = [items.count(i) for i in items]
    return dict(zip(items, l))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    item = create_inventory(items)
    for key in inventory:
        if key in items:
            item[key] = item[key] + inventory[key]
        elif key not in items:
            item.update({key: inventory[key]})
        else:
            pass
    return item


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for i in items:
        if inventory[i] == 0:
            continue
        elif i in inventory:
            inventory[i] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    for key in list(inventory):
        if key == item:
            inventory.pop(key)
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # for key in inventory:
    #     print((key, inventory[key]))
    return [(key, inventory[key])for key in inventory if inventory[key] > 0]


print(list_inventory({"coal": 7, "wood": 11,
      "diamond": 2, "iron": 7, "silver": 0}))
#[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
