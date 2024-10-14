from praktikum.bun import Bun
from data import bun_price, bun_name
class TestBuns:
    def test_get_bun(self):
        bun = Bun(bun_name, bun_price)
        bun.get_name()
        bun.get_price()
        assert bun.name == bun_name
        assert bun.price == bun_price

