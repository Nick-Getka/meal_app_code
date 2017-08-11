import math

from conf import *
from recipe import *
from datamanager import *

class Reranker(object) :
    def __init__(self) :
        self._config = Conf()
        self._iindex = None
        return None

    def resetRank(self, recList) :
        for r in recList :
            r.weight = 1.0
        return None

    def rerank(self, recList, selected):
        if self._iindex is None or len(selected) == 0:
            self.build_iindex()
        else :
            if self._config.vsm :
                recList = self._vsm(recList, selected)
        return None

    def build_iindex(self) :
        man = DataManager()
        self._iindex = man.fetchInverseIndex()
        return None

    def _vsm(self, recList, selected) :
        query = []
        for s in selected:
            for i in s.getIngredientNames() :
                found = False
                index = 0
                while index < len(query) and not found :
                    if query[index]['ingredient'] == i :
                        query[index]['tf'] +=1
                        found = True
                    index +=1
                if not found :
                    found2 = False
                    ind = 0
                    idf = None
                    while ind < len(self._iindex) and not found2 :
                        if self._iindex[ind]['ingredient'] == i :
                            found2 = True
                            idf = self._iindex[ind]['idf']
                        ind +=1
                    query.append({
                        'ingredient': i,
                        'idf':idf,
                        'tf':1.0
                    })

        for rec in recList:
            score = 0.0
            query_doc_sum = 0.0
            query_sum = 0.0
            doc_sum = 0.0
            for x in rec.getIngredientNames():
                found = False
                query_weight = 0
                for y in query:
                    if y['ingredient'] == x :
                        query_weight = y['tf']*y['idf']

                doc_weight = 0
                for z in self._iindex:
                    if z['ingredient'] == x :
                        doc_weight = len(z['recipes'])*z['idf']

                query_doc_sum += (query_weight*doc_weight)
                query_sum += (query_weight*query_weight)
                doc_sum += (doc_weight*doc_weight)

            denom = math.sqrt(query_sum*doc_sum)
            if denom != 0 :
                score = query_doc_sum/denom
            rec.weight = score
        return None
