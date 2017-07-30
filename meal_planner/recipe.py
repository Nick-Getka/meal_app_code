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
    def __init__(self, amt, measure, name) :
        self.name = name
        self.amt = amt
        self.measure = measure
    def __str__(self) :
        return str(self.amt)+" "+self.measure+" "+self.name

#Basic storage unit for the recipes
class Recipe(object) :
    def __init__(self) :
        self._weight = 1
        self._name = None
        self._ingList = []
        self._fullIngList = []
        return None
    def __init__(self, csvfile) :
        self._weight = 1
        self._name = None
        self._name = None
        self._ingList = []
        self._fullIngList = []
        self.read_csvrow(csvfile)
        return None
    def __str__(self) :
        ret = ""
        if self._name is not None :
            ret += "Name: "+str(self._name)+"\nIngredient List: "
            for y in range(0, len(self._ingList)) :
                ret += str(self._ingList[y]) + "\n"
        else :
            ret = "Empty"
        return ret

    #Getters and Setters
    def get_weight(self) :
        return self._weight
    def set_weight(self, x) :
        self._weight = x
    def get_ingList(self) :
        return self._ingList if self._name != None else None
    def get_fullIngList(self) :
        return self._fullIngList if self._name != None else None
    def get_name(self) :
        return self._name

    #Reads in data
    def read_csvrow(self, row) :
        self._name = row[0]
        for x in range(1, len(row)-2, 3) :
            self._ingList.append(row[x+2])
            self._fullIngList.append(Ingredient(row[x],row[x+1],row[x+2]))
        return None
