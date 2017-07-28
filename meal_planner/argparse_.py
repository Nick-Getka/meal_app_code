import argparse

class ArgParser(object):
    def __init__(self):
        self._argparser = argparse.ArgumentParser(
            description = "Meal Planning App",
        )
        self._parsedargs = None
        self.setup()

    def setup(self):
        self._argparser.add_argument(
            "-m", "--meal",
            action = "store_const",
            const = True,
            type = int,
            choices = range(1,7,2),
            required = True,
            dest = "meal_count",
            help = 'Enter number of meals to plan (1, 3, 5, or 7)'
        )
        self._argparser.add_argument(
            "-r", "--read",
            action = "store_const",
            const = True,
            choices = ("csv","db"),
            required = True,
            dest = "read_type",
            help = "Enter where the planner should read the data from either from CSV (csv) or database (db)."
        )
        self._argparser.add_argument(
            "-f", "--file",
            action = "store_const",
            const = True,
            dest = "data_path",
            help = "If reading from a .csv file, please include the path to the file."
        )
        return None
    def get_args(self, cache=True):
        if self._parsedargs is None or not cache:
            self._parsedargs = self._argparser.parse_args()

        rt = self._parsedargs.read_type.lower()
        if rt == "csv" and self._parsedargs.data_path is None:
            parser.error("Reading the data as a csv requires passing the path to the data file. Using -f or --file.")

        return self._parsedargs
