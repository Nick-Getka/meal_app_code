from recipe import *
from conf import *
import json
import numpy as np
import math
import pprint as pp


class Reranker(object) :
    def __init__(self, args) :
        self._args = args
        self._recArr = []
        self._terms = []
        self._iindex = None
        self._config = Conf()
        return None
    def __del__(self) :
        os.remove(self._iindex)
    def set_recArr(self, r) :
        self._recArr = r

    def rerank(self, selected):
        if len(selected) != 0 or len(self._recArr) == 0:
            self._build_iindex()
            if self._args.vsm : self._vsm(selected)
        return self._recArr

    def _build_iindex(self) :
        if self._iindex is None:
            self._iindex = self._config.iindex_path
            terms = []
            for recipe in self._recArr:
                name = recipe.get_name()
                for ing in recipe.get_ingList() :
                    found = False
                    index = 0
                    while index < len(terms) and not found :
                        if ing == terms[index]['ingredient'] :
                            terms[index]['recipes'].append(name)
                            found = True
                        index +=1

                    temp_arr = []
                    temp_arr.append(name)
                    if not found :
                        terms.append({
                            'ingredient': ing,
                            'recipes': temp_arr,
                            'idf':None
                        })
            for t in terms :
                t['idf'] = math.log(1+(len(terms)/len(t['recipes'])))
            f = open(self._iindex, 'w')
            json.dump(terms, f, indent=4)
            f.close()
        return None


    def _vsm(self, selected) :



        f = open(self._iindex, 'r')
        ii = json.load(f)
        f.close()

        query = []
        for s in selected:
            for i in s.get_ingList() :

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
                    while ind < len(ii) and not found :
                        if ii[ind]['ingredient'] == i :
                            found2 = True
                            idf = ii[ind]['idf']
                        ind +=1
                    query.append({
                        'ingredient': i,
                        'idf':idf,
                        'tf':1
                    })

        pp.pprint(query)

        temp = self._recArr
        for rec in temp:
            score = 0
            query_doc_sum = 0
            query_sum = 0
            doc_sum = 0
            for x in rec.get_ingList():
                found = False
                query_weight = 0
                for y in query:
                    if y['ingredient'] == x :
                        query_weight = y['tf']*y['idf']

                doc_weight = 0
                for z in ii:
                    if z['ingredient'] == x :
                        doc_weight = len(z['recipes'])*z['idf']


                query_doc_sum += (query_weight*doc_weight)
                query_sum += query_weight*query_weight
                doc_sum += doc_weight*doc_weight

            denom = math.sqrt(query_sum*doc_sum)
            if denom != 0 :
                score = query_doc_sum/denom
            rec.set_weight(score)

        return temp
