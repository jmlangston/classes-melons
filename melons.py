"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3:
            total = (qty * self.base_price) * 0.75
        else:
            total = qty * self.base_price

        return total

