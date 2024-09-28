import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000 and quantity <= max - min + 1 ):
        return []

    res = set()
    
    while len(res) < quantity:
        res.add(random.randint(min, max))

    return sorted(list(res))
