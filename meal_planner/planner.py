from . import argparse_ as ap

__all__ = [
    "MealPlanner"
]

class MealPlanner(object):
    def __init__(self):
        self._args = ap.ArgParser().get_args(cache=False)
        self.meal_num = self._args.meal_count
        self.read_type = self._args.read_type
        self.data_path = self._args.data_path

        print self.meal_num+" "+self.read_type+" "+self.data_path
