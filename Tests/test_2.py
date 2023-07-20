'''Демонстрация'''
import sys
from datetime import datetime
class Car:
    '''описание класса'''
    def __init__(self, color, make, model, year, ctype):
        '''Описание метода'''
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.ctype = ctype
        if "Linux" == sys.platform:
            print("You're using Linux!")
        self.weight = self.get_weight(ctype)

    def get_weight(ctype):
        '''Описание метода'''
        if ctype == 1:
            return 2000
        return None