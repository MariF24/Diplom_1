import pytest
from praktikum.ingredient import Ingredient
from data import ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct, ingredient_type_incorrect, ingredient_name_incorrect, ingredient_price_incorrect


class TestIngredients:


    def test_get_correct_ingredient(self):
        ingredient = Ingredient(ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct)

        assert ingredient.type == ingredient_type_first_correct
        assert ingredient.name == ingredient_name_first_correct
        assert ingredient.price == ingredient_price_first_correct


    def test_get_incorrect_ingredient(self):
        ingredient = Ingredient(ingredient_type_incorrect, ingredient_name_incorrect, ingredient_price_incorrect)

        assert ingredient.get_type != ingredient_type_incorrect
        assert ingredient.get_name != ingredient_name_incorrect
        assert ingredient.get_price != ingredient_price_incorrect







