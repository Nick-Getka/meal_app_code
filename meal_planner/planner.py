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

import csv
import random
import pprint as pp
import numpy as np

from argparse_ import *
from recipe import *


__all__ = [
    "MealPlanner"
]

class MealPlanner(object) :
    def __init__(self) :
        args = ArgParser().get_args(cache=False)
        self._meal_num = args.meal_count
        self._read_type = args.read_type
        self._data_path = args.data_path
        self._recipeArr = []
        return None

    #Innerclass used to keep ranking easy
    class RankRecipe(object) :
        def __init__(self, rec) :
            self._rank = 1
            self._recipe = rec if type(rec) == 'Recipe' else Recipe(rec)
            return None
        def get_recipe(self):
            return self._recipe
        def get_ing(self) :
            return self.recipe.get_ingList

    #Getters and Setters
    def get_meal_num(self) :
        return self._meal_num
    def get_read_type(self) :
        return self._read_type
    def read_from_csv(self, path) :
        self._read_type = "csv"
        self._data_path = path
        load_data()
        return None
    def read_from_db() :
        self._read_type = "db"
        load_data()
        return None

    #Loading Data Methods
    def load_data(self) :
        if len(self._recipeArr) == 0:
            self.load_csv() if self._read_type == "csv"  else self.load_db()
        return None
    def load_csv(self) :
        with open(self._data_path, 'rb') as csvfile :
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader :
                self._recipeArr.append(self.RankRecipe(row))
        return None
    def load_db(self) :
        print "Loading data from database not implemented yet"
        return None

    #Meal Selection Methods
    def random_selection(self) :
        not_master = np.asarray(self._recipeArr)
        choice = random.sample(range(len(not_master)), self._meal_num)
        for z in choice :
            print not_master[z].get_recipe()

    #VSM Reranking next
