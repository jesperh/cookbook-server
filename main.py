from fastapi import FastAPI
import json
from models import Recipe
from fastapi import HTTPException

app = FastAPI()

def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def find_recipe_by_id(recipe_id):
    recipes = load_recipes()
    for recipe in recipes:
        if recipe.get("id") == recipe_id:
            return recipe
    return None
    

@app.get("/")
def read_root():
    return {"Cook": "Book"}

@app.get("/recipes/{recipe_id}")
def find_recipe(recipe_id: int):
    recipe = find_recipe_by_id(recipe_id)
    if recipe:
        return {"recipe": recipe}
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/recipes")
def get_recipes():
    recipes = load_recipes()
    return recipes
