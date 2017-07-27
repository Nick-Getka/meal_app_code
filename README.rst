# meal_app_docker
Dockerfile and other docker related files to setting up the container network for the meal planning app

Meal Planner App

Final Goal:
Given a list of recipes, this app is intended to create an efficient meal plans, matching recipes based on ingredients, preference rankings, and other factors. The final app with take allow users to add, remove and modify recipes as well as allow them to give them a preference score of 1, 2, 3, or 4 (in ascending order of preference).  The final app will also take into account the raw ingredients the user has left over from the week before, keeping a "digital pantry" updated based on the meals selected for the week and user input.  Finally the app will rank meals based on how efficiently they use food.  For example if one meal uses say half an onion, the app will give more weight to another recipe that would use the other half of the onion.

v1:
Version 1 of this app will contain only the core of this idea.  The recipes will be maintained in a postgresql database (an er diagram of the db is in the database folder), and a command line based application that will take the number of meals (1, 3, 5, 7) as the only parameter.  The digital pantry is not part of this initial version, neither is the preference score, or recipe adding/removing/editing.  This version will select meals based on recipes loaded into the database from a test_data.csv file found in database/data folder.

Code:

How to Run:
To run see the meal_app_docker repo
