import psycopg2
import math
import os

from recipe import *

__all__ = [
    "DataManager"
    ]

class DataManager(object) :
    def __init__(self):
        dbUser = os.environ.get('POSTGRES_USER', 'postgres')
        dbPass = os.environ.get('POSTGRES_PASSWORD', 'practice1234')
        dbIP = os.environ.get('POSTGRES_IP', '0.0.0.0')
        dbPort = os.environ.get('POSTGRES_Port', '5432')
        self.conn = psycopg2.connect(user=dbUser, password=dbPass, host=dbIP, port=dbPort)
        return None
    def __del__(self):
        self.conn.close()

    def fetchRecipes(self) :
        rArr = []
        cursor = self.conn.cursor()
        cursor.execute("SELECT recipe_id, name FROM recipe")
        rec_names = cursor.fetchall()
        for r in rec_names :
            tempList = []
            select = 'SELECT ingredient.name, ingredient.measure, recipe_ingredient_assoc.amount, ingredient.ingredient_id \
                    FROM recipe_ingredient_assoc \
                    FULL JOIN ingredient \
                    ON ingredient.ingredient_id = recipe_ingredient_assoc.ingredient_id \
                    WHERE recipe_id=%s' % r[0]
            cursor.execute(select)
            for item in cursor.fetchall() :
                tempList.append(Ingredient(item[0], item[1], item[2], item[3]))
            rArr.append(Recipe(r[1],tempList,r[0]))
        return rArr

    def fetchInverseIndex(self) :
        iIndex = []
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(recipe_id) FROM recipe')
        recipeCount = int(cursor.fetchall()[0][0])

        cursor.execute('SELECT ingredient_id, name FROM ingredient')
        for i in cursor.fetchall() :
            select = 'SELECT recipe.name \
                    FROM recipe_ingredient_assoc \
                    FULL JOIN recipe \
                    ON recipe.recipe_id = recipe_ingredient_assoc.recipe_id \
                    WHERE ingredient_id=%s' % i[0]
            cursor.execute(select)
            tempList = cursor.fetchall()
            idf = math.log(1+(recipeCount/len(tempList)))

            iIndex.append({
                'ingredient': i[1],
                'recipes': tempList,
                'idf':idf
            })
        return iIndex
