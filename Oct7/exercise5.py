def item_lister(items):
    items[0] = "First item"
    items[1] = items[0]
    items[2] = items[2] + 1
    print(items)


item_lister([2, 4, 6, 8])
