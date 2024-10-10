from praktikum.bun import Bun

from data import bun_price_correct, bun_name_correct, bun_name_incorrect, bun_price_incorrect
class TestBuns:
    def test_get_correct_bun(self):
        bun = Bun(bun_name_correct, bun_price_correct)

        assert bun.name == bun_name_correct
        assert bun.price == bun_price_correct

    def test_get_incorrect_bun(self):
        bun = Bun(bun_name_incorrect, bun_price_incorrect)

        assert bun.get_name != bun_name_incorrect
        assert bun.get_price != bun_price_incorrect
