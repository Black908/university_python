"""class Calculator:
    def sum(self, x,y):
        return x+y
    def minus(self, x,y):
        return x-y
    def multiply(self, x,y):
        return x*y
    def divide (self, x,y):
        return x/y

calc = Calculator()
print(calc.cum(1,2))
"""
from  tkinter import *

calc_index = 0

def click_btn7():
    global clacl_index
    ent.insert(calc_index, '7')
    calc_index = calc_index+1
def click_btn8():
    global calc_index
    ent.insert(calc_index,'8')
    calc_index = calc_index +1
def click_btnPlus():
    global clac_index
    ent.insert(clac_index, '+')
    calc_index = calc_index +1
def click_btnMinus():
    global clac_index
    ent.insert(clac_index, '-')
    calc_index = calc_index +1