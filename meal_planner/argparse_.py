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

import argparse

__all__ = [
    "ArgParser"
]

#argparse wrapper used to set the command line arguments
class ArgParser(object):
    def __init__(self):
        self._argparser = argparse.ArgumentParser(
            prog = "Meal Planning App",
            add_help = True,
            epilog = "For more information please visit: "\
                "https://github.com/Nick-Getka/meal_app_code",
            description = "Meal Planning application that creates a smart weekly meal plan."
        )
        self._parsedargs = None

        #adding the arguments
        self._argparser.add_argument(
            "-m", "--meal",
            type = int,
            choices = range(1,16,2),
            required = True,
            dest = "meal_count",
            help = 'Enter number of meals to plan (1, 3, 5, or 7)'
            )
        self._argparser.add_argument(
            "-r", "--read",
            choices = ("csv","db"),
            required = True,
            dest = "read_type",
            help = "Enter where the planner should "\
                "read the data from either from CSV (csv) or database (db)."
            )
        self._argparser.add_argument(
            "-f", "--file",
            dest = "data_path",
            help = "If reading from a .csv file, please include the path to the file."
            )
        self._argparser.add_argument(
            "-v","--vsm",
            action = "store_true",
            dest = "vsm",
            help = "By adding this argument and true sets the meal planner to"\
                    " use the vsm to rerank the recipies."
            )
        return None

    #parse the command line arguments
    def get_args(self, cache=True):
        #Cheking the cla were previously parsed
        if self._parsedargs is None or not cache:
            self._parsedargs = self._argparser.parse_args()
        #Error checking for csv which requires a path to the csv file
        if self._parsedargs.read_type == "csv" and self._parsedargs.data_path is None:
            self._argparser.error("Reading the data as a csv requires passing the path "\
            "to the data file. Using -f or --file.")
        return self._parsedargs
