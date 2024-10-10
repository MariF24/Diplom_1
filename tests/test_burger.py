import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import bun_price_correct, bun_name_correct, ingredient_name_first_correct, ingredient_price_first_correct, ingredient_type_first_correct, ingredient_type_double_correct, ingredient_name_double_correct, ingredient_price_double_correct
class TestBurgers:

    def test_set_buns_true(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name_correct
        mock_bun.get_price.return_value = bun_price_correct
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingredients_type,ingredients_name,ingredients_price',
    [
        [ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct],
        [ingredient_type_double_correct, ingredient_name_double_correct, ingredient_price_double_correct],

    ]
                             )
    def test_add_ingredient_true(self, ingredients_type, ingredients_name, ingredients_price):
        ingredient = Ingredient(ingredients_type, ingredients_name, ingredients_price)
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]


    def test_remove_ingredient_true(self):
        ingredient = Ingredient(ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_true(self):

        ingredient_first = Ingredient(ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct)
        ingredient_double = Ingredient(ingredient_type_double_correct, ingredient_name_double_correct, ingredient_price_double_correct)
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)
        burger.move_ingredient(1,0)

        assert burger.ingredients[0] == ingredient_double
        assert burger.ingredients[1] == ingredient_first


    def test_get_price_true(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name_correct
        mock_bun.get_price.return_value = bun_price_correct
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient_first = Ingredient(ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct)
        ingredient_double = Ingredient(ingredient_type_double_correct, ingredient_name_double_correct, ingredient_price_double_correct)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)

        assert burger.get_price() == 115.0



    def test_get_receipt_true(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name_correct
        mock_bun.get_price.return_value = bun_price_correct
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient_first = Ingredient(ingredient_type_first_correct, ingredient_name_first_correct, ingredient_price_first_correct)
        ingredient_double = Ingredient(ingredient_type_double_correct, ingredient_name_double_correct, ingredient_price_double_correct)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)

        assert '==== Bulka ====' in burger.get_receipt()

