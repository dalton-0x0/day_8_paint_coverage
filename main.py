import math

'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of 
wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can

e.g. Height = 2, Width = 4, Coverage = 5

number of cans 	= (2 * 4) / 5 = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded 
up to 2 cans.
'''

coverage = 5


def paint_calc(height, width, can_coverage):
    """function that calculates the amount of paint needed to for a certain area"""
    num_cans = (height * width) / can_coverage
    round_up_num_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_num_cans} cans of paint")


#  test run
paint_calc(height=15, width=5, can_coverage=coverage)
