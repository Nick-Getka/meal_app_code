__all__ = [
    "Recipe",
    "Ingredient"
    ]

class Ingredient(object):
    def __init__(self, name, amt, measure):
        self.name = name
        self.amt = amt
        self.measure = measure
class Recipe(object)
    def __init__(self, ingredientList):
        self.ingredientList = ingredientList
