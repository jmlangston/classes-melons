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


class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    base_price = 5.0

    def get_price(self, qty):

        if qty >= 5:
            total = (qty * self.base_price) * 0.5
        else: 
            total = qty * self.base_price
        return total


# def make_class_from_list(melons):
    
#     class melons[0](object):

#     for melon_order in melons:

class CasabaOrder(object):
    species = 'Casaba'
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    base_price = 6.0

    def get_price(self, qty):
        total = qty * self.base_price * 1.5
        return total 


class SharlynOrder(object):
    species = 'Sharlyn'
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 5.0    

    def get_price(self, qty):
        total = qty * self.base_price * 1.5
        return total 

class Santa_Claus(object):
    species = 'Santa Claus'
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]
    base_price = 5.0    

    def get_price(self, qty):
        total = qty * self.base_price * 1.5
        return total

class Christmas(object):
    species = 'Christmas'
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter"]
    base_price = 5.0    

    def get_price(self, qty):
        total = qty * self.base_price
        return total

class Horned_Melon(object):
    species = 'Horned Melon'
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 5.0   

    def get_price(self, qty):
        total = qty * self.base_price * 1.5
        return total

class Xigua(object):
    species = 'Xigua'
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]
    base_price = 10.0 

    def get_price(self, qty):
        total = qty * self.base_price * 1.5
        return total

class Ogen(object):
    species = 'Ogen'
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Summer", 'Spring']
    base_price = 6.0   

    def get_price(self, qty):
        total = qty * self.base_price
        return total
