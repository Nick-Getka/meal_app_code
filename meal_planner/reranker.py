from recipe import *

class Reranker :
    def __init__(self, args) :
        self._args = args
        self._recArr = []
        self._terms = []
        return None
    def set_recArr(r) :
        self._recArr = r

    def rerank(self, selected):
        if len(selected) != 0 or len(self._recArr) ==0:
            if self._args.vsm : self._vsm(selected)
        return self._recArr

    def _vsm(self, selected) :
        query = []
        for s in selected :
            query += s.get_ingList()
        print query

        return None
