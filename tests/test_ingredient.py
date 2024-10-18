import pytest
from praktikum.ingredient import Ingredient
from data import ingredient_type_first, ingredient_name_first, ingredient_price_first


class TestIngredients:


    def test_get_ingredient_type(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient.type = ingredient.get_type()

        assert ingredient.type == ingredient_type_first

    def test_get_ingredient_name(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient.name = ingredient.get_name()

        assert ingredient.name == ingredient_name_first


    def test_get_ingredient_price(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient.price = ingredient.get_price()

        assert ingredient.price == ingredient_price_first


