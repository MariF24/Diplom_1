import pytest
from praktikum.ingredient import Ingredient
from data import ingredient_type_first, ingredient_name_first, ingredient_price_first


class TestIngredients:


    def test_get_ingredient(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient.get_type()
        ingredient.get_name()
        ingredient.get_price()
        assert ingredient.type == ingredient_type_first
        assert ingredient.name == ingredient_name_first
        assert ingredient.price == ingredient_price_first







