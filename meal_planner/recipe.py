# The MIT License (MIT)
#
# Copyright (c) 2014-2016 Benedikt Schmitt <benedikt@benediktschmitt.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__all__ = [
    "Recipe",
    "Ingredient"
    ]

#Basic storage unit for the ingredients
class Ingredient(object) :
    def __init__(self, name, measure, amount, db_id) :
        self.name = name
        self.measure = measure
        self.amount = amount
        self.db_id = db_id
    def __str__(self) :
        return str(self.amount)+" "+str(self.measure)+" "+str(self.name)


#Basic storage unit for the recipes
class Recipe(object) :
    def __init__(self, name, ingredientList, db_id) :
        self.weight = 1.0
        self.name = name
        self.ingredientList = ingredientList
        self.db_id = db_id
        return None
    def __str__(self) :
        ret = ""
        ret += "Name: "+str(self.name)+"\nIngredient List: "
        for y in range(0, len(self.ingredientList)) :
            ret += str(self.ingredientList[y]) + "\n"
        return ret

    def getIngredientNames(self) :
        names = []
        for r in self.ingredientList :
            names.append(r.name)
        return names
