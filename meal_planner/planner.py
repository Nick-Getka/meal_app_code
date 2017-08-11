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
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WListANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WListANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import random
import numpy as np
from copy import copy, deepcopy

from recipe import *
from reranker import *
from datamanager import *


__all__ = [
    "Planner"
]

class Planner(object) :
    def __init__(self) :
        self._rr = Reranker()
        self._db = DataManager()
        self.recipeList = self._db.fetchRecipes()
        return None



    #Meal Selection Methods
    def _random_selection(self, not_master) :
        return random.sample(range(len(not_master)),1)[0]

    def _weighted_selection(self, not_master) :
        sums = []
        weight_sum = 0
        for r in not_master:
            weight_sum += r.weight
            sums.append(weight_sum)
        rnd = random.random() * weight_sum
        for x, s in enumerate(sums) :
            if rnd < s :
                return x

    def select(self, meal_num) :
        not_master = deepcopy(self.recipeList)
        selected = []
        for x in range(meal_num) :
            self._rr.rerank(not_master, selected)
            new_sel = self._weighted_selection(not_master)
            selected.append(not_master[new_sel])
            not_master = np.delete(not_master, new_sel)
        return selected
