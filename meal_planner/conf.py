import os

class Conf(object) :
    class __Conf:
        def __init__(self) :
            self.iindex_path = os.getcwd()+r'/meal_planner/tmp/iindex.json'
            self.db_username = None
            self.db_password = None
            self.db_port = None
            self.db_ip = None

    instance = None

    def __new__(cls):
        if not Conf.instance:
            Conf.instance = Conf.__Conf()
        return Conf.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

#The singleton code is based on the example given on this site
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
